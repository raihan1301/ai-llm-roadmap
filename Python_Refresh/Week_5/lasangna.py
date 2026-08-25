EXPECTED_BAKE_TIME = 40

def bake_time_remaining(time_spend):
    remaining_time = EXPECTED_BAKE_TIME - time_spend
    return remaining_time

def preparation_time_in_minutes(no_layers):
    # each layers takes 2 minutes to prepare

    total_time = no_layers * 2
    return total_time

def elapsed_time_in_minutes(no_layers, elapsed_bake_time):
    """
    elapsed_bake_time = the number of minutes the lasagna has spent baking in the oven already
    no_layers = the number of layers added to the lasagna
    """

    # now for no of layers how much time it takes we have to call prep function
    prep_time = preparation_time_in_minutes(no_layers)
    elapse_time = prep_time + elapsed_bake_time
    return elapse_time

    """
    Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
    """

def main():
    layers = int(input("enter no of layers: "))
    elapse_time = float(input("enter the time in minutes, how long lasagna is been baking: "))

    prep_time = preparation_time_in_minutes(layers)
    print(f"it took {prep_time} minutes for preparation of {layers} layers")

    time_done = elapsed_time_in_minutes(layers, elapse_time)
    remaining_time = bake_time_remaining(time_done)

    print(f"It will take {remaining_time} to complete the baking of lasagna")

if __name__ == "__main__":
    main()