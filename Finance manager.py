#personal finance manager
print("Welcome to your Personal finance manager")
def formula(amount_left):
    (20*amount_left/100) 
income = int(input("enter your monthly income in INR = "))
utilities = int(input("enter amount spent on utilities = "))
groceries = int(input("enter amount spent on groceries = "))
ans = (input("do you pay rent = "))

expense = int
if (ans == 'yes'):
    rent = int(input("enter rent amount = "))
    expense = rent + utilities + groceries 

elif (ans == 'no' ):
    rent = 0
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
        savings = 5*amount_left/100
        print("your savings = ", savings)
    elif(ans == '10%'):
        savings = 10*amount_left/100
        print("your savings = ", savings)
    elif(ans == '20%'):
        savings = 20*amount_left/100 
        print("your savings = ", savings)
    elif(ans == '30%'):
        savings = 30*amount_left/100
        print("your savings = ", savings)
    elif(ans == '40%'):
        savings = 40*amount_left/100
        print("your savings = ", savings)
    elif(ans == "50%"):
        savings = 50*amount_left/100
        print("your savings = ", savings)
    print("your summary report = ")
    print("amount spent on groceries = ", groceries)
    print("amount spent on utilities = ", utilities)
    print("amount spent on rent = ", rent)
    print("amount saved = ", savings)
    print("amount left after savings = ", amount_left-savings)
else: 
    savings = 0
    print("your summary report = ")
    print("amount spent on groceries = ", groceries)
    print("amount spent on utilities = ", utilities)
    print("amount spent on rent = ", rent)
    print("amount saved = ", savings)
    print("amount left after savings = ", amount_left-savings)
