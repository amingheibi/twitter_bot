from pathlib import Path
import csv
import json


def check_response(response):
    if response.status_code != 200:
        print(response.status_code)
        print(response.text)
        return 1
    return 0


def get_keywords():
    lines = []
    with open(Path('data/keywords.txt'), 'r', encoding='utf-8') as input_file:
        lines = input_file.read().splitlines()
    return lines


def write_to_csv_file(response, file_path):
    with open(file_path, 'w', newline='', encoding="utf-8") as csvfile:
        csvw = csv.writer(csvfile)
        # csvw.writerow(['tweet_id','author_id','text','entities'])
        # simplify tweet for readablity
        csvw.writerow(['tweet_id', 'text'])
        for item in response.json()['data']:
            # csvw.writerow([item['id'],item['author_id'],item['text'],json.dumps(item.get('entities','N/A'))])
            csvw.writerow([item['id'], item['text']])
