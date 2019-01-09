str1 = "Pesho Gosho Miro Kiro"
print(str)

str1 = str1.replace(" ", "")
print(str1)

#convert num to string
number = int(5)
string_to_int = str(number)
string_num = "10"
int_to_string = int(string_num)
print(int_to_string)
print(string_to_int)

# STRING ARRAYS
string_arr = ["Miro" , "Pesho", "Gosho", "Teo"]
print(string_arr)
#foreach in python
for arr in string_arr:
    print(arr)


#char array
char_arr = ['A' , 'B', 'a', 'b']

for arr in char_arr:
    print(arr + arr.upper() + " " + chr(65))

