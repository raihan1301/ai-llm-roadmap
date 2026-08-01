import argparse

parser = argparse.ArgumentParser(description="meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)  # so if its int no need to do anything without n

args = parser.parse_args()

for _ in range(args.n):
    print("meow")

# python argparse.py -h
# python argparse.py --help


#unpack

# coins = [100, 25, 50]
# *coins  ==> this will send the individual value to function
# total(*coins)  

# *coins ==> this is for list to unpack
# **coins  ==> this is for dict to unpack

# *args, **kwargs