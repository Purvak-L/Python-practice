'''
Python - Dictionary
'''

student = {'name':"Purvak",'age':25,'courses':['SPCC','DSIP',"AI"]}

print(student)
print(student.get('name'))
#When we try to access key which is not present
print(student.get('phone'))
student['name'] = 'Apk'
student['phone'] = [90,23,45]
print(student.get('phone'))
print(student)

#update takes Dictionary as input
student.update({'anthing':16})
student.update({'name':'Purvak'})
print(student)


# To remove values
del student['age']
print(student)
popped = student.pop('courses')
print(popped)

print (student.keys())
print (student.values())
print(student.items())


for key,values in student.items():
    print (key,values)
