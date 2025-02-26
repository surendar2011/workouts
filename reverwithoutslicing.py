def reverse_for_loop(s):
    s1 = " "

    for c in s:
        s1 = c + s1

    return s1

input = 'hello'
print(reverse_for_loop(input))