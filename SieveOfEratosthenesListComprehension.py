'''Enter a number n to get a list of prime numbers up to n
*Uses the Sieve of Eratosthenes algorithm implemented by list comprehension'''

n = int(input('Enter highest number: '))

complist = {eggs for spam in range(2, n) for eggs in range(spam*spam, n, spam)} #Set to avoid duplicates

primelist = [spam for spam in range (2, n) if spam not in complist]

print (primelist)
