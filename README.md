Алгоритм работы бота:
бот принимает текстовое или голосовое сообщение
если получен текст, он отправляется в качестве промта в YandexGPT
если получено голосовое сообщение:
оно расшифровывается в текст с помощью SpeechKit
бот отправляет текст в качестве запроса в YandexGPT
сгенерированный YandexGPT ответ бот направит в SpeechKit для превращения текста в голос
бот присылает пользователю ответ в том же формате, в котором пользователь присылал запрос: текст в ответ на текст, голос в ответ на голос