def calculate_area(x, y):
    print(f"Area : {x * y}")

calculate_area()
def repeat_message(message, times):
    for i in range(times):
        print(message)

repeat_message(5, "Hello")
def get_number():
    while True:
        num = input("Give me a number.")
        try:
            num = int(num)
            return
        except:
            print("That's not a number")

num = get_number()
def check_play():
    play = input("Do you want to play again")
    if play.lower() in ["y", "yes"]:
        return True
    else:
        return False

check_play()
