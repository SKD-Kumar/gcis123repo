import random

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
    
    l1.insert(3, 10) #inserts 100 at index 2
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
    t1 = (1,2,5)
    list3 = make_list(t1)
    print(list3, "Before scaling")
    list4 = scale(list3, 3)
    print(list4, "After scaling")

    an_int = 5
    a_list = [an_int]
    a_list,an_int = mutater(a_list, an_int)
    print("In main:", a_list)
    print("In main:", an_int)

    l1 = [1,2]
    l2 = [4,5,6,7]
    l3 = cat(l1, l2)
    print(l1,l2,l3, sep = '\n')

    l1 = [1,2]
    l2 = [4,5,6,7]
    l4 = extender(l1, l2)
    print(l1,l2,l4, sep = '\n')

    l1 = []
    for i in range(8):
        inserter(l1, i)
        print(l1)
    
    print("Before popping:", l1)
    l1 = popper(l1)
    print("After popping:", l1)

main()

