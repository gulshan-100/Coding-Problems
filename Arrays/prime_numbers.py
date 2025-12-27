def prime_numbers(number):
    result = []
    for i in range(2, number + 1):
        count = 0 
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 2:
            result.append(i)
    return result

num = 50
primes = prime_numbers(num)
print(primes)