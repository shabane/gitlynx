import re
import random


def isValidateLink(link: str) -> bool:
    # this regex will validate URL base on [trojan, vless, vmess, ss] protocols
    if re.match(re.compile(r"^(https?://|ss://|vless://|vmess://|trojan://)"), link):
        return True
    return False


def chooseName() -> str:
    _alpha_bet_lowercase = "a b c d e f g h i j k l m n o p q r s t w x y z "
    _alpha_bet_uppercase = "A B C D E F G H I J K L M N O P Q R S T W X Y Z "
    _numerics = "1 2 3 4 5 6 7 8 9 0 "
    _chars = _alpha_bet_lowercase + _alpha_bet_uppercase + _numerics
    _chars = _chars.strip().split(' ')
    
    length = random.randint(2, 5)
    name = ""
    for i in range(length):
        name += random.choice(_chars)
    return name
