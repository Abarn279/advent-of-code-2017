def is_prime(n):
    return all(n%j for j in range(2, int(n**0.5)+1)) and n>1

b = 79
c = 70

c = b = (b * 100) - (-100000)
c -= -17000

h = 0

for z in range(b, c + 1, 17):
	if not is_prime(z):
		h += 1

print(h)