import requests
import html
import os
os.system('clear')

API_ENDPOINT = 'https://opentdb.com/api.php'
PARAMETERS = {
    'amount': 10,
    'type': 'boolean'
}

response = requests.get(url=API_ENDPOINT, params=PARAMETERS)
response.raise_for_status()

question_data_raw = response.json()['results']
question_data = []

for item in question_data_raw:
    new_question = {
        'question': html.unescape(item['question']),
        'answer': item['correct_answer']
    }
    question_data.append(new_question)
