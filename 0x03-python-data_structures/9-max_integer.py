def max_integer(my_list=[]):
    if not len(my_list):
        return None
    max_i = my_list[0]
    for x in my_list[1:]:
        if x > max_i:
            max_i = x
    return max_i
