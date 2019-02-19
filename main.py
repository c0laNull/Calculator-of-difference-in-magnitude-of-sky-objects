def calculator_of_differences_in_brightness(characters, m1, m2):
    dm =m1-.m2
    return round(2.512**dm,characters)
    
m1 = float(input("Input first magnitude: "))
m2 = float(input("Input second magnitude: "))

print("difference in observed star brightness between two stars: "+calculator_of_differences_in_brightness(40, m1, m2))
