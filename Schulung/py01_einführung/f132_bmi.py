def BMI(weight, height):
    return weight / height**2


def evaluate_BMI(bmi):
    if bmi < 16:
        return "Starkes Untergewicht"
    elif bmi < 17:
        return "Mäßiges Untergewicht"
    elif bmi < 18.5:
        return "Leichtes Untergewicht"    
    elif bmi < 25:
        return "Normalgewicht"    
    elif bmi < 30:
        return "Übergewicht" 
    elif bmi < 35:
        return "Adipositas Grad I" 
    elif bmi < 40:
        return "Adipositas Grad II" 
    else:
        return "Adipositas Grad III" 
 
    
w = input("Gewicht: ")
w = float(w)    
h = float(input("Größe: "))

bmi = BMI(w,h)
print("BMI: {0:.2f}".format(bmi)) 
evaluate_BMI(bmi)   