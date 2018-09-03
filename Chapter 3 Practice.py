a: int = 6
b: int = 8
c: int = 5
print (a > c)
print (c == b)
print (b != a)
print (c <= a)
#3.2
age = int (input ("How old are you? "))
if age >= 18:
    print("You are old enough to vote.")
else:
    print ("You are not old enough to vote")
#3.3
password = input("Enter the password: ")
if password == "narwhals":
    print ("That is correct.")
else:
    print ("That is not correct.")
#3.4
number = int(input("Pick a number between 1 and 5: "))
if number == 1:
    print ("I")
elif number == 2:
    print ("II")
elif number == 3:
    print ("III")
elif number == 4:
    print ("IV")
elif number == 5:
    print ("V")
else:
    print ("That is not a valid number")
#3.5
customer_age = int(input("How old is the customer?  "))
if customer_age >=62:
    cost = 9.89
elif customer_age >=12 and customer_age <=61:
    cost = 12.89
elif customer_age <=12 and customer_age >=4:
    cost = 0.99 * customer_age
else:
    cost = 0.00
print ("Your cost for a customer who is " + str(customer_age) + " years old")
print ("is $" + format(cost, ",.2f"))
#3.5.2
d = 10
e = 10
f = 12
d and e
d == e or d == f
not d == f
#3.6
tired = True
hungry = False
if tired == True and hungry == False:
    print ("Eyes closed")
else:
    print ("Eyes open")
