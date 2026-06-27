import is_char
string = input("write a sentence ")
list = []
temp = ""

for i in range(len(string)):
    if i == (len(string) - 1):
        if is_char.is_function(string[i]) == True:
            temp += string[i]
            break
    if is_char.is_function(string[i]) == True:
        temp += string[i]
    elif is_char.is_function(string[i]) == False:
        if string[i + 1] != " ":
            temp += string[i]
            
        

print(list)
print(temp)
