"""
验证码测试功能

Author: RuNa
Version: 1.0
Date: 2025-11-02
"""
import random
import string

ALL_CHARS = str(string.digits + string.ascii_letters) # 所有字元 = 0~9 + A~Z大小写
# Chars;字元, digits;数位

def judgment_code(a, b):
    if a == b:
        return print("\033[2;30;42m通过验证！\033[0m")
    elif a != b:
        return print("\033[2;30;41m验证失败。\033[0m")

def generate_code(*, code_len=4): # 生成随机码, 预设长度=4
    return ''.join(random.choices(ALL_CHARS, k=code_len))

while True:
    # 生成验证码
    CAPTCHA_code = {'code': 'none'}
    CAPTCHA_code['code'] = generate_code(code_len=5)
    print(f'\033[2;37;40m验证码为：{CAPTCHA_code['code']}\033[0m')

    #输入验证码
    your_code = {'code': 'none'}
    your_code['code'] = str(input("\033[2;37;40m请输入验证码：\033[2;37;40m"))

    # 判断是否正确
    if your_code['code'] == CAPTCHA_code['code']:
        print("\033[2;30;42m通过验证！\033[0m")
        break
    elif your_code['code'] != CAPTCHA_code['code']:
        print("\033[2;30;41m验证失败。\033[0m")
        break

# 避免重复
your_code.clear()
CAPTCHA_code.clear()

