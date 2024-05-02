def count_occurrences(lst):
    a = {}
    for item in lst:
        i = 0
        for num in lst:
            if item == num:
                count += 1
        if item not in a:
            a[item] = count
    return a

my_list = input()
n = count_occurrences(my_list)
print(n)

