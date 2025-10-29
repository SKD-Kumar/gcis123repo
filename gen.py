'''def add():
  print('hi')
  print('hhehe')
add()


num= int(input("Enter number: "))
if num > 0:
    print("+ve")
elif num < 0:
    print("-ve")
else:
    print("zero")



num= int(input("Enter number: "))
if num %2 == 0:
    print("even")
else:
    print("odd")



num= int(input("Enter number: "))
if num >= 18:
    print("vote bee")
else:
    print("nah you still young")



def check_equilateral(a,b,c):
    if a==b==c:
        return True
    else:
        return False
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("ENter side c: "))
print(check_equilateral(a,b,c))
'''

'''
passwd = input("Enter password: ")
if passwd == 'python123':
    print("Access granted")
else:
    print("Access denied")'''

'''a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both are equal")'''


'''read age from the user and display if the user is a child(<13) teenager(<20) or adult(else)'''
'''age = int(input("Enter your age: "))
if age < 2:
    print("Infant")
elif age < 6:
    print("Toddler")
elif age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age > 60:
    print("Senior citizen")
else:
    print("Adult")'''


'''read the score_of_student of students, if score_of_student above 90 = A, above 75 = B,
above 65 = c, above 55 = d, else = f'''

"""score_of_student = int(input("Enter your score_of_student: "))
if score_of_student > 90:
    print("A")
elif score_of_student > 75:
    print("B")
elif score_of_student > 65:
    print("C")
elif score_of_student > 55:
    print("D")
else:
    print("F => Fail")
"""

'''a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
l1 = [a,b,c]
print("Greatest is: ", max(l1))'''

'''def isosceles(a,b,c):
    if not(equilateral(a,b,c)):
        if a==b or b==c or a==c:
            return True
    return False
    
def equilateral(a,b,c):
    if a==b==c:
        return True
    else:
        return False
def scalene(a,b,c):
    if not(equilateral(a,b,c) or isosceles(a,b,c)):
        return True
    else:
        return False

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
print("Isosceles: ", isosceles(a,b,c))
print("Equilateral: ", equilateral(a,b,c))
print("Scalene: ", scalene(a,b,c))'''


"""i = 1
while i<=5:
    print(i)
    i = i+1"""

'''i = 0
while i<=10:
    print(i)
    i = i+2'''

"""i = 10
while i>1:
    print(i)
    i = i-2"""

"""i = 1
while i <=5:
    print(i**2)
    i = i+1 """

'''i = 1
while i <=5:
    print(i**3)
    i = i+1 '''

'''sum = 0
i = 1
while i <=5:
    sum += i
    i = i+1
print("Sum is: ", sum)'''

'''
"""Countdown:"""
i = 5
sum = 0
while i >= 0:
    print(i)
    sum +=i
    i = i-1
print("Sum is: ", sum)

"""Countup"""
i = 0
sum = 0
while i <= 4:
    print(i)
    sum += i
    i = i+1
print("Sum is: ", sum)'''

'''def countup(num):
    sum = 0
    i = 0
    while i <= num:
        print(i)
        sum += i
        i+=1
    return sum

def main():
    num = int(input('Enter number: '))
    sum = countup(num)
    print(sum)
main()'''

'''
def countdown(number):

    total = 0

    while number >= 0:

        print(number)

        total += number

        number -= 1

    return total

def countup(number):

    total = 0

    i = 1

    while i <= number:

        print(i)

        total += i

        i += 1

    return total

def main():

    num = int(input("Enter a number: "))

    resultdown countdown(num)

    resultup = countup(num)
    print(resultup)
    print(resultdown)
    print('both are same')
main()'''

def main():

    num = int(input("Enter a number: "))

    resultdown countdown(num)

    resultup = countup(num)
    print(resultup)
    print(resultdown)
    print('both are same')