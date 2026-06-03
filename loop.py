i=0
while(i<=10):
    print(i)
    i+=1

i = 1
while True:
    print(i)
    i += 1
    if not (i <= 10):
        break

fruits=["banana","kera","bhenta"]
for fruit in fruits :
    print(fruit)

for i in range(10):
    if i==5:
       continue
    print(i)    