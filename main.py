import psutil
import requests
import os
import subprocess
import time

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
        os.system('cls')
        print(f">>> MiniBin UA")
        print(f">>> Oleh Liubchenko")
        print(f"")
        print(f">>> Файл успішно завантажено до {dest_path}.")
        time.sleep(1.0)
    except requests.RequestException as e:
        os.system('cls')
        print(f">>> MiniBin UA")
        print(f">>> Oleh Liubchenko")
        print(f"")
        print(f">>> Помилка при завантаженні файлу: {e}")
        time.sleep(1.0)

def restart_process(exe_path):
    try:
        os.system('cls')
        print(f">>> MiniBin UA")
        print(f">>> Oleh Liubchenko")
        print(f"")
        print(f">>> Перезапуск процесу...")
        time.sleep(1.0)
        subprocess.Popen(exe_path)
        os.system('cls')
        print(f">>> MiniBin UA")
        print(f">>> Oleh Liubchenko")
        print(f"")
        print(f">>> Процес {exe_path} успішно перезапущено.")
        time.sleep(1.0)
    except Exception as e:
        os.system('cls')
        print(f">>> MiniBin UA")
        print(f">>> Oleh Liubchenko")
        print(f"")
        print(f">>> Помилка при перезапуску процесу: {e}")
        time.sleep(1.0)

if __name__ == "__main__":
    process_name = "MiniBin.exe"
    exe_path, process = check_process(process_name)
    
    if exe_path:
        os.system('cls')
        print(f">>> MiniBin UA")
        print(f">>> Oleh Liubchenko")
        print(f"")
        print(f">>> Процес {process_name} запущено.")
        time.sleep(1.0)
        process_dir = os.path.dirname(exe_path)
        os.system('cls')
        print(f">>> MiniBin UA")
        print(f">>> Oleh Liubchenko")
        print(f"")
        print(f">>> Каталог процесу: {process_dir}")
        time.sleep(1.0)
        
        ini_file_path = os.path.join(process_dir, 'minibin-language.ini')
        
        ini_file_url = "https://raw.githubusercontent.com/liubquanti/MiniBin-UA/main/minibin-language.ini"
        download_file(ini_file_url, ini_file_path)
        
        try:
            os.system('cls')
            print(f">>> MiniBin UA")
            print(f">>> Oleh Liubchenko")
            print(f"")
            print(">>> Зупинка процесу...")
            time.sleep(1.0)
            process.terminate()
            process.wait()
            os.system('cls')
            print(f">>> MiniBin UA")
            print(f">>> Oleh Liubchenko")
            print(f"")
            print(f">>> Процес {process_name} успішно зупинено.")
            time.sleep(1.0)
        except Exception as e:
            os.system('cls')
            print(f">>> MiniBin UA")
            print(f">>> Oleh Liubchenko")
            print(f"")
            print(f">>> Помилка при зупинці процесу: {e}")
            time.sleep(1.0)
        
        restart_process(exe_path)
        
    else:
        os.system('cls')
        print(f">>> MiniBin UA")
        print(f">>> Oleh Liubchenko")
        print(f"")
        print(f">>> Процес {process_name} не знайдено.")
        time.sleep(1.0)
