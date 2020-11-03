from pathlib import Path


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
