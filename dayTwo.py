def shortest_word(string):
    shortest_word = min(string.split(), key=len)
    return shortest_word


# print(shortest_word("don't think that word means what you think it means"))


def sum_of_minimums(list):
    sum = 0
    for i in range(len(list)):
        sum += min(list[i])
    return sum


my_list = [
    [1, 2, 3, 4, 5],
    [5, 6, 7, 8, 9],
    [20, 21, 34, 56, 100]
]

# print(sum_of_minimums(my_list))
# should return 26


def split_strings(s):
    if len(s) % 2 != 0:
        s += '_'
    return [s[i:i+2] for i in range(0, len(s), 2)]


print(split_strings('abc'))
# should return ['ab', 'c_']

print(split_strings('abcdef'))
# should return ['ab', 'cd', 'ef']
