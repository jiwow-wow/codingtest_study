str = input()

def updown(str):
    if (len(str)>= 1 and len(str) <=20):
        result = ""
        for i in range(len(str)):
            if str[i].isupper():
                result += str[i].lower()
            elif str[i].islower():
                result +=str[i].upper()
    else: 
        print("입력 범위 초과")
        return -1
    return result

print(updown(str))