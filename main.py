import psutil
import requests
import os
import subprocess

def check_process(process_name):
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            if process_name.lower() in proc.info['name'].lower():
                return proc.info['exe'], proc
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return None, None

def download_file(url, dest_path):
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(dest_path, 'w', encoding='utf-16') as f:
            f.write(response.text)
        print(f"Файл успішно завантажено до {dest_path}.")
    except requests.RequestException as e:
        print(f"Помилка при завантаженні файлу: {e}")

def restart_process(exe_path):
    try:
        print("Перезапуск процесу...")
        subprocess.Popen(exe_path)
        print(f"Процес {exe_path} успішно перезапущено.")
    except Exception as e:
        print(f"Помилка при перезапуску процесу: {e}")

if __name__ == "__main__":
    process_name = "MiniBin.exe"
    exe_path, process = check_process(process_name)
    
    if exe_path:
        print(f"Процес {process_name} запущено.")
        process_dir = os.path.dirname(exe_path)
        print(f"Каталог процесу: {process_dir}")
        
        ini_file_path = os.path.join(process_dir, 'minibin-language.ini')
        
        ini_file_url = "https://raw.githubusercontent.com/liubquanti/MiniBin-UA/main/minibin-language.ini"
        download_file(ini_file_url, ini_file_path)
        
        try:
            print("Зупинка процесу...")
            process.terminate()
            process.wait()
            print(f"Процес {process_name} успішно зупинено.")
        except Exception as e:
            print(f"Помилка при зупинці процесу: {e}")
        
        restart_process(exe_path)
        
    else:
        print(f"Процес {process_name} не знайдено.")
