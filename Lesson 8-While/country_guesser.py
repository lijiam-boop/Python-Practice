# =====================================================================
# Task: Country Guessing Game
# =====================================================================

# VALUES
# TODO: Create a variable to store the correct country (e.g., "Italy").
correct_country = "Canada"
# TODO: Create a variable to keep track of the user's current guess. 
#       (Hint: Start it as an empty string "" so the loop runs at least once!)


# LOOP
# TODO: Start a 'while' loop. 
#       The loop should keep running AS LONG AS the user's guess 
#       is NOT EQUAL to the correct country.
while guess != country:
    
    # TODO: Ask the user for their guess and save it to your guess variable.
    #       (Remember: This changes the loop condition so it doesn't run forever!)
    guess = input("What country am I think of?")
    # TODO: (Optional) Add an 'if' statement inside the loop.
    #       If they guessed wrong, print an encouraging message or an extra hint.
    #       If they guessed right, the loop will automatically exit on the next check!


# GAME OVER / WINNING MESSAGE
# TODO: Print a congratulatory message celebrating their win!

# ================================================================
# EXTENSION
# TODO: Add an introduction
# TODO: Add a scoring system (starts at 20, lose 1 point for each wrong guess)
# TODO: Add a lose condition (if score reaches 0)

#==================================================================
# EXPERT
# TODO: Make the game unique (use a list of countries and randomly select one)
# TODO: Add a play again option
count = 0
while count < 5:
    print("Hello!")
    count = count + 1
timer = 3
while timer > 0:
    print("Counting down!")
    timer = timer - 1
    user_input = ""
while user_input != "exit":
    user_input = input()
    print("You said: " + user_input)

