# Ask the user for information
name = input("What is your name? ")
age = input("How old are you? ")
favorite_food = input("What is your favorite food? ")
favorite_color = input("What is your favorite color? ")

# Create a short story using the information
story = f"""
Once upon a time, there was a person named {name}.
At {age} years old, {name} loved eating {favorite_food} every single day.
One day, wearing their favorite {favorite_color} outfit, {name} went on an amazing adventure!
"""

# Print the story
print(story)

