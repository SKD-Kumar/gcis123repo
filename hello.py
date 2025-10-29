'''def prompt(): #hahaha
    val1  = input("Enter first value: ")
    val2 = input("Enter second value: ")
    print("Addition:", val1 + val2)
    print("Subtraction:", val1 - val2)
    print("Multiplication:", val1 * val2)
    print("Division:", val1 / val2)
    print("Floor Division:", val1 // val2)
    print("Modulus:", val1 % val2)
    print("Exponent:", val1 ** val2)
    print("k bye")    

prompt()
'''
'''
def circle_area(radius):
    return 3.14159 * radius ** 2

def square_area(side):
    return side * side

def triangle_area(base, height):
    return 0.5 * base * height

def rectangle_area(length, width):
    return length * width

def main():
    area = circle_area(10)
    print("Area of circle with radius 10 is:", area)
    area = square_area(10)
    print("Area of square with side 10 is:", area)
    area = triangle_area(10, 5)
    print("Area of triangle with base 10 and height 5 is:", area)
    area = rectangle_area(10, 5)
    print("Area of rectangle with length 10 and width 5 is:", area)

main()
'''
'''
import math

pi = math.pi
def area_of_circle(radius):
    return pi * radius ** 2
def circumference_of_circle(radius):
    return 2 * pi * radius

def main():
    radius = 10
    area = area_of_circle(radius)
    circumference = circumference_of_circle(radius)
    print("Area of circle with radius", radius, "is:", area)
    print("Circumference of circle with radius", radius, "is:", circumference)
main()'''

'''write a program to read input from user and check if it palindrome'''
'''str1= input("Enter string to check: ")
str1_rev = str1[::-1]
if str1 == str1_rev:
    print("palindrome")
else:
    print("Not palindrome")'''

'''str1 = input("Enter: ")
print(str1)
for i in str1:
    print(i)
counter = 0
while counter<len(str1):
    print(str1[counter])
    counter+=1
print(str1[::-1])
'''

'''count = 0

while True:
    count = count + 1
    if count % 5 == 0:
        continue
    elif count >= 1000:
        break
    print(count)
print("Done!")'''

'''find of sum of all odd numbers provided by the user, and prompt him for input until he enters 0'''
'''sum_num = 0
while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    elif num%2 == 0:
        continue
    sum_num += num
print("Hehe, sum = ", sum_num)'''
"""
'''all numbers from 0 - 10'''
l1 = range(0,11)
'''all even numbers from 0 to 20'''
l2 = range(0,21,2)
'''all odd numbers from 5 to 15'''
l3 = range(5,16,2)
''' from 10 to zero'''
l4 = range(10,-1,-1)

for i in l1:
    print(i)
print()
for i in l2:
    print(i)
print()
for i in l3:
    print(i)
print()
for i in l4:
    print(i)
print()"""

'''def print_range(a_range):
    for i in a_range:
        print(i)'''

'''for i in range(1,6):
    print(i)

for i in range(0,11,2):
    print(i)

for i in 'apple':
    print(i)'''

'''for i in range(5,51,5):
    print('5 x ',i//5,'=', i)

for i in range(10,0,-1):
    print(i)

for i in range(1,6):
    print(i*i*i, end = ' ')'''

'''n = int(input(":"))

for i in range(n):
    for j in range(i+1):
        print('*', end = ' ')
    print()'''

'''str1 = input("Enter string: ")

str2 = ''
for i in str1:
    str2 = i + str2

print(str2)'''

"""def split_shit(str1, delimiter):
    tokens = str1.split(delimiter)
    for i in tokens:
        print(i)

print("Test1")
split_shit("That's my house, \" I said.", "\\")
print("Test2")
split_shit("one, two,\tth\\ree\nfour five", "\\")"""

import file_shit as fs
'''fs.print_lines("gen.py")
fs.word_search("prime.txt")
fs.longest_word("prime.txt")
fs.print_name_from_CSV("namecomma.csv")

#need to open a non-existing file with append mode to see what happens
with open("hello.txt","at") as f1:
    name = input("Enter name: ")
    f1.write(name + '\n') #important to add newline character'''

#fs.class_avg()

f1 = open("namecomma.csv",'at')
print(f1.write('hi,name'))