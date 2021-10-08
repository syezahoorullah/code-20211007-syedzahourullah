import json
import ijson
from urllib import request

ow_count=0 #counter for overweight    
def opt(person):
    global ow_count
    BMI=(int(person["WeightKg"])/((float(person["HeightCm"])/100)**2))
    if(BMI<18.5):
        pass
        # print("Underweight")
    elif(BMI>=18.5 and BMI<25):
        pass
        # print("Normal weight")
    elif(BMI>=25 and BMI<30):
        pass
        # print("Overweight")
        ow_count+=1
    elif(BMI>=30 and BMI<35):
        pass
        # print("Moderately obese")
    elif(BMI>=35 and BMI<40):
        pass
        # print("Severely obese")
    elif(BMI<=40):
        pass
        # print("Very severely obese")
    

def do_op(loc):
    
    objects = ijson.items(loc,'item')
    for ob in objects:
        opt(ob)
    print("\nThe total overweight people are:",ow_count)

FILENAME='filedata.json'
def with_file(FILENAME):
    try:
       with open(FILENAME) as ff:
            do_op(ff)
    except FileNotFoundError:
        print("An issue occured while processing the file please try again")


def with_url(url):
    
    fu = request.urlopen(url)

    with open('urldata.json', 'w', encoding='utf-8') as f:
        f.write(fu.read().decode('utf-8'))
    with_file('urldata.json')
        
    # do_op(fu.read())
sel_opt=0
while sel_opt!=3:
    try:
        sel_opt = int(input("Through which mode you wish to continue:\n1. Using a file\n2. Using URL\n3. Exit\n"))
    except:
        print("Please provide a valid option")
    if sel_opt==1:
        option=input("The file named data.json needs to be present in the current working directory.\nDo you wish to enter file destination manually. (Y/N)\n")
        if(option=='Y' or option == 'y'):
            FILENAME = ''
            while FILENAME == '':
                FILENAME = input("Please enter the filename along with full path to the JSON file\n")
        with_file(FILENAME)
        break
    elif sel_opt==2:
        with_url(input("Please enter the URL\n"))
        break
