# This programme does a simple interest calculation 
# User inputs for calculation 
value = float(input('Specify amount to be calculated: ')) # Specifies the amount of money to be calculated 
rate = float(input('Specify the annual interest rate: ')) # Specifies annual interest rate
time = float(input('Specify the amount of years: ')) # Specifies the amount of years the calucaltion will be made over

# Interest rate calculation 
interest = value * rate * time / 100 # Interest rate calculation 

# Calculation of interest
print(f'Interest made:', interest)

# Calculation of the original value plus interest
total = value + interest
print(f'Total amount:', total) # Prints total amount  