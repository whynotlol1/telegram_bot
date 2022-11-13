import requests
import json


def extract_arg(arg) -> list or None:
    return arg.split()[1:]


def to_fixed(num: float, digits: int) -> str:
    return f"{num:.{digits}f}"


def format_text(text: str) -> str:
    symbols = [',', '!', '?', '.', ':', ';']
    text_to_be_formatted = []
    for i in text:
        text_to_be_formatted.append(i)
    text_returned = ''
    for i in range(len(text_to_be_formatted)):
        try:
            if i == 0 or (text_to_be_formatted[i - 2] == '.' and text_to_be_formatted[i - 1] == ' '):
                text_returned += text_to_be_formatted[i].capitalize()
            elif i + 1 < len(text_to_be_formatted) and text_to_be_formatted[i] == ' ' and text_to_be_formatted[i + 1] in symbols:
                text_returned += text_to_be_formatted[i + 1]
                text_to_be_formatted[i + 1] = None
            else:
                text_returned += text_to_be_formatted[i]
        except TypeError:
            pass
    return text_returned


def get_crypto_price(crypto: str) -> str:
    key = f"https://api.binance.com/api/v3/ticker/price?symbol={crypto.upper()}USDT"
    response = requests.get(key)
    data = json.loads(response.text)
    return data['price']
