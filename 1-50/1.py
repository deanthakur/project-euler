def summing_multiples(multiple_limit):
    sum = 0
    for i in range(multiple_limit):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(summing_multiples(1000))