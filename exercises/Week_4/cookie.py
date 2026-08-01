# great example of using class and property function
class Jar_class:
    def __init__(self, capacity=12):  # if no capcity is provided it will assume 12 and if you provide capcity it will be replaced by that
        self._capacity = capacity  # as soon as init is called capacity value is stored and below size is stored
        self._size = 0
    
    def __str__(self):
        return "🍪" * self._size  # when print is called it will get size value from above

    def deposit(self,n): # this will be called from main function
        if self._size + n > self._capacity:  # size value and capacity value will be getting from init function
            raise ValueError("Jar capacity exceded")
        
        self._size += n  # updating size value and hence it will update it in init function.
    
    def withdraw(self,n): # this will be called from main function
        if n > self._size:  # size value will be getting from init function
            raise ValueError("Not Enough Cookies")
        self._size -= n  # updating size value and hence it will update it in init function.

    @property
    def capacity(self):
        return self._capacity # this will take whatever the capacity value in init

    @property
    def size(self):
        return self._size  # this will take whatever the size value in init
    
def main():
    cookie = int(input("Enter the capacity of cookie jar: "))

    jar = Jar_class(cookie)   # this will automatically calls class __init__ function, so as soon as you created object for class init is called
    print(jar)  # this will call __str__ function from the class to get return statement
    print(jar.size)  # this will call size property
    print(jar.capacity) # this will call capacity property

    cookie_added = int(input("Enter the no of cookie you want to add in Jar : "))
    jar.deposit(cookie_added)  #this will call deposit function from class
    print(jar)
    print(jar.size)
    print(jar.capacity)

    cookie_taken = int(input("Enter the no of cookie you want to take out from Jar : "))
    jar.withdraw(cookie_taken)
    print(jar)
    print(jar.size)
    print(jar.capacity)

if __name__ == "__main__":
    main()


"""
main()
  ↓
Ask capacity
  ↓
Jar_class(capacity)
  ↓
__init__ runs automatically
  ↓
_size starts at 0
  ↓
deposit() increases _size
  ↓
withdraw() decreases _size
  ↓
__str__ displays cookies
  ↓
properties return capacity and size

"""