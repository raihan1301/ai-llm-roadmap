def eat_ghost(pellet_active , touching_ghost):
    """
    function that takes two parameters (if Pac-Man has a power pellet active and if Pac-Man is touching a ghost) 
    and returns a Boolean value if Pac-Man is able to eat a ghost. 
    The function should return True only if Pac-Man has a power pellet active and is touching a ghost.
    """
    if pellet_active and touching_ghost:
        return True
    return False

def score(power_pellet, dot):
    """
    function that takes two parameters (if Pac-Man is touching a power pellet and if Pac-Man is touching a dot) 
    and returns a Boolean value if Pac-Man scored. 
    The function should return True if Pac-Man is touching a power pellet or a dot.
    """
    if power_pellet or dot:
        return True
    return False

def loose(pellet_active , touching_ghost):
    """
    function that takes two parameters (if Pac-Man has a power pellet active and if Pac-Man is touching a ghost) 
    and returns a Boolean value if Pac-Man loses. 
    The function should return True if Pac-Man is touching a ghost and does not have a power pellet active.
    """
    if touching_ghost and not pellet_active:
        return True
    return False

def win(dots_eaten, pellet_active, touching_ghost):
    """
    function that takes three parameters (if Pac-Man has eaten all of the dots, if Pac-Man has a power pellet active, and if Pac-Man is touching a ghost) 
    and returns a Boolean value if Pac-Man wins. 
    The function should return True if Pac-Man has eaten all of the dots and has not lost based on the rules defined in part 3.
    """
    if dots_eaten and not loose(pellet_active, touching_ghost):
        return True
    return False

def main():
    play1 = eat_ghost(True, True)
    print(f"pacman eat ghosts in play 1 : {play1}")
    play2 = eat_ghost(True, False)
    print(f"pacman eat ghosts in play 2 : {play2}")

    play3 = score(True, False)
    print(f"pacman score in play3 : {play3}")
    play4 = score(False, False)
    print(f"pacman score in play4 : {play4}")

    play5 = win(True, True, True)
    print(f"pacman win in play5 : {play5}")
    play6 = win(True, False, True)
    print(f"pacman win in play6 : {play6}")

main()