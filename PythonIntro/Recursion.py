def sumOfRecursion(num_of_recursion):
    if(num_of_recursion == 1):
        return 1
    return num_of_recursion + sumOfRecursion(num_of_recursion)
#home work rewrite fibonnacci without recursion

#fibonacci
def  fibonacciReqursion(numberOfRecursion):
    if(numberOfRecursion == 0):
        return 0
    if(numberOfRecursion == 1):
        return  1
    return fibonacciReqursion(numberOfRecursion - 1) + fibonacciReqursion(numberOfRecursion -2)

print("Enter number for sum recursion")
num_of_recursion = int(input())
print("Enter num for fibonacci")
numberOfRecursion = int(input())
print(sumOfRecursion(num_of_recursion))
print(fibonacciReqursion(numberOfRecursion))