#personal finance manager
print("Welcome to your Personal finance manager")
income = int(input("enter your monthly income in INR = "))
utilities = int(input("enter amount spent on utilities = "))
groceries = int(input("enter amount spent on groceries = "))
ans = (input("do you pay rent = "))

expense = int
if (ans == 'yes'):
    rent = int(input("enter rent amount = "))
    expense = rent + utilities + groceries 

elif (ans == 'no' ):
    expense = utilities + groceries 

print("your expense is = ", expense)
amount_left = income - expense 
print("amount left after expense = ", amount_left)
list = [ '5%', '10%', '20%', '30%', '40%', '50%' ]
ans = input( "do you want to save this month = ")
if (ans == 'yes'):
    print(list)
    ans = (input("how much do you want to save? = "))
    if (ans == '5%'):
        print("your savings = ", 5*amount_left/100 )
    elif (ans == '10%'):
        print("your savings = ", 10*amount_left/100)
    elif(ans == '20%'):
        print("your savings = ", 20*amount_left/100)
    elif(ans == '30%'):
        print("your savings = ", 30*amount_left/100)
    elif(ans == '40%'):
        print("your savings = ", 40*amount_left/100)
    elif(ans == "50%"):
        print("your savings = ", 50*amount_left/100)

if(ans == 'no'):
    print("have a nice day")
