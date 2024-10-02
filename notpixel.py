import requests
from colorama import Fore, Style
import random
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import subprocess
import json

def print_welcome_message():
    print(Fore.WHITE + r"""
          
🆂🅸🆁🅺🅴🅻
          
█▀▀ █▀▀ █▄░█ █▀▀ █▀█ █▀█ █░█ █▀
█▄█ ██▄ █░▀█ ██▄ █▀▄ █▄█ █▄█ ▄█
          """)
    print(Fore.GREEN + Style.BRIGHT + "Not Pixel BOT")
 
 
def check_user(query):
    url = 'https://notpx.app/api/v1/users/me'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'authorization': f'initData {query}',
        'dnt': '1',
        'origin': 'https://image.notpx.app',
        'priority': 'u=1, i',
        'referer': 'https://image.notpx.app/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"Name : {data['firstName']}")
            print(f"Balance : {data['balance']}")
            print(f"Repaints : {data['repaints']}")
        else:
            print(f"Failed to fetch data for query: {query}, Status Code: {response.status_code}")
            return False  # Tambahkan return False jika gagal
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False  # Tambahkan return False jika terjadi exception
    return True  # Tambahkan return True jika berhasil

def playing_game(query):
    url = 'https://notpx.app/api/v1/repaint/start'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'initData {query}',
        'content-type': 'application/json',
        'origin': 'https://image.notpx.app',
        'priority': 'u=1, i',
        'referer': 'https://image.notpx.app/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }
    while True:
        data = {
            "pixelId": random.randint(10000, 99999),
            "newColor": "#493AC1"
        }

        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            print("Sukses Repaint")
        elif response.status_code == 400:
            error_data = response.json()
            if error_data.get("code") == 16:
                print("Repaint tidak cukup")
                break  # Keluar dari loop jika response code 400/16
            else:
                print(f"Error: {error_data.get('error')}")
                break  # Keluar dari loop jika ada error lain
        else:
            print(f"Failed with status code: {response.status_code}")
            break  # Keluar dari loop jika status code bukan 200 atau 400

def claim_mining(query):
    url = 'https://notpx.app/api/v1/mining/claim'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'authorization': f'initData {query}',
        'dnt': '1',
        'origin': 'https://image.notpx.app',
        'priority': 'u=1, i',
        'referer': 'https://image.notpx.app/',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        try:
            data = response.json()
            print(f"{data['claimed']} ter claim")
        except ValueError:
            print("Gagal mem-parsing JSON")
    elif response.status_code == 500:
        print("Belum waktunya claim")
    else:
        print("Error:", response.status_code)

def get_tasks_from_file():
    with open('task.txt', 'r') as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks if task.strip()]

def clear_tasks(query):
    tasks = get_tasks_from_file()
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'authorization': f'initData {query}',
        'dnt': '1',
        'origin': 'https://image.notpx.app',
        'priority': 'u=1, i',
        'referer': 'https://image.notpx.app/',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }

    for task in tasks:
        url = f'https://notpx.app/api/v1/mining/task/check/{task}'
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            try:
                response_json = response.json()
                if response_json.get(task) == True:
                    print(f"{task} Berhasil")
                elif response_json.get(task) == False:
                    print(f"{task} Sudah Selesai")
                else:
                    print(f"{task}: Sudah Selesai")
            except json.JSONDecodeError:
                print(f"Failed to decode JSON response for task {task}: {response.text}")
        else:
            print(f"Error fetching task {task}: {response.status_code} {response.text}")

def main():
    print_welcome_message()
    while True:
        with open('query.txt', 'r') as file:
            queries = file.readlines()
        
        for query in queries:
            query = query.strip()
            if query:
                if not check_user(query):
                    continue  # Lanjut ke query berikutnya jika check_user gagal
                playing_game(query)
                claim_mining(query)
                print("Clear Task")
                clear_tasks(query)  
        
        time.sleep(10)  # Tunggu 10 detik sebelum membaca file lagi

if __name__ == "__main__":
    main()