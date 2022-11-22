from time import sleep
 
def loe_alla(number, lõpp):
    while number >= lõpp:
        print(number)
        number -= 1
        sleep(1)
 
loe_alla(4,2)
loe_alla(500,499)