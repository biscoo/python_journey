# ----------------------------
# Reeborg's World - Hurdle 4 Solution
# ----------------------------

# Define turn_right() using three left turns
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Define jump() to move around a wall/hurdle
def jump():
    turn_right()
    move()
    turn_right()
    move()

# Main loop: keep running until Reeborg reaches the goal
while not at_goal():
    
    # Case 1: There is a wall in front
    if wall_in_front():
        if wall_on_right():
            # If there's also a wall on the right, turn left
            turn_left()
        else:
            # Otherwise, jump over the hurdle
            jump()
    
    # Case 2: No wall in front, but right side is clear
    elif right_is_clear():
        jump()
    
    # Case 3: Keep moving forward while the right side is blocked
    while wall_on_right():
        if at_goal():  # Exit loop if Reeborg reached the goal
            break
        if front_is_clear():
            move()      # Move forward if the path is clear
        else:
            turn_left() # Turn left if blocked
