import random
from datetime import datetime, date

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def flip_coin():
    c = random.randint(0, 1)
    if c == 0:
        return "Testa"
    else:
        return "Croce"

def gen_emoji():
    emoji = ["\U0001f642", "\U0001F601", "\U0001F602", "\U0001F914", "\U00002764", "\U0001F389"]
    return random.choice(emoji)

def current_date():
    today_date = date.today()
    return today_date

def current_time():
    now_time = datetime.now().strftime("%H:%M:%S")
    return now_time
