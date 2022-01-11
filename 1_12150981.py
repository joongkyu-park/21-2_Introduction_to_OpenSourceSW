#과제 1번_12150981

def isInt(string):
    if string[0] == '-':
        return string[1:].isdigit()

    else:
        return string.isdigit()

print("1. 1번째 n자리 정수 출력")
n1 = ""
while True:
    n1 = input("n자리 정수를 입력하세요: ")
    if isInt(n1):
        break
print("2. 2번째 n자리 정수 출력")
n2 = ""
while True:
    n2 = input("n자리 정수를 입력하세요: ")
    if isInt(n2):
        break
print("3. 곱셈 결과 출력")

a = int(n1)
b = int(n2)
c = a*b
maxLen = max(len(str(c)), 1+len(n2),len(n1))

print(" "*(maxLen-len(n1)),a,sep="")
print("X"," "*(maxLen-len(n2)-1),b,sep="")
print("-"*(maxLen))

for i in range(1,len(str(abs(b)))+1):
    tmp = abs(a) * (int(str(b)[len(str(b))-i]) % (i * 10))
    print(" "*(maxLen-(i-1)-len(str(tmp))),end="")
    print(tmp,end="")
    print(" "*(i-1))

print("-"*(maxLen))

if len(str(c)) > 1+len(n2):
    print(c)
else:
    print(" "*(maxLen-len(str(c))),end="")
    print(c)
