print("Hello world!")
l1 = ["name", "age", "city"]
def func1(x):
    l2 = []
    for i in range(x):
        var = input("Enter your ",l1[i],": ")
        l2.append(var)
    return l2
print(func1(3))