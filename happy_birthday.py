print("Hello world!")
#just to print
l1 = ["name", "age", "city"]
#to make a list of items to be taken as input
def func1(x):
    '''
    x is the number of inputs to be taken
    this function will take x inputs
    and return them in a list
    by asking the user for each input
    via a for loop
    '''
    print("""You will be asked to 
          enter """,x," inputs")
    l2 = []
    for i in range(x):
        print("Enter your ",l1[i],": ", end = "")
        var = input()
        l2.append(var)
    return l2
print(func1(3))
print(var)
'''
this way i will be taking multiple inputs
and storing them in a list
and then returning that list
within a single function'''