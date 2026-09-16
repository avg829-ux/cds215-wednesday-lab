number= int(input("Enter a positive number=> "))

count=1

while count <= number*5:
    if count % 2 ==0:
        print(count, "is even")
    else:
        print (count, "is odd number")

    count = count +1 
print("Finished")
