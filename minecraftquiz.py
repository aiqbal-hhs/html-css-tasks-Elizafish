score = 0

print("""This is a 13 question long quiz on random facts about minecraft. Type either A, B, C, or D.
Good Luck""")

question_one = input("""Who created minecraft?
A. Markus Persson,
B. Notch Hannover,
C. Alex Berg,
D. Steve Andersson
""")
question1 = question_one.title()
if question1 == "A":
    print("""
That is correct
""")
    score += 1
else:
    print("""
That is incorrect, the correct answer was A.
""")

question_two = input("""When was Minecraft’s initial release date: 
A. 15 September 2011
B. 18  November 2011
C. 19 February 2012
D. 12 January 2012
""")
question2 = question_two.title()
if question2 == "B":
    print("""
That is correct
""")
    score += 1
else:
    print("""
That is incorrect, the correct answer was B.
""")
  
question_three = input("""Where was Minecraft designed: 
A. Halmstad
B. Falun
C. Stockholm
D. Trelleborg
""")
question3 = question_three.title()
if question3 == "C":
    print("""
That is correct
""")
    score += 1
else:
    print("""
That is incorrect, the correct answer was C.
""")

question_four = input("""Who owns minecraft
A. Mojang
B. Epic Gaming
C. Google
D. Microsoft
""")
question4 = question_four.title()
if question4 == "D":
    print("""
That is correct
""")
    score += 1
else:
    print("""
That is incorrect, the correct answer was D.
""")

question_five = input("""How much did minecraft sell for:
A. 3 Billion
B. 1.7 Billion
C. 2.1 Billion
D. 2.5 Billion
""")
question5 = question_five.title()
if question5 == "D":
    print("""
That is correct
""")
    score += 1
else:
    print("""
That is incorrect, the correct answer was D.
""")

question_six = input("""How many music discs are there in minecraft:
A. 12
B. 10
C. 13
D. 15
""")
question6 = question_six.title()
if question6 == "C":
    print("""
That is correct
""")
    score += 1
else:
    print("""
That is incorrect, the correct answer was C.
""")

question_seven = input("""True or false creepers were originally a coding error
True
False
""")
question7 = question_seven.title()
if question7 == "True":
    print("""
That is correct
""")
    score += 1
else:
    print("""
That is incorrect
""")

question_eight = input("""True or false was minecraft the first name:
True
False
""")
question8 = question_eight.title()
if question8 == "False":
    print("""
That is correct
""")
    score += 1
else:
    print("""
That is incorrect
""")

question_nine = input("""What was the original name for minecraft:
A. Cave game
B. Mining & Crafting
C. Exploring & Caving
D. Craft game
""")
question9 = question_nine.title()
if question9 == "A":
    print("""
That is correct
""")
    score += 1
else:
    print("""
That is incorrect, the correct answer was A.
""")

question_ten = input("""How long did it take to design the first version of minecraft
7 days
6 days
9 days
4 days
""")
question10 = question_ten.title()
if question10 == "B":
    print("""
That is correct
""")
    score += 1
else:
    print("""
That is incorrect, the correct answer B.
""")
    
question_eleven = input("""What is the rainbow sheep name
A. James
B. Jeremiah
C. Jeb
D. Julian
""")
question11 = question_eleven.title()
if question11 == "C":
    print("""
That is correct
""")
    score += 1
else:
    print("""
That is incorrect, the correct answer was C.
""")

question_twelve = input("""What is the upside down dogs name:
A. Maximus
B. Achilles
C. Dinner bone
D. Doggy food
""")
question12 = question_twelve.title()
if question12 == "C":
    print("""
That is correct
""")
    score += 1
else:
    print("""
That is incorrect, the correct answer was C.
""")

question_thirteen = input("""What is the name commonly used for the creator of minecraft:
A. Mark
B. Miney
C. God of minecraft
D. Notch
""")
question13 = question_thirteen.title()
if question13 == "D":
    print("""
That is correct
""")
    score += 1
else:
    print("""
That is incorrect, the correct answer was D.
""")

print("""
You scored {} points out of 13, congratulations!""".format(score))
