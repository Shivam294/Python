def palindrome(string):
    # y = string.split('')
    # print(y)
    # if(str(y).join([])==string):
    #     return True
    # else:
    #     return False
    if string == string[::-1]:
        return True
    else:
        return False

string = str(input("Enter your string: "))
print(palindrome(string))