number= int(input("Enter a possitive number=> "))

count=1

while count <= number:
    if count % 3 ==0:
        print(count, "is divisible by 3")
    else:
        print (count, "is not divisible by 3")

    count = count +1 
print("Finished")