#this is comment in python language

'''
This is a multiline
comment.
'''
print("enter two numbers")
number_one = int(input())
number_two = int(input())

# Home work write logics with another operations
#use methods

def sumTwoNumbers(number_one, number_two):
    if(number_one < 0 or number_two < 0):
        return 0
    return  number_one + number_two


print(sumTwoNumbers(number_two, number_one))