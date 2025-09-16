# ----------------------------
# Reeborg's World - Maze Solution
# ----------------------------

# Define turn_right() using three left turns
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Main loop: keep running until Reeborg reaches the goal
while not at_goal():
    
    # Follow the left-hand wall until there's space on the right
    while wall_on_right():
        
        # If there is a wall directly ahead, turn left
        while wall_in_front():
            turn_left()
        
        # If the front is clear, move forward
        if front_is_clear():
            move()
        else:
            move()  # This "else" is redundant but kept for original logic
    
    # If the right side becomes clear, take a right turn and move
    if right_is_clear():
        if at_goal():   # Stop if Reeborg has reached the goal
            break
        else:
            turn_right()
            move()
