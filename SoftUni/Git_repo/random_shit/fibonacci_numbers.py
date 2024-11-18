import time
start = time.time()

def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Print first 10 Fibonacci numbers
gen = fibonacci_gen()
for _ in range(1500000):
    next(gen)

# Save timestamp
end = time.time()

print(end - start)