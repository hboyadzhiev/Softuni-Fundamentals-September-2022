number = int(input())

prime = True

for x in range(2, number + 1):
    for y in range(2, number + 1):
         if x * y == number:
             prime = False
             break


if number <= 1:
    prime = False

if prime == True:
    print("True")
else:
    print("False")
