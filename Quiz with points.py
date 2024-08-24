list1= "Each question has 10 points", "If the player answers correctly, 10 points are rewarded", "If the player answers incorrectly, 0 points are awarded", " The player can only see the score at the end of the quiz"
print("welcome to the space quest")
ans0 = input("do you want the rulebook? = ")
if(ans0 == 'yes'):
       print(list1)
elif(ans0 == 'no'):
       print("you may proceed")

ans1 = input("Are you ready to start? = ")
if (ans1 == 'yes'):
       print("lets start then")
elif(ans1 == 'no'):
       print("hardluck then, anyways, here's the first question")

ans = input("What is at the center of the Milky Way galaxy? = ")
if (ans == 'black hole'):
        print('your answer is correct')
        print("+10 points")
        points1 = +10
        
else:
       print("your answer is wrong")
       print("wrong, the correct answer is 'black hole'")
       print("0 points")
       points1 = +0

ans = input("Excluding the sun, which is the closest star to Earth? = ")
if (ans == 'alpha centauri'):
        print('your answer is correct')
        print("+10 points")
        points2 = points1 + 10
        
else:
       print("your answer is wrong")
       print("wrong, the correct answer is 'alpha centauri'")
       print("0 points")
       points2 = points1 + 0

ans = input("What is the name of the first spacecraft to bring astronauts to the moon? = ")
if (ans == 'apollo 11'):
       print("your answer is correct")
       print ("+10 points")
       points3 = points2 + 10

else:
       print("your answer is wrong")
       print("wrong, the correct answer is 'apollo 11'")
       print("0 points")
       points3 = points2 + 0 

ans = input("what is the name of your university = ")
if (ans == 'atlas'):
       print("your answer is correct")
       print ("+10 points")
       points4 = points3 + 10

else:
       print("your answer is wrong")
       print("bruh how the hell did u get this wrong, you dummy, the correct answer is 'atlas'")
       print("0 points")
       points4 = points3 + 0 

ans = input("what is the name of the first satellite ever launched = ")
if (ans == 'sputnik 1'):
       print("your answer is correct")
       print ("+10 points")
       points5 = points4 + 10

else:
       print("your answer is wrong")
       print("wrong, the correct answer is ' sputnik 1'")
       print("0 points")
       points5 = points4 + 0 

print("You have completed this quiz")
print("here are your points")
print("your score = ", points5)
if (points5 == 30, points5 == 20, points5 == 10, points5 == 0):
       print("Study harder")
elif (points5 == 40):
       print("AMAZING!!!")
elif (points5 == 50):
       print("PERFECTION") 
