from subprocess import Popen, PIPE
from multiprocessing import Process
import math
def start(start,end,process): #подаем на начало диапозон, конец диапозон и сам процесс
    rez=[]
    temp = True
    for i in range(int(start),int(end)+1):
        for g in range(2,10+1):
            if g != math.fabs(i): #позволяет работать с вещественными числами
                if math.fabs(i) % g == 0:
                    temp = False
                    break

        if temp == True:
            rez.append(i)
        temp= True
    print(f'Процесс: {process+1}, диапазон [{start},{end}], \n результат : {rez}\n')

if __name__ =='__main__':
    split = 2
    with Popen(['python','sss.py',' -1' ,"30"], stdout=PIPE) as task: #открытие дочернего процесса
        i = task.stdout.read().decode() #вызов инфы из стд в переменную, декодирует
        print(i)
    i = i.split('\n') #для того, чтобы строку представить в виде списка
    #print('Первые два числа в списке это диапазон')
    #print(i)
    list_ = []
    range_of_number = 0
    if int(i[0]) < 0:
        if int(i[1])<0:
            range_of_number = int(i[0]) + int(i[1])
            range_of_number = math.fabs(range_of_number) + 1
        elif int(i[1])>0:
            range_of_number = int(i[0]) - int(i[1])
            range_of_number = math.fabs(range_of_number) + 1
        elif int(i[1])==0:
            range_of_number = math.fabs(int(i[0])) + 1
    elif int(i[0]) >0:
        range_of_number = int(i[1]) - int(i[0]) + 1
    elif int(i[0]) == 0:
        range_of_number = int(i[1]) + 1

    shag = int(i[0])
    for g in range(split):
        f = Process(target=start ,args=(shag,shag+int(range_of_number/split)-1,g))
        shag = shag+int(range_of_number/split)
        list_.append(f)
        f.start()
    for i in list_:
        i.join()

