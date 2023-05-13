# function of join
def join_demo():
    stations = ("HUA", "SAM", "SIL", "LUM", "KHO", "SIR",
                "SUK", "PET", "RAM", "CUL", "HUI", "SUT",
                "RAT", "LAT", "PHA", "CHA", "KAM", "BAN")
    print(stations)
    print(" -> ".join(stations))
    print(" -> ".join(stations[1:4]))
    print(" -> ".join(stations[1:4][::-1]))

join_demo()