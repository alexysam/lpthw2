# используется переменная argv, позволяющая получить имя файла
from sys import argv
script, filename = argv

# файл присваивается переменной и открывается
txt = open(filename)

print(f"Содержимое файла {filename}:")

# из переменной вызывается функция .read()
print (txt.read ())

# повторение 
print("Снова введите имя файла:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
