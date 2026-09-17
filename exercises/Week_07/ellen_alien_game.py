class Alien:
    health = 3
    total_aliens_created = 0

    def __init__(self, xcordinate, ycordinate):
        self.xcordinate = xcordinate
        self.ycordinate = ycordinate
        self.health = 3
        """
        
        """
        Alien.total_aliens_created += 1
        """
        total_aliens_created should belong to the Alien class, because we're counting every Alien ever created.
        so it should not be self.total_aliens_created
        """

    def hit(self):
        self.health -= 1

    def is_alive(self):
        if self.health == 0:
            return False
        return True

    def teleport(self, new_xcordinate, new_ycordinate):
        self.xcordinate = new_xcordinate
        self.ycordinate = new_ycordinate

    def collision_detection(self, other):
        pass

def new_aliens_collection(positions):
    aliens = []
    for position in positions:
        alien_object = Alien(position[0], position[1])
        aliens.append(alien_object)
    return aliens


def main():
    alien = Alien(2,0)

    xvalue = alien.xcordinate
    """
    xvalue = alien.x_coordinate
    xvalue will return the method object because we created x_coordinate method
    we dont need this we can directly call the value if method is not there

    so we removed the method and replace xvalue with direct variable
    """
    print(xvalue)

    yvalue = alien.ycordinate
    print(yvalue)

    health = alien.health
    print(health)

    life_left = alien.hit()
    print(alien.health)

    Alien_alive = alien.is_alive()
    print(Alien_alive)

    alien_teleport = alien.teleport(5,-4)
    new_xvalue = alien.xcordinate
    print(new_xvalue)
    
    new_yvalue = alien.ycordinate
    print(new_yvalue)

    Alien(5, 1)
    alien_three = Alien(3, 0)
    alien_no = alien_three.total_aliens_created
    print(alien_no)

    alien_start_positions = [(4, 7), (-1, 0)]
    aliens = new_aliens_collection(alien_start_positions)

    for alien in aliens:
        print(alien.xcordinate, alien.ycordinate)


main()