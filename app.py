import time
import csv
import requests
import logging
import os
from datetime import datetime
from fake_useragent import UserAgent

# Настройка логирования
log_file_path = 'dogs_service.log'
if not os.path.exists(log_file_path):
    open(log_file_path, 'w').close()

logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s %(message)s')

def claim_request(url, proxy, user_id):
    fake_useragent = UserAgent()
    user_agent = fake_useragent.random
    current_time = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")

    params = {
        'user_id': user_id
    }
    headers = {
        'User-Agent': user_agent,
        'Accept': "application/json",
        'sec-ch-ua': "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Android WebView\";v=\"126\"",
        'sec-ch-ua-mobile': "?1",
        'sec-ch-ua-platform': "\"Android\"",
        'origin': "https://onetime.dog",
        'x-requested-with': "org.telegram.messenger",
        'sec-fetch-site': "same-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://onetime.dog/",
        'accept-language': "en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7",
        'if-modified-since': current_time,
        'priority': "u=1, i"
    }

    proxies = {
        'http': proxy,
        'https': proxy
    }
      
    response = requests.get(url, params=params, headers=headers, proxies=proxies)
    return response.json()

def read_csv(file_path):
    data = []
    if not os.path.exists(file_path):
        logging.warning(f"CSV file {file_path} does not exist. Creating an empty CSV file.")
        with open(file_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['discription', 'proxy', 'userid'])  # Записываем заголовок

    try:
        with open(file_path, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if len(row) == 3:  # Проверяем, что строка содержит 3 поля
                    entry = {
                        'discription': row[0],
                        'proxy': row[1],
                        'userid': row[2]
                    }
                    data.append(entry)
        logging.info("CSV file read successfully")
    except Exception as e:
        logging.error(f"Error reading CSV file: {e}")
    return data

def claim_function(file_path):
    while True:
        logging.info("Starting a new cycle of claim_function")
        data = read_csv(file_path)
        for entry in data:
            try:
                url = "https://api.onetime.dog/rewards"
                response_json = claim_request(url, entry['proxy'], entry['userid'])
                
                total = response_json.get('total')
                streak = response_json.get('streak')

                logging.info(f"{entry['discription']} join function : total={total}, streak={streak}")
            except Exception as e:
                logging.error(f"Error during claim request: {e}")
        logging.info("Sleeping for 6 hours")
        time.sleep(6 * 60 * 60)  # Sleep for 6 hours (6 * 60 minutes * 60 seconds)

if __name__ == '__main__':
    file_path = 'file.csv'  # Обратите внимание на полный путь
    logging.info("Starting claim function")
    claim_function(file_path)
