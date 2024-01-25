
import re
def normalize_phone(phone_number):
    sanitized_numbers=[]
    for item in phone_number:    
        pattern = r"[+0-9]"
        phone_list = re.findall(pattern, item)
        if len(phone_list) == 10:
            phone_list = [*["+","3","8"], *phone_list]
        if phone_list[0] != "+":
            phone_list = ["+", *phone_list]
        phone = ""    
        for x in phone_list: 
            phone += x  
        sanitized_numbers.append(phone)
    return("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

raw_numbers = [   "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "]

print(normalize_phone(raw_numbers))

