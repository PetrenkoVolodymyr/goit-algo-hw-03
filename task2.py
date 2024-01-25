import random

def get_numbers_ticket(min, max, quantity):
    if type(min) == int and type(max) == int and type(quantity) == int and min>0 and max<=1000 and quantity<=max-min+1:
        list=[]
        while len(list) < quantity:
            num = random.randint(min, max)
            if num in list:
                continue
            else:
                list.append(num)
        return(sorted(list))
    else:
        return('Введено некоректні дані')

print(get_numbers_ticket(1,49,6))