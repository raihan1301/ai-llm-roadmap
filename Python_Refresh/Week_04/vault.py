class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    #now we have to define str method to say how you want to print this init method 
    def __str__(self):
        return f"{self.galleons} galleons, {self.sickles} sickles, {self.knuts} knuts"
    
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

# now to add both operator and weasley

# galleons = potter.galleons + weasley.galleons  # same way for sickels and knuts
# total = Vault(galleons, sickles, knuts) # and this will work but we can do by operator overload

# Operator Overload
total = potter + weasley
print(total)