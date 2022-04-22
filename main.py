# Packages imported from Python libraries
# Pygame library offers gaming elements and modules to use in the program
import pygame

# random offers modules to create random numbers
import random

# time offers modules that can create actions after a certain amount of time has passed
import time

# This initiates the pygame environment and window
pygame.init()

# This sets a variable of 400 and 400 to width and height to use later as width and height in pixels
width, height = 400, 400

# This sets the pygame window height and width by pixels using the above variable
# A variable is also set to the window with its height and width
game_screen = pygame.display.set_mode((width, height))

# This sets the title of the window
pygame.display.set_caption("Snake")

# Variable that sets the initiate location of the snake on the map
x, y = 200, 200

# Variable set to determine how much the snake can move on the x and y axis
# Setting delta_x to 10 means the default movement is away from x axis which is to the right
# This means that when the game starts, the snake will be moving right
delta_x, delta_y = 10, 0

# Creates 2 variables for food on x axis and food on y axis
# random.randrange(0, width) assigns random positioning for width of food and height of food
# //10*10 ensures that food location is always in multiples of 10 to coincide with game and snake sizing and game rules
food_x, food_y = random.randrange(0, width) // 10 * 10, random.randrange(0, height) // 10 * 10

# Variable that creates a list that stores the coordinates of each unit of its body
# This gives the snake the ability to grow in length when it eats food
body_list = [(x, y)]

# Sets a variable for clock to be used in program
# Clock is a module called from the pygame library
# This is used for snake moving speed and countdown timer to end game after end game
clock = pygame.time.Clock()

# Variable set so when game over is called, False means the game continues
# Game is finished when it clashes with its own body
game_over = False

# Calls the font method from pygame and sets font to Arial and font size to 25
font = pygame.font.SysFont("Arial", 25)

# Module to display the snake on the screen
def snake():

    # Variable set so the snake can be updated when moved on the screen
    # Variable made global so they can be used outside of module
    global x, y, food_x, food_y, game_over

    # %width and %height ensures that if the snake moves of the screen, it appears back on the other side
    x = (x + delta_x) % width
    y = (y + delta_y) % height

    # If this if statement changes game_over to true, the game ends by breaking the while loop
    if (x, y) in body_list:
        game_over = True
        return

    # This statement and while loop actually adds to the piece of food to the snake body size, saving into the body list
    # append just allows the code to add it to the body list
    body_list.append((x, y))

    # The if and while loop adds the food to the body and deletes from the screen and adds a new piece of food
    # The food is again added in a random location
    if food_x == x and food_y == y:

        # The food is again added in a random location through the while loop
        while (food_x, food_y) in body_list:
            food_x, food_y = random.randrange(0, width) // 10 * 10, random.randrange(0, height) // 10 * 10

    # Else statement ensures the snake size remain the same until it has eaten more food
    else:
        del body_list[0]

    # Game screen fill ensures that when the snake moves out of a unit, that unit fills back with black
    game_screen.fill((0, 0, 0,))

    # This statement displays the score on the screen in yellow as per RGB
    # The message starts with a string saying your score
    # This is followed with the score which is retrieved from how many pieces have been added to body
    # Body pieces added is retrieved from the body_list list
    gamescore = font.render("Your score: " + str(len(body_list)), True, (255, 255, 0))

    # This statement ensures above is displayed on the game screen and positions the message in top left of window
    game_screen.blit(gamescore, [0, 0])

    # Sets the food pieces as a rectangle on the game screen
    # Sets the colour of the food pieces as red in RGB format
    # Sets the width and height of game pieces to 10 px and 10px
    pygame.draw.rect(game_screen, (255, 0, 0), [food_x, food_y, 10, 10])

    # for loop that gives the snake the ability to grow when it eats food
    # Calls the body_list to remember the size of the snake
    for (i, j) in body_list:

        # Sets the snake as a rectangle on the game screen
        # Sets the colour of the snake as white in RGB format
        # Sets the width and height of starting snake and game pieces to 10 px and 10px
        pygame.draw.rect(game_screen, (255, 255, 255),
                         [i, j, 10, 10])

    # Action to update the snake every time it eats food and is called in the while loop
    pygame.display.update()

