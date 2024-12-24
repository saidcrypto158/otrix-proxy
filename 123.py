import requests
import time
from datetime import datetime
from colorama import Fore, Style


# Токен аккаунта
TOKEN = "123"

# ID канала или ветки
CHANNEL_OR_THREAD_ID = "1319450142914646069"

# URL для отправки сообщения
URL = f"https://discord.com/api/v9/channels/{CHANNEL_OR_THREAD_ID}/messages"

HEADERS = {
    "Authorization": TOKEN,
    "Content-Type": "application/json"
}

# Путь к файлу с сообщениями
MESSAGES_FILE = "messages.txt"

# Прокси-сервер в формате login:password:ip:port
PROXY = "login:pass@ip:port"

# Настройка прокси для requests
proxies = {
    "http": f"http://{PROXY}",
    "https": f"http://{PROXY}",
}

def load_messages(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            messages = [line.strip() for line in file if line.strip()]
        if not messages:
            raise ValueError("Файл с сообщениями пуст!")
        return messages
    except FileNotFoundError:
        print(f"{Fore.RED}[ОШИБКА]{Style.RESET_ALL} Файл {file_path} не найден.")
        exit(1)
    except ValueError as e:
        print(f"{Fore.RED}[ОШИБКА]{Style.RESET_ALL} {e}")
        exit(1)

# Функция отправки сообщения
def send_message(content):
    message = {"content": content}
    try:
        response = requests.post(URL, headers=HEADERS, json=message, proxies=proxies)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if response.status_code == 200:
            print(f"{Fore.GREEN}[УСПЕХ_ДАО]{Style.RESET_ALL} Сообщение отправлено: '{content}' в {current_time}")
        else:
            print(f"{Fore.RED}[ОШИБКА_ДАО]{Style.RESET_ALL} Код ошибки: {response.status_code}. Ответ: {response.text}")
    except requests.exceptions.ProxyError as e:
        print(f"{Fore.RED}[ОШИБКА_ПРОКСИ]{Style.RESET_ALL} Проблема с прокси-сервером: {e}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}[ОШИБКА_СЕТИ]{Style.RESET_ALL} Проблема с запросом: {e}")

# Основной цикл
def main():
    messages = load_messages(MESSAGES_FILE)
    for message in messages:
        send_message(message)
        time.sleep(68)  # Пауза 68 секунд между сообщениями
    print("\nВсе сообщения отправлены. Скрипт завершен.")


# Запуск
if __name__ == "__main__":
    main()
