def f(*args, **kwargs):  #args means take variable number from left to right like a list
    print("Positional:", args) # kwargs means take number of keyword arguments like dictionary
    print("Named:", kwargs)


f(100, 50, 25)
f(galleons=100, sickles=50, knuts=25)