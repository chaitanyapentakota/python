def get_value(val):
    for key, value in people.items():
        if val == key:
            print(value)

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male','EmpId':'9091'},
          2: {'name': 'Marie', 'age': '25', 'sex': 'Female','EmpId':'9092'},
          3: {'name': 'chaitanya', 'age':'23','sex': 'male','EmpId':'9093'},
          4: {'name': 'lahari', 'age': '22', 'sex': 'Female','EmpId':'9094'}}
          
get_value(int(input('enter the key: ')))
