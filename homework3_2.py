# This programme calculates the are of a rectangle 
# Define length and width of rectangle 
length = float(input('Define length of rectangle: ')) # Define length of rectangle 
width = float(input('Define width of rectangle: ')) # Define width of rectangle 

# Area calculation 
area = length * width 

# Perimeter calculation 
perimeter = 2 * length + width

# Result of area calculation  
print(f'Area of rectangle is {area:.1f}m2')

# Result of perimeter calculation  
print(f'Perimeter of rectangle is {perimeter:.1f}m')