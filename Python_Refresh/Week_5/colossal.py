"""
There are two queues for this ride, each represented as a list:
Normal Queue
Express Queue (also known as the Fast-track) - where people pay extra for priority access.
You have been asked to write some code to better manage the guests at the park.

"""

def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """
    Define the add_me_to_the_queue() function that takes 4 parameters <express_queue>, <normal_queue>, <ticket_type>, <person_name> 
    and returns the appropriate queue updated with the person's name.

    <ticket_type> is an int with 1 == express_queue and 0 == normal_queue.
    <person_name> is the name (as a str) of the person to be added to the respective queue.
    """

    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    normal_queue.append(person_name)
    return normal_queue

def find_my_friend(queue, friend_name):
    """
    Define the find_my_friend() function that takes 2 parameters queue and friend_name and returns the position in the queue of the person's name.

    <queue> is the list of people standing in the queue.
    <friend_name> is the name of the friend whose index (place in the queue) you need to find.

    Remember: Indexing starts at 0 from the left, and -1 from the right.
    """
    if friend_name in queue:
        return queue.index(friend_name)

def add_me_with_my_friends(queue, index, person_name):
    """
    Define the add_me_with_my_friends() function that takes 3 parameters queue, index, and person_name.

    <queue> is the list of people standing in the queue.
    <index> is the position at which the new person should be added.
    <person_name> is the name of the person to add at the index position.
    
    Return the queue updated with the late arrivals name.
    """
    # Insert "Bucky" at index 1
    queue.insert(index, person_name)
    return queue

def remove_the_mean_person(queue, person_name):
    """
    Define the remove_the_mean_person() function that takes 2 parameters queue and person_name.

    <queue> is the list of people standing in the queue.
    <person_name> is the name of the person that needs to be kicked out.
    """
    queue.remove(person_name)
    return queue

def how_many_namefellows(queue, person_name):
    """
    Define the how_many_namefellows() function that takes 2 parameters queue and person_name.

    <queue> is the list of people standing in the queue.
    <person_name> is the name you think might occur more than once in the queue.
    """

    """
    we can do this line as well instead of below code
    return queue.count(person_name)
    """
    count = 0
    for name in queue:
        if person_name == name:
            count += 1

    return count

def remove_the_last_person(queue):
    """
    You will have to define the function remove_the_last_person() that takes 1 parameter queue, 
    which is the list of people standing in the queue.

    You should update the list and also return the name of the person who was removed, so you can write them a voucher.
    """

    remove_name = queue.pop(-1)
    """
    we can also do del queue[-1]
    we can also do pop()
    we cannot do .remove() because remove needs value not index
    """
    return queue , remove_name

def sorted_names(queue):
    """
    Define the sorted_names() function that takes 1 argument, queue, 
    (the list of people standing in the queue), and returns a sorted copy of the list.
    """
    return sorted(queue)

def main():
    result1 = add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=1, person_name="RichieRich")
    print(result1)

    result2 = find_my_friend(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], friend_name="Steve")
    print(result2)

    result3 = add_me_with_my_friends(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], index=1, person_name="Bucky")
    print(result3)

    result4 = remove_the_mean_person(queue=["Natasha", "Steve", "Eltran", "Wanda", "Rocket"], person_name="Eltran")
    print(result4)

    result5 = how_many_namefellows(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"], person_name="Natasha")
    print(result5)

    result6, result6_1 = remove_the_last_person(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"])
    print(result6, result6_1)

    result7 = sorted_names(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"])
    print(result7)

main()