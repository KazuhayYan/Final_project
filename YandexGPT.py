import requests
import logging
from Configuration import YaGPT_URL, LOGS, Speech_kit_URL_tts, MAX_GPT_TOKENS, SYSTEM_PROMT
from creds import get_creds

logging.basicConfig(filename=LOGS, level=logging.ERROR, format="%(asctime)s FILE: %(filename)s IN: %(funcName)s MESSAGE: %(message)s", filemode="w")

def count_gpt_tokens(messages):
    IAM_TOKEN, FOLDER_ID = get_creds()
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/tokenizeCompletion"
    headers = {
        'Authorization': f'Bearer {IAM_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        'modelUri': f"gpt://{FOLDER_ID}/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.7,
            "maxTokens": f"{MAX_GPT_TOKENS}",
            "reasoningOptions": {
                 "mode": "DISABLED"
            },
        },
        "messages": messages
    }
    try:
        return len(requests.post(url=url, json=data, headers=headers).json()['tokens'])
    except Exception as e:
        logging.error(e)
        return 0

def ask_gpt(messages):
    IAM_TOKEN, FOLDER_ID = get_creds()
    url = YaGPT_URL
    headers = {
        "Accept": "application/json",
        'Authorization': f'Bearer {IAM_TOKEN}'
    }
    data = {
        'modelUri': f"gpt://{FOLDER_ID}/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.7,
            "maxTokens": MAX_GPT_TOKENS,
            "reasoningOptions": {
                "mode": "DISABLED"
            }
        },
        "messages": [
            SYSTEM_PROMT,
            {"role": "user", "text": f"{messages}"}
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code != 200:
            return False, f"Ошибка GPT. Статус-код: {response.status_code}", None
        answer = response.json()['result']['alternatives'][0]['message']['text']
        tokens_in_answer = count_gpt_tokens([{'role': 'assistant', 'text': answer}])
        return True, answer, tokens_in_answer
    except Exception as e:
        logging.error(e)
        return False, "Ошибка при обращении к GPT",  None

def text_to_speech(text: str):
    IAM_TOKEN, FOLDER_ID = get_creds()
    headers = {
        'Authorization': f'Bearer {IAM_TOKEN}',
    }
    data = {
        'text': text,
        'lang': 'ru-RU',
        'voice': 'filipp',
        'folderId': FOLDER_ID,
    }
    response = requests.post(Speech_kit_URL_tts, headers=headers, data=data)
    if response.status_code == 200:
        return True, response.content
    else:
        return False, "При запросе в SpeechKit возникла ошибка"

def speech_to_text(data):
    IAM_TOKEN, FOLDER_ID = get_creds()
    params = "&".join([
        "topic=general",
        f"folderId={FOLDER_ID}",
        "lang=ru-RU"
    ])
    headers = {
        'Authorization': f'Bearer {IAM_TOKEN}',
    }
    response = requests.post(
        f"https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?{params}",
        headers=headers,
        data=data
    )
    decoded_data = response.json()
    if decoded_data.get("error_code") is None:
        return True, decoded_data.get("result")
    else:
        return False, "При запросе в SpeechKit возникла ошибка"