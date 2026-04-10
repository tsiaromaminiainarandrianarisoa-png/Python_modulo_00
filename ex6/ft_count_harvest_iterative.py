def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    n = 1
    while n in range(days + 1):
        print("Day", n)
        n = n + 1
    print("Harvest time!")
