
import re
def normalize_phone(phone_number):

    pattern = r"[+0-9]"
    phone_list = re.findall(pattern, phone_number)
    if len(phone_list) == 10:
        phone_list = [*["+","3","8"], *phone_list]
    if phone_list[0] != "+":
        phone_list = ["+", *phone_list]
    phone = ""    
    for x in phone_list: 
        phone += x  
    return(phone)

raw_numbers = "380tg 44@ 1а23* 4./567"

print(normalize_phone(raw_numbers))


