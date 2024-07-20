import random
print("Welcome to Password Generator")
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cl = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n = ['1','2','3','4','5','6','7','8','9']
s = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|','<','>','?']

cap_let = int(input("How many Capital letters ? \n"))
letters = int(input("How many letters ? \n"))
symbols = int(input("How many symbols ? \n"))
numbers = int(input("How many numbers ? \n"))

password_list = []

for char in range(1,cap_let+1):
  password_list += random.choice(cl)

for char in range(1,letters+1):
  password_list += random.choice(l)

for sym in range(1,symbols+1):
  password_list += random.choice(s)

for num in range(1,numbers+1):
  password_list += random.choice(n)

passw = ''
random.shuffle(password_list)
for p in range(0,len(password_list)):
  passw += password_list[p]

print(f"Generated Password is {passw}")
