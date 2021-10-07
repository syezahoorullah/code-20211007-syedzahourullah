import json

var = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
"HeightCm": 167, "WeightKg": 82}]

def lets(var):
    people = json.loads(json.dumps(var))

    for person in people:
        BMI=(int(person["WeightKg"])/((float(person["HeightCm"])/100)**2))
        if(BMI<18.5):
            print("Underweight")
        elif(BMI>=18.5 and BMI<25):
            print("Normal weight")
        elif(BMI>=25 and BMI<30):
            print("Overweight")
        elif(BMI>=30 and BMI<35):
            print("Moderately obese")
        elif(BMI>=35 and BMI<40):
            print("Severely obese")
        elif(BMI<=40):
            print("Very severely obese")



lets(var)