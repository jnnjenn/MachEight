import sys

# Function to find the couples in a list of numbers that sum up a target number
def app(numbers, target):
    listCouples = []

    for i in range(len(numbers)):
        # loop through all the numbers following the current number
        for j in range(i+1, len(numbers)):
            # check if the sum of the current and the following number is equal to the target sum
            if numbers[i] + numbers[j] == target:
                # if it is, append a tuple of the current and following number to the list of pairs
                listCouples.append((numbers[i], numbers[j]))
    
    return listCouples

# get the first and second command line arguments and store them as strings
param1 = sys.argv[1]
param2 = sys.argv[2]

# split the first argument on the comma and convert each number to an integer
# store the resulting list in a variable called list_of_numbers 
lista_de_numeros = [int(numero) for numero in param1.split(',')]
total_sum = int(param2)

result = app(lista_de_numeros, total_sum)
print(result)