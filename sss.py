import sys
from time import sleep

def check_simple_number (number):
    tmp = True
    number = number*(-1) if number<0 else number
    for item in range(2,11):
         if number != item:
             if number % item == 0:
                 tmp = False
    return tmp

if __name__ == '__main__':
    start = sys.argv[1]
    end = sys.argv[2]
    print(str(start))
    print(str(end))
    sleep(1)
    for item in range(int(start),int(end)+1):
        if check_simple_number(item):
            print(str(item))

