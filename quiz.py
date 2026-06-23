print("Welcome to the quiz ")
# Question 1
print("\n1. What is the capital of New Zealand?")
print("1) Auckland")
print("2) Wellington")
print("3) Christchurch")
print("4) Hamilton")

while True:
    ans1 = input("Your answer (1-4): ").strip()
    if ans1 in ["1", "2", "3", "4"]:
        break
    print("Invalid! Please enter 1-4 only.")

if ans1 == "2":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The answer is 2.")

# Question 2
print("\n2. Which animal is native to NZ?")
print("1) Kiwi")
print("2) Tiger")
print("3) Elephant")
print("4) Dog")

while True:
    ans2 = input("Your answer (1-4): ").strip()
    if ans2 in ["1", "2", "3", "4"]:
        break
    print("Invalid! Please enter 1-4 only.")

if ans2 == "1":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The answer is 1.")

# Question 3
print("\n3. What colour is a kiwi fruit inside?")
print("1) Red")
print("2) Green")
print("3) Blue")
print("4) Black")

while True:
    ans3 = input("Your answer (1-4): ").strip()
    if ans3 in ["1", "2", "3", "4"]:
        break
    print("Invalid! Please enter 1-4 only.")

if ans3 == "2":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The answer is 2.")

# Question 4
print("\n6. How many days in a week?")
print("1) 5")
print("2) 7")
print("3) 10")
print("4) 30")

while True:
    ans6 = input("Your answer (1-4): ").strip()
    if ans6 == "2":
        print("Correct!")
        score += 1
        break
    elif ans6 in ["1","3","4"]:
        print("Wrong! Try again.")
    else:
        print("Please enter 1-4 only!")
 # Question 5
print("\n5. What colour is the sun?")
print("1) Yellow")
print("2) Blue")
print("3) Green")
print("4) Black")

while True:
    ans5 = input("Your answer (1-4): ").strip()
    if ans5 == "1":
        print("Correct!")
        score += 1
        break
    elif ans5 in ["2","3","4"]:
        print("Wrong! Try again.")
    else:
        print("Please enter 1-4 only!")
    
# Final Score
print("\nQuiz finished!")
print(f"Your final score: {score}/3")
print("Well done!")