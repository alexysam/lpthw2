# запускать python ex16.py test.txt
from sys import argv
script, filename = argv

print (f"Я собираюсь стереть файл {filename}.")
print ("Если вы не хотите стирать его, нажмите ctrl+C (^C).")
print ("Если хотите стереть файл, нажмите Enter.")

input ("?")

print ("Открытие файла...")
target = open (filename, "w")

print ("Очистка файла. До свидания!")
target.truncate()

print ("Теперь я запрашиваю у вас три строки.")

line1 = input ("строка1: ")
line2 = input ("строка2: ")
line3 = input ("строка3: ")

print ("Это я запишу в файл.")

target.write (line1)
target.write ("\n")
target.write (line2)
target.write ("\n")
target.write (line3)
target.write ("\n")

print ("И наконец, я закрою файл.")
target.close ()

#close - закрывает файл с сохранением
#read - считывает файл, результат можно присвоить переменной
#redline - считывает одну строку
#truncate - очищает файл
#write(stuff) - записывает данные в файл
#seek(0) - перемещает указатель в начало файла
