import json

from matplotlib.font_manager import json_load


#1. Write a Python program to convert JSON data to Python objects.
def exercise1():
    with open('states.json', 'r') as file:
        states_new = json.load(file)
        print(states_new)
#2. Write a Python program to convert Python objects (dictionary) to JSON data.
def exercise2():
    py_dict = {
        "name" : "Klejdi",
        "age" : 22 ,
        "occupation": "student"
    }
    in_json = json.dumps(py_dict)

#3. Write a Python program to convert Python objects into JSON strings. Print all the values.
def exercise3():
    py_dict = {
        "name": "Klejdi",
        "age": 22,
        "occupation": "student"
    }
    in_json = json.dumps(py_dict)
    print(in_json)

#4. Write a Python program to convert Python dictionary objects (sort by
#key) to JSON data. Print the object members with indent level 4.
def exercise4():
    py_dict = {
        "name": "Klejdi",
        "age": 22,
        "occupation": "student"
    }
    in_json = json.dumps(py_dict, sort_keys=True, indent=4)
    print(in_json)

#5. Write a Python program to create a new JSON file from an existing JSON
#file. Use the included json file ’states.json’ and create a new json file that
#does not contain the ’area code’ field.

def exercise5():
    with open('states.json', 'r') as the_file:
        data = json.load(the_file)

    states = data.get('states', [])

    for state in states:
        if 'area_codes' in state:
            del state['area_codes']

    with open('new_states.json', 'w') as file:
        json.dump(data, file, indent=4)



if __name__ == "__main__":
    print("EXERCISE SET 1")
    print("EX1")
    exercise1()
    print("EX2")
    exercise2()
    print("EX3")
    exercise3()
    print("EX4")
    exercise4()
    print("EX5")
    exercise5()