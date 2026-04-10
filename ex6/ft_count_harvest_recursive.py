def call_me(days, day):
    print("Day", day)
    if day in range(days):
        call_me(days, day + 1)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    day = 1
    call_me(days, day)
    print("Harvest time!")
