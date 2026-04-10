def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type.capitalize()
    units = ("packets", "grams", "area")
    back = (" available", " total", "square meters")
    loc = 0
    front = ""
    res = ""
    while loc < 3:
        if unit == units[loc]:
            res = back[loc]
            if loc == 2:
                front = " covers"
                unit = ""
            break
        loc = loc + 1
    if res == "":
        return (print("Unknown unit type"))
    print(f"{seed} seeds:{front} {quantity} {unit}{res}")
