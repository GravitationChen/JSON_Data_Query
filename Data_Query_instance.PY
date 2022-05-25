#Welcome
def welcome():
    print("""
    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    """
    )
    print("This Program is developed by Boyu Chen on 5 25 2022.")
    print("Version 1.0.0")

#import module on demand
import json

#input data and directory verification
def input_data():
    directory_validity = False
    data = ""
    directory = input("Please type in the directory of the JSON file you want to query, starts from \"/\" or \"./\". Or typing in nothing to query demo_data.json by default->>>")
    if directory == "":
        directory = "demo_data.json"
    else:
        pass
    try:
        data = str(open(directory,mode="r").read())
        directory_validity = True
    except:
        print("No such file or directory!")
    return data, directory_validity

#verify if the json file id format is correct
def json_id_check(data):
    json_id_validity = False
    jsondata = json.loads(data)
    try:
        test = jsondata["id"]["0"]
        json_id_validity = True
    except:
        print("JSON file id failed to pass the test! Terminating script! Please make sure the id starts from 0 and the file follows the rule of data.json")
    return json_id_validity


#parse the json data
def parse_json(data):
    jsondata = json.loads(data)
    input_index = jsondata["id"]["0"].keys()
    input_index_str = str(input_index)
    lenth = len(input_index_str)
    input_index_str = input_index_str[11:lenth-2]
    return jsondata, input_index_str, input_index

#User input start
def user_input(input_index_str):
    b_input = "Please enter the specific property you want to query ({},\'*\') ->>>"
    b_input = b_input.format(input_index_str)
    a = input("Please enter the id of the person you want to query ->>>")
    b = input(b_input)
    return a, b

#Verify if the querying id is valid
def id_check(jsondata,a,input_index_str):
    validity = False
    try:
        test = jsondata["id"][a]
        validity = True
    except:
        print("This is not a valid id")
        user_input(input_index_str)
    return validity

#Verify if the querying property is valid in json data input
def property_check(b,input_index):
    validity = False
    if b in input_index or b == "*":
        validity = True
    else:
        print("This is not a valid property!")
    return validity

#Check for correct pronoun for the person in json data(based on data "sex")
def pronoun_check(jsondata,a):

    if jsondata["id"][a]["sex"].upper() == "FEMALE" or jsondata["id"][a]["sex"].upper() == "MALE_TO_FEMALE":
        gender = "Her"
    elif jsondata["id"][a]["sex"].upper() == "MALE" or jsondata["id"][a]["sex"].upper() == "FEMALE_TO_MALE":
        gender = "His"
    else:
        gender = "Their"
    return gender

#Query
def query(a,b,gender,jsondata):
    if b != "*":
        try:
            rawout = "{} {} is {}."
            jsondata = jsondata["id"][a][b]
            out = rawout.format(gender,b,jsondata)
            print(out)
        except:
            pass
    elif b == "*":
        try:
            jsondata = jsondata["id"][a]
            keys = jsondata.keys()
            print(keys)
            for i in keys:
                rawout = "{} {} is {}."
                n = jsondata[i]
                out = rawout.format(gender,i,n)
                print(out)
        except:
            pass
    else:
        pass

#Define Main Function
def main():
    welcome()
    data, directory_validity = input_data()
    if directory_validity == True:
        json_id_validity = json_id_check(data)
        if json_id_validity != False:
            jsondata, input_index_str, input_index = parse_json(data)
            while True:
                a, b = user_input(input_index_str)
                id_validity = id_check(jsondata,a,input_index_str)
                property_validity = property_check(b,input_index)
                if id_validity == True and property_validity == True:
                    gender = pronoun_check(jsondata,a)
                    query(a,b,gender,jsondata)
                    break
                else:
                    continue
        else:
            pass
    else:
        pass
             
main()
