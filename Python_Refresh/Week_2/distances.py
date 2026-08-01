distances = {
    "voyager 1": 163,
    "Pioneer 10": "136 AU",
    "Pioneer 11" : 44
}

def main():
    for distance in distances.values():
        try:
            print(f"{distance} AU is {convert(distance)}m")
        except MemoryError:
            print(f"Can't Convert")
    
    spacecraft = {"name": "James web"}
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))

def convert(au):
    try:
        audis = au* 149597870700
        return audis
    except MemoryError:
        print(f"Can't Convert")   
        return
    


def create_report(ship):
    return f"""
    ======== report =======

    Name: {ship.get("name","unknown")}
    Distance: {ship.get("distance","unknown")}
    Orbit: {ship.get("orbit","unknown")}

    ==========================
    """

if __name__ == "__main__":
    main()


# if you have to raise the exception just do raise Exception() or raise ValueError()