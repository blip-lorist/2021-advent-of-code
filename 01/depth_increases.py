# Part 1
def count_increases(depths):
    increases = 0
    for i, depth in enumerate(depths):
        if i != 0 and depth > depths[i-1]:
            increases += 1

    return increases


# Part 2
def window_sums_list(depths, window_size=3):
    window_sums = []
    for i, depth in enumerate(depths):
        if i != 0 and i != (len(depths) - 1):
            window_sum = depths[i-1] + depth + depths[i+1]
            window_sums.append(window_sum)

    return window_sums

def window_sums_increases(depths):
    window_sums = window_sums_list(depths)
    increases = count_increases(window_sums)
    return increases