# While loop keeps window open until actions to close occur
while True:

    # If statement gives instructions and conditions if game_over variable is changed to true
    if game_over:

        # This statement makes the game over screen fill with black, consistent with in game screen
        game_screen.fill((0, 0, 0))

        # This statement displays the score on the screen in yellow as per RGB
        # The message starts with a string saying you scored
        # This is followed with the score which is retrieved from how many pieces have been added to body
        # Body pieces added is retrieved from the body_list list
        score = font.render("You scored: " + str(len(body_list)), True, (255, 255, 0))

        # This statement ensures above is displayed on the game screen and positions the message in top left of window
        game_screen.blit(score, [0, 0])

        # This statement displays a message saying game over when game_over changed to true
        # Message is displayed for 10 seconds in white as per RGB colours
        msg = font.render("GAME OVER!", True, (255, 255, 255))

        # This statement ensures the above message is displayed on the game screen
        # This statement also tells the program where on the window to display the message
        game_screen.blit(msg, [width // 3, height // 3])

        # This statement ensures score is updated by actual score and message displays
        pygame.display.update()

        # This statement counts down 10 seconds and then performs next action which is close game and window
        time.sleep(10)

        # This closes the pygame environment
        pygame.quit()
        quit()
    events = pygame.event.get()

    # This for loop controls what event occurs depending on action
    for event in events:

        # This closes the pygame environment if the close icon on the window is selected
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # This if statement determines an action when an arrow key is pressed during game
        if event.type == pygame.KEYDOWN:

            # If statement instructs if the left arrow key is selected, the snake will move to the left 10 px
            if event.key == pygame.K_LEFT:

                # ! = 10 if statement added so snake cant go backward to its current position
                # If the snake is moving left, ! = 10 ensures it cant move right if right arrow key is pressed
                if delta_x != 10:

                    # -10 means the snake moves towards the x axis which is towards the left
                    delta_x = -10

                # 0 means no movement is made on the y axis when left is selected
                delta_y = 0

            # If statement instructs if the right arrow key is selected, the snake will move to the right 10 px
            elif event.key == pygame.K_RIGHT:

                # ! = -10 if statement added so snake cant go backward to its current position
                # If the snake is moving right, ! = -10 ensures it cant move left if ledt arrow key is pressed
                if delta_x != -10:

                    # 10 means the snake moves away from the x axis which is towards the right
                    delta_x = 10

                # 0 means no movement is made on the y axis when left is selected
                delta_y = 0

            # # If statement instructs if the up arrow key is selected, the snake will move up 10 px
            elif event.key == pygame.K_UP:

                # 0 means no movement is made on the x axis when up is selected
                delta_x = 0

                # ! = 10 if statement added so snake cant go backward to its current position
                # If the snake is moving up, ! = 10 ensures it cant move down if down arrow key is pressed
                if delta_y != 10:

                    # -10 means the snake moves towards the y axis which is up
                    delta_y = -10

            # If statement instructs if the down arrow key is selected, the snake will move down 10 px
            elif event.key == pygame.K_DOWN:

                # 0 means no movement is made on the x axis when down is selected
                delta_x = 0

                # ! = -10 if statement added so snake cant go backward to its current position
                # If the snake is moving down, ! = -10 ensures it cant move up if up arrow key is pressed
                if delta_y != -10:

                    # 10 means the snake moves away from the y axis which is down
                    delta_y = 10

            # Else statement instruct if no arrow key is currently being pressed, the game should continue
            # Snake should continue moving in the direction it was previously moving
            else:
                continue

            # Calls the snake method after every event so the actions of the snake occur when moves or eats food
            # Also ensures snake is at correct size and moving in correct direction
            snake()

    # This if statement makes the snake move automatically
    # The snake will continue to move in the direction previously selected
    if not events:
        snake()

    # Clock statement determines the speed the snake moves
    clock.tick(10)
