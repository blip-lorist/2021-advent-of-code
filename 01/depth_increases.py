def count_increases(depths):
    increases = 0
    for i, depth in enumerate(depths):
        if i != 0 and depth > depths[i-1]:
            increases += 1

    return increases

