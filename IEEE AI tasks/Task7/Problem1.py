def calculate_probability_distribution(data):
    total_elements = len(data)
    frequency_distribution = {}
    for value in data:
        if value in frequency_distribution:
            frequency_distribution[value] += 1
        else:
            frequency_distribution[value] = 1
    probability_distribution = {}
    for value, frequency in frequency_distribution.items():
        probability_distribution[value] = frequency / total_elements
    
    return probability_distribution
input_data = input("Enter the data values separated by spaces: ")
data = list(map(int, input_data.split()))
output = calculate_probability_distribution(data)
print(output)
