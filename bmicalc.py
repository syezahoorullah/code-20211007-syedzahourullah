import ijson

def opt(person):
    
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

def do_op(loc):
    
    objects = ijson.items(loc,'item')
    for ob in objects:
        opt(ob)


FILENAME='data.json'
def with_file(FILENAME):
    
    option=input("The file named data.json needs to be present in the current working directory.\nDo you wish to enter file destination manually. (Y/N)\n")

    if(option=='Y' or option == 'y'):
        FILENAME = ''
        while FILENAME == '':
            FILENAME = input("Please enter the filename along with full path to the JSON file\n")
    try:
       with open(FILENAME) as ff:
            do_op(ff)
    except FileNotFoundError:
        print("An issue occured while processing the file please try again")


with_file(FILENAME)