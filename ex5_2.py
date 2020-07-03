largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        number = float(num)
    except:
        print('Invalid Input')
        continue
    if smallest == None:
       smallest = number
    if smallest>= number:
       smallest = number
    if largest == None:
        largest= number
    if largest<= number:
        largest= number

print("Maximum", largest)
print ("Minimum", smallest)
