# this function allows us to get a valid input from the user
def get_natural_number_input():
    while True:  # while True will run this function until we get the valid input from the user
        try:  # the try block will probe if what the user inputed will lead to an error or not 
            n = int(input("Enter a natural number: "))
            if n > 0:
                return n
            else: # this is how we handled the error or exception in case n is negative
                print("Please enter a number greater than zero: ")
        except ValueError: #we used a value error keyword to make sure the user does not input strings or other charaters
            print("Invalid input. Please enter a valid natural number ")

# This function returns a Boolean value of True if the number it takes as a parameter is a prime
# and a Boolean value of False if otherwise.
def is_prime(n):
    if n == 2: return True # we separately take the case of n = 2
    if n <= 1 or n % 2 == 0: return False # In case the number is negative or less even 
    for i in range(2, n // 2 + 1): # we search for divisor
        if n % i == 0: return False # if we find them then it is not prime
    return True

# this function take a void list and takes in all the primes found in between 2 and a given
#number such that we will have a list with all the primes that we can then use for operations
def get_prime_numbers(n):
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes


if __name__ == "__main__":
    n = get_natural_number_input()
    prime_list = get_prime_numbers(n)
    for i in range (4, n+1):
        found_pair = False # A flag to help us track down for which numbers the hypothesis doesn't hold
        for prime in prime_list:
            if (i-prime) in prime_list: # If i can be written as a sum of 2 primes, then, i - prime is also prime so it should be in the list
                print(prime, " and ", i - prime, " summed up are", i)
                found_pair = True # A pair was found so we set the flag as True
                break # We break cause we have no reason to search for all the possible cases or to go all the way to where p2 = p1 and vice versa
        if not found_pair: # This if statement runs the block of code in case a certain pair was not found 
            print("No 2 prime numbers found who's sum is ", i)

#This code does not use a range and simply searches if the given number verifies the hypothesis or not.
'''if __name__ == "__main__":
    n = get_natural_number_input()
    prime_list = get_prime_numbers(n)
    found_pair = False
    for prime in prime_list:
        if (n-prime) in prime_list:
            print(prime, " and ", n - prime, " summed up are", n)
            found_pair = True
            break
    if not found_pair:
        print("No 2 prime numbers found who's sum is ", n)'''



#print("the primes are:", get_prime_numbers(n))

