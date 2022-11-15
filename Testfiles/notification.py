import requests

def send_to_telegram(message):

    apiToken = secrets.api_token
    chatID = secrets.chat_id
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

send_to_telegram(f"Je pakje met barcode {'barcode'} werd zonet geleverd")