import math
import csv

#opening the csv file 
with open("data.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

#converting it into a list
data = file_data[0]

# Writing a function to find the mean of the given data
def mean(number):
    number_of_elements = len(number)
    total_value = 0
    
    for i in number:
        total_value = total_value + int(i)
    
    mean = total_value / number_of_elements
    return mean

# Subtracting the mean from all the values and squaring them
sqaured_root = []

for number in data:
    x = int(number) - mean(data)
    x = x**2
    sqaured_root.append(x)

# Getting the sum of all the elements from the squared list
sum_of_numbers = 0
for element in sqaured_root:
    sum_of_numbers = sum_of_numbers + element

# Dividing the sum by the number of values in the dataset
result  = sum_of_numbers / (len(data) - 1)

# Getting the square root of the result
std_deviation = math.sqrt(result)
print("The standard deviation of the data is ", std_deviation)