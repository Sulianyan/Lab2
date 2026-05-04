def calculate_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height*height)
    print("bmi is " + str(bmi))
    if (bmi < 18.5):
        print("Underweight")
        return -1
    elif (bmi >= 18.5 and bmi < 25):
        print("Normal weight")
        return 0
    elif (bmi >= 25 and bmi < 30):
        print("Overweight")
        return 1
    else:
        print("Obese")
calculate_bmi(weight = 60, height = 1.75)