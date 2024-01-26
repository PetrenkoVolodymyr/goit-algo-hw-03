import random

def get_numbers_ticket(start, end, quantity):
    if type(start) == int and type(end) == int and type(quantity) == int and start>0 and end<=1000 and quantity<=end-start+1:
        chosen=[]
        while len(chosen) < quantity:
            num = random.randint(start, end)
            if num in chosen:
                continue
            else:
                chosen.append(num)
        return(sorted(chosen))
    else:
        return('Введено некоректні дані')

print(get_numbers_ticket(1,49,6))