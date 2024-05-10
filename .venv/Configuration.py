Speech_kit_URL_tts = "https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize"
YaGPT_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
SYSTEM_PROMT = [{'role': 'system', 'text': 'Ты хороший собеседник. Общайся с пользователем на "ты". '
                                            'Поддерживай диалог. Не объясняй пользователю, что ты умеешь и можешь. '
                                            'Изображай человека'}]
MAX_USERS = 3
MAX_GPT_TOKENS = 120
COUNT_LAST_MSG = 5
MAX_USER_STT_BLOCKS = 10
MAX_USER_TTS_SYMBOLS = 5000
MAX_USER_GPT_TOKENS = 2000
HOME_DIR = '/home/student/Final_project/Final_project'
LOGS = f'{HOME_DIR}/logs.txt'
DATABASE_FILE = f'{HOME_DIR}/messages.db'
IAM_TOKEN_PATH = f'{HOME_DIR}/creds/iam_token.txt'
FOLDER_ID_PATH = f'{HOME_DIR}/creds/folder_id.txt'
BOT_TOKEN_PATH = f'{HOME_DIR}/creds/bot_token.txt'