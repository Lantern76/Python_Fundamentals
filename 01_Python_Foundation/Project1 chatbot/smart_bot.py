import random

polite_response = ["Cool choice!", "Interesting!", "Never heard of that one!"]

good_colors = ["blue", "green", "purple"]

while True:
    user_color = input("What is your favorite color? ").lower()

    if user_color == "quit":
        break

    if user_color in good_colors:
        print("Mine Too!")
    else:
        print(random.choice(polite_response))
