"""import random

def lists():
    l1 = list()
    for i in range(5):
        l1.append(input("Enter element: "))
    '''Method-1:
    for i in l1:
        #before modification:
        #print(i)
        print(l1.index(i),":",i)'''
    
    #Method-2:
    for i in range(len(l1)):
        print(i,":",l1[i])
    
    l1.insert(2, 100) #inserts 100 at index 2
    print(l1)
    return l1

def make_list(a_sequence):
    L = []
    for i in a_sequence:
        L.append(i)
        print(L)
    return L

def scale(a_list, scalar):
    for i in range(len(a_list)):
        a_list[i] = a_list[i] * scalar
    return a_list

def mutater(a_list, an_int):
    print("Before mutation:", a_list)
    print("Before mutation:", an_int)
    an_int = an_int * 5
    a_list[0] = a_list[0] * 5
    print("After mutation:", a_list)
    print("After mutation:", an_int)
    return a_list, an_int

def cat(a_list, b_list):
    L = a_list+b_list
    return L

def extender(a_list, b_list):
    a_list+=(b_list)
    return a_list

def inserter(a_list, value):
    index = len(a_list)//2
    a_list.insert(index, value)
    return a_list

def popper(a_list):
    while a_list != []:
        a_list.pop(random.randint(0, len(a_list)-1))
        print("List:", a_list)
    return a_list

def main():
    list_main = lists()
    print(list_main)
    list2 = make_list('Hello')
    print(list2)

    #for scale function
    t1 = (1,2,3,4,5)
    list3 = make_list(t1)
    print(list3, "Before scaling")
    list4 = scale(list3, 3)
    print(list4, "After scaling")

    an_int = 2
    a_list = [an_int]
    a_list,an_int = mutater(a_list, an_int)
    print("In main:", a_list)
    print("In main:", an_int)

    l1 = [1,2,3]
    l2 = [4,5,6]
    l3 = cat(l1, l2)
    print(l1,l2,l3, sep = '\n')

    l1 = [1,2,3]
    l2 = [4,5,6]
    l4 = extender(l1, l2)
    print(l1,l2,l4, sep = '\n')

    l1 = []
    for i in range(5):
        inserter(l1, i)
        print(l1)
    
    print("Before popping:", l1)
    l1 = popper(l1)
    print("After popping:", l1)

main()"""
#above is by me (contains out of syllabus parts)
#doing it in class below:
"""def tuples(a_tuple):
    print("length of tuple",len(a_tuple))
    for i in a_tuple:
        print(i)
    try:
        a_tuple[0] = 100
    except TypeError as e: #this is part of classwork
        print("Tuples are immutable", e)
        '''Out of syllabus:
    except Exception as e:
        print("Tuples are immutable", e, "just error type",type(e).__name__)'''
tuples((1,2,3,4,5))"""

"""def lists():
    l1 = list(('s',1,'abc',2.5,True))
    for i in l1:
        print(i)
    print("Trying to change element at index 1")
    l1[0] = 100
    print(l1)
    # to print index also, dont use list.index() cause it is out of syllabus
    for ind in range(len(l1)):
        print(ind,":",l1[ind])
    return l1
if __name__ == "__main__":
    lists()"""

"""def make_list(a_sequence):
    l1 = list()
    for i in a_sequence:
        l1.append(i)
        print(l1)
    return l1


def scale(a_list, scalar):
    for i in range(len(a_list)):
        a_list[i] *= scalar
    print("Scaled list:", a_list)


def cat(a_list, b_list):
    return a_list+b_list

def main():
    main_list = make_list('Hello')
    print("Main list:", main_list)
    print("Before scaling:", main_list)
    scale(main_list, 3)
    print("After scaling:", main_list)
    c = cat([1,2,3], [4,5,6])
    print("Concatenated list:", c)
    """
#out of syllabus:
'''def hehe(t1, l1, int1):
    t1 = (4,5,6)
    l1.append(4)
    int1 += 5
    print("in function: ",t1,id(t1))
    print("in function: ",l1,id(l1))
    print("in function: ",int1,id(int1))

    l1 = [10,20,30]
    print("in function after reassigning list: ",l1,id(l1))
t_main = (1,2,3)
l_main = [1,2,3]
int_main = 5
hehe(t_main, l_main, int_main)
print("in main: ",t_main,id(t_main))
print("in main: ",l_main,id(l_main))
print("in main: ",int_main,id(int_main))'''

"""l1 = ['s','d','f']
print(''.join(l1))"""
