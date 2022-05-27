# Копирование содержимого из одного файла в другой

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print (f"Копирование данных из файла {from_file} в файл {to_file}")

# in_file = open (from_file, 'w')
# indata = in_file.read ()
# эти 2 строки можно заменить одной
indata = open(from_file).read ()

print (f"Исходный файл имеет размер {len(indata)} байт")

print (f"Целевой файл существует? {exists(to_file)}")
print ("Готов, нажмите клавишу Enter для продолжения или Ctrl+C для отмены")
input ()

out_file = open (to_file, 'w')
out_file.write (indata)

print ("Отлично, все сделано.")

out_file.close ()
# in_file.close ()    #Если выше две строки приводили в одну, то строка не нужна

# запускать с двумя аргументами
# python3 ex17.py test.txt new_file.txt

# сначала создаем простой файл
# echo "Это тестовый файл." >test.txt
# теперь можно просмотреть его
# cat test.txt
