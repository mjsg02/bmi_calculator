

def bmi_calculator():
    # We create two variables, weight and height, and request them by console.
    weight = float(input("How much do you weigh?(kg) \n"))
    height = float(input("How tall are you?(m) \n"))
    # We do the BMI calculation. We use the round function to obtain only two decimal places.
    bmi = round((weight / (height ** 2)), 2)
    # We save the imc result in a variable
    result = "Your bmi is: " + str(bmi)
    # We do an if loop to get the classification
    if bmi < 18.5:
        return result + " (underweight)"
    elif 18.5 <= bmi < 25:
        return  result + " (normal weight)"
    elif 25 <= bmi < 30:
        return result + " (above normal weight)"
    else:
        return result + " (overweight)"


print(bmi_calculator())