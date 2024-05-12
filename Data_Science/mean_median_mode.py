import numpy as np
from scipy import stats

numbers = [7,5,11,4,7,8,2]

mean = np.mean(numbers)
median = np.median(numbers)
mode = stats.mode(numbers)
std = np.std(numbers)
var = np.var(numbers)

print("Mean = ",mean)
print("Median = ",median)
print("Mode = ",mode)
print("Standard Deviation = ",std)
print("Variance = ",var)