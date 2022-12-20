import random

# n = 19416
# samples = 1000
# expected_ones = 4984

n = 85
samples = 100000
expected_ones = 23

# makes a list with each element being the total number of times someone was hospitalized in the n samples, done samples times
all_tests = [sum([random.randint(0,1) for i in range(n)]) for j in range(samples)]

count = 0
left_p = expected_ones
right_p = n-expected_ones
for val in all_tests:
    # check if value percentage is above or below
    if ((val < left_p) or (val > right_p)):
        count += 1
# abs(sample_sizes_ntick[0][1] - sample_sizes_ntick[0][0])
print(count)
print(count/samples)