#  Теоретическая часть – Theoretical Part – Қисмати назариявӣ
# 1.Что такое рекурсия и как она работает?
# EN: What is recursion and how does it work?
# TJ: Рекурсия чист ва он чӣ тавр кор мекунад?



# блок который призывает себя и решает функцию внутри себя


# 2.Объясните разницу между функцией и замыканием.
# EN: Explain the difference between a function and a closure.
# TJ: Тафовут миёни функсия ва closure-ро фаҳмонед.


# closure аз функцияи берунги дарунгиро return мекунад


# 3.Для чего используются декораторы в Python?
# EN: What are decorators used for in Python?
# TJ: Декораторҳо дар Python барои чӣ истифода мешаванд?

# для того чтобы показать действия до, и после

# 4.**Что такое аргументы *args и kwargs?
# EN: What are *args and **kwargs?
# TJ: *args ва **kwargs чӣ маъно доранд?

# kwargs не находит ошибок
# args - для передачи аргументов


# 5.Чем отличаются локальные и глобальные переменные?
# EN: What is the difference between local and global variables?
# TJ: Тафовут миёни тағйирёбандаи маҳаллӣ ва умумӣ дар чист?

# локалные переменные - даруни функция худаш дохил меша
# global-общий функция дахл дора



# задача 1
# RU: Создайте функцию, которая выводит ваше имя и возраст.


# def greet(name="Али",age=20):
#     return f"Меня зовут {name}. Мне {age} лет."
# print(greet())   



# Задача 2
# RU: Создайте функцию, которая принимает два числа и выводит их сумму.

# EN: Create a function that takes two numbers and prints their sum.

# TJ: Функсияе эҷод кунед, ки ду ададро қабул карда, ҷамъашонро чоп кунад.

# 📥 Ввод / Input:

# 5 7
# 📤 Вывод / Output:


# def sum(a, b):
#      return a+b
# print(sum(5, 7))




# Задача 3
# RU: Создайте функцию, которая принимает строку и выводит её длину.

# EN: Create a function that takes a string and prints its length.

# TJ: Функсияе эҷод кунед, ки сатрро қабул карда, дарозии онро чоп кунад.

# 📥 Ввод / Input:


# hello
# 📤 Вывод / Output:

# 5

# def func(text):
#     print(len(text))
# func('hello')




# Задача 4
# RU: Создайте функцию, которая принимает список чисел и выводит сумму чётных чисел.

# EN: Create a function that takes a list of numbers and prints the sum of even numbers.

# TJ: Функсияе эҷод кунед, ки рӯйхати ададҳоро қабул карда, ҷамъбасти ададҳои ҷуфтро чоп кунад.

# 📥 Ввод / Input:

# [1, 2, 3, 4, 5, 6]
# 📤 Вывод / Output:

# 12


# def func(lst):
#     sum=0
#     for i in lst:
#         if i % 2 == 0:
#             sum+=i
#     return sum
# print (func(lst=[1,2,3,4,5,6]))






# Задача 5
# RU: Создайте функцию, которая возвращает n-е число Фибоначчи (рекурсивно).

# EN: Create a function that returns the n-th Fibonacci number (recursively).

# TJ: Функсияе эҷод кунед, ки адади n-уми Фибоначчиро бармегардонад (рекурсивӣ).

# 📥 Ввод / Input:

# 6
# 📤 Вывод / Output:

# 8

# def fib (n):
#     if n==1:
#         return 1
#     if n==2:
#         return 1
#     return fib(n-1)+fib(n-2)
# print(fib(6))




# Задача 6
# RU: Создайте функцию, которая возвращает замыкание, добавляющее заданное число к аргументу.

# EN: Create a function that returns a closure adding a fixed number to its argument.

# TJ: Функсияе эҷод кунед, ки closure бармегардонад, ки адади додашударо ба аргумент зам мекунад.

# 📥 Ввод / Input:


# add5 = make_adder(5); add5(10)
# 📤 Вывод / Output:
 
# 15


# def make_adder(m):
#     def inner (n):
#         return m+n
#     return inner
# add=make_adder(10)
# print(add(5))





# Задача 7
# RU: Создайте декоратор, который до вызова функции печатает "Выполняется...".

# EN: Create a decorator that prints "Running..." before calling the function.

# TJ: Декораторе эҷод кунед, ки пеш аз иҷро "Дар ҳоли иҷро..." чоп мекунад.

# 📥 Ввод / Input:

# @trace
# def hello():
#     print("Привет!")
# hello()
# 📤 Вывод / Output:

# Выполняется...
# Привет!


# def counter(func):
#     def inner(*args):
#         print('Выполняется...')
#         func(*args)
#     return inner


# @counter
# def hello():
#     print('Привет!')
# hello()




# Задача 8
# RU: Создайте функцию, которая принимает список строк и выводит самую длинную строку.

# EN: Create a function that takes a list of strings and prints the longest string.

# TJ: Функсияе эҷод кунед, ки рӯйхати сатрҳоро қабул карда, дарозтарин сатрро чоп кунад.

# 📥 Ввод / Input:

# ["apple", "banana", "kiwi", "strawberry"]
# 📤 Вывод / Output:
 
# strawberry

# str1=["apple", "banana", "kiwi", "strawberry"]
# long=""
# cnt=""

# for i in str1:
   
#         if len(cnt)>len(long):
#             long=cnt
#         cnt= ""

# print(long)



# Задача 9
# RU: Создайте функцию, которая принимает строку и рекурсивно переворачивает её.

# EN: Create a function that recursively reverses a string.

# TJ: Функсияе эҷод кунед, ки сатрро ба таври рекурсивӣ чаппа мекунад.

# 📥 Ввод / Input:

# text
 
# 📤 Вывод / Output:

 
# "nohtyp"

# def reverse_string(s):
#     if len(s)==1:
#         return s
#     return reverse_string(s[1:])+s[0]
# print(reverse_string('python'))




# Задача 10
# RU: Напишите декоратор, который подсчитывает количество вызовов функции и печатает его.

# EN: Write a decorator that counts how many times the function was called and prints it.

# TJ: Декораторе нависед, ки шумораи даъватҳои функсияро ҳисоб карда, чоп мекунад.

# 📥 Ввод / Input:

 
# @counter
# def f():
#     pass
# f()
# f()
# f()
# 📤 Вывод / Output:

 
# Функция вызвана 1 раз
# Функция вызвана 2 раз
# Функция вызвана 3 раз




# def counter(func):
#     n=0
#     def inner(*args):
#         nonlocal n
#         n+=1
#         print (f'функция вызвана',n, end=" ")
#         func(*args)
#     return inner


# @counter
# def f ():
#     print()
# f()
# f()
# f()


