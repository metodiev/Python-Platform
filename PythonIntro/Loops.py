

def printForLoop(number):
    for i in range(1, number):
        print(i)

def printWhileLoop(number):
    while(number > 0):
        print(number)
        number=number-1

    #def printDoWhileLoop(number):
    #in python language there is no such thing as do while loop
print("Enter a Number12")
number =  int(input())
printForLoop(5)
printWhileLoop(number)

#home work write reverse cycles