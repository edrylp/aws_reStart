whole_number = 2
prime_numbers = []

# iterate through numbers 1 to 50
while whole_number <= 250:
    is_prime = True

    # check if whole number is divisible by any number between 2 and itself - 1
    for i in range(2, whole_number):
        if whole_number % i == 0:
            is_prime = False
            break

    if is_prime:
        prime_numbers.append(str(whole_number))

    whole_number += 1

result = ", ".join(prime_numbers)
print(result)