#вводим с клавиатуры кол-во секунд
time=int(input('введите времяв секундах: '))

#подсчитываем часы, минуты, секунд
h=time//3600
m=(time-h*3600)//60
s=time-h*3600-m*60

#выводим данные
print(h,"часов",m,'минут',s,'секунд')
