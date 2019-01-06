print("Enter your current age")

def check_user_age(age):
    if (age <= 18):
        return 0
    return  -1

#python doesn't has switch statment
def print_user_message(argument):
    switcher = {
        0: print_allow_site_message(),
       -1: print_warning_message()
    }
    return switcher.get(argument, "nothing")

def print_allow_site_message():
    print("Sucessfull login")


def print_warning_message():
    print("Warning you dont have enougn age to be here please visit www.cartoonnetwork.com")

age = int(input())
print(check_user_age(age))



print(print_user_message(age))