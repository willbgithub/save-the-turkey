# Save the Turkey 🦃
# SBiC GBM: Thanksgiving Code Along (STARTER)
# Fill in the code under each comment! Delete each "pass" once you write that function.

# Import the random module so we can roll random numbers
import random

# Create a variable called STARTING_LIVES and set it to 3
STARTING_LIVES = 3

# The story is already written for you!
# Each scene has a description and two choices.
# Each choice has a chance of success (0.0 to 1.0) and a message for each outcome.
scenes = [
    {
        "description": "It's the night before Thanksgiving. You hear Farmer Fred sharpening the carving knife...",
        "choices": [
            {"text": "Hide in the haystack", "chance": 0.7,
             "success": "Fred walks right past you. Smooth.",
             "fail": "You sneeze. Hay fever. Fred spots you and you barely get away!",
             "death": "You are deathly allergic to hay. You die on the spot."},
            {"text": "Make a run for the barn door", "chance": 0.5,
             "success": "You waddle out the door at top speed!",
             "fail": "The door is locked and you bonk your beak. Ouch!",
             "death": "You are deathly allergic to doors. You die on the spot."},
        ],
    },
    {
        "description": "You made it outside, but there's a tall fence around the whole farm.",
        "choices": [
            {"text": "Dig under the fence", "chance": 0.6,
             "success": "You dig like never before and squeeze right through!",
             "fail": "You hit a rock. Your claws are sore, but you eventually wiggle under.",
             "death": "You find a patch of uranium. You are deathly allergic to uranium. You die on the spot."},
            {"text": "Try to fly over it", "chance": 0.4,
             "success": "Turns out turkeys CAN fly (a little)! You clear the fence!",
             "fail": "Turkeys... can't really fly. You faceplant into the mud.",
             "death": "You fall and snap your neck. You die on the spot."},
        ],
    },
    {
        "description": "You reach a busy road. A pumpkin truck is parked nearby.",
        "choices": [
            {"text": "Hop in the back of the pumpkin truck", "chance": 0.6,
             "success": "You blend right in with the pumpkins and ride into town!",
             "fail": "The truck hits a pothole and you go flying out the back!",
             "death": "The truck runs you over. You die on the spot."},
            {"text": "Cut through the cornfield", "chance": 0.7,
             "success": "The corn is tall enough to hide you completely.",
             "fail": "You get stuck in a corn maze for three hours. Exhausting.",
             "death": "You are deathly allergic to corn. You die on the spot."},
        ],
    },
    {
        "description": "A neighborhood dog spots you and starts barking!",
        "choices": [
            {"text": "Distract it with cranberry sauce", "chance": 0.6,
             "success": "The dog forgets you exist. Cranberry sauce wins again.",
             "fail": "The dog eats the sauce AND keeps chasing you!",
             "death": "You are deathly allergic to cranberry sauce. You die on the spot."},
            {"text": "Play dead", "chance": 0.5,
             "success": "The dog sniffs you, gets bored, and walks away.",
             "fail": "The dog thinks it's a game and drags you around the yard!",
             "death": "You are so good at playing dead that you become dead. You die on the spot."},
        ],
    },
    {
        "description": "You made it to town, but every house is cooking Thanksgiving dinner. You need a disguise!",
        "choices": [
            {"text": "Disguise yourself as a ham", "chance": 0.5,
             "success": "Nobody suspects a thing. You are now a ham.",
             "fail": "A family almost puts you in the oven. You escape, but it was close!",
             "death": "You are deathly allergic to ham. You die on the spot."},
            {"text": "Join the Thanksgiving parade", "chance": 0.6,
             "success": "You march in the parade and everyone thinks you're a costume!",
             "fail": "A kid points and yells 'REAL TURKEY!' You flee the parade.",
             "death": "You are deathly allergic to Thanksgiving parades. You die on the spot."},
        ],
    },
]


def show_lives(lives):
    # Make a string of hearts, one for each life (hint: you can multiply a string by a number!)
    msg = "Lives: "    
    # Print the hearts and the number of lives, like "Lives: ❤️ ❤️ ❤️ (3)"
    i = 0
    while (i < lives):
        i += 1
        msg += "❤️  "
    msg += f"({lives})"
    print(msg)


def get_choice(choices):
    # Loop through the choices with enumerate (start counting at 1)
    for i, choice in enumerate(choices):
        # Print the number and the choice's text, like "  1. Hide in the haystack"
        print(f"{i+1}. {choice["text"]}")

    # Write a while True loop so we keep asking until we get a valid answer
    while True:
        # Use input() to ask the room for 1 or 2, and .strip() off extra spaces
        choice = input("Enter 1 or 2: ")
        # If the answer is "1" or "2"...
        if (choice == "1" or choice == "2"):
            # Return the matching choice from the list (lists start at 0, so subtract 1!)
            return choices[int(choice)-1]
        # Otherwise, print a message telling them to pick 1 or 2
        print("Invalid choice!")
        



def play_scene(scene, lives):
    # Print a blank line, then print the scene's description
    print(f"\n{scene["description"]}")

    # Call get_choice() with this scene's choices and save the result in a variable
    choice = get_choice(scene["choices"])

    # Use random.random() to roll a number between 0 and 1 and save it in a variable
    randomVal = random.random()

    # If the roll is less than the choice's chance, it worked...
    if (randomVal < choice["chance"]):
        # Print a ✅ and the choice's success message
        print(f"✅ {choice["success"]}")

    # Otherwise, it failed...
    else:
        # Take away one life
        lives -= 1
        # Print a ❌ and the choice's fail message
        if (lives > 0):
            print(f"❌ {choice["fail"]}")
        else:
            print(f"❌ {choice["death"]}")

        

    # Call show_lives() to show the updated lives
    show_lives(lives)

    # Return the updated lives
    return lives


def main():
    # Print the title of the game and a one-line intro
    print("Save the Turkey")
    print("Help the turkey escape before Thanksgiving dinner!")

    # Create a lives variable and set it to STARTING_LIVES
    lives = STARTING_LIVES

    # Call show_lives() to show the starting lives
    show_lives(lives)

    # Write a for loop that goes through every scene in scenes
    for scene in scenes:
        # Call play_scene() and save the result back into lives
        lives = play_scene(scene, lives)

        # If lives is 0 or less, break out of the loop early
        if (lives <= 0):
            break



    # Print a blank line before the ending
    print("")

    # If the turkey still has more than 0 lives...
    if (lives > 0):
        # Print a win message that says how many lives are left
        print(f"You win! You have {lives} lives remaining.")

    # Otherwise...
    else:
        # Print a lose message (the turkey is dinner!)
        print("You lose!")

# Call main() to start the game
main()