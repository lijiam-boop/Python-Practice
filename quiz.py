def welcome():
    print("Welcome to the quiz ")
score = 0
# Question 1
print("\n1. What is the capital of Australia?")
print("1) Melbourne")
print("2) Canberra")
print("3) Sydney")
print("4) Perth ")

while True:
    ans1 = input("Your answer (1-4): ").strip()
    if ans1 == "2":
        print("Correct!")
        score += 1
        break

    elif ans1 in ["1", "3", "4"]:
        print("Wrong! Try again.")

    else:
        print("Please enter 1-4 only!")

# Question 2
print("\n2. Which animal is native to NZ?")
print("1) Kiwi bird")
print("2) Tiger")
print("3) Elephant")
print("4) Dog")

while True:
    ans2 = input("Your answer (1-4): ").strip()
    if ans2 == "1":
        print("Correct!")
        score += 1
        break

    elif ans2 in ["2", "3", "4"]:
        print("Wrong! Try again.")

    else:
        print("Please enter 1-4 only!")

# Question 3
print("\n3. What colour is a kiwi fruit inside?")
print("1) Red")
print("2) Green")
print("3) Blue")
print("4) Black")

while True:
    ans3 = input("Your answer (1-4): ").strip()
    if ans3 == "2":
        print("Correct!")
        score += 1
        break

    elif ans3 in ["1", "3", "4"]:
        print("Wrong! Try again.")

    else:
        print("Please enter 1-4 only!")

# Question 4
print("\n4. How many days in a week?")
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
print(f"Your final score: {score}/5")
print("Well done!")