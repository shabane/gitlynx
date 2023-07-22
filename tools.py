import re


def isValidateLink(link: str) -> bool:
    # this regex will validate URL base on [trojan, vless, vmess, ss] protocols
    if re.match(re.compile(r"^(https?://|ss://|vless://|vmess://|trojan://)"), link):
        return True
    return False
