# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = "*" * n + "\n"
    i = 1
    while i < n - 1:
        result += "*" + (n - 2) * " " + "*" + "\n"
        i += 1
    if n != 1:
            result += "*" * (n) + "\n"

    return result.rstrip()

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    for i in range(1, n + 1):
        for j in range (1, i + 1):
            result += str(j)
        result = result.strip()
        result += "\n"
        
    return result.rstrip() 
# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0
    i = 1           # we do i = 1 because we dont want to include zero... i said IRL that it is the index but im not sure
    while i <= n:
        total += i
        i += 1
    return total
print(sum_of_natural_numbers(5))
# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    pyramid = ""
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        pyramid += spaces + stars + '\n'
    return pyramid.rstrip()
print(centered_star_pyramid(5))