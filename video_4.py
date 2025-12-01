# DISTONAY(KEY VALUE PAIRS called hash map in other programming language)
student={'name':'ishani','age':'20','roll number':1, 'subject':['math','science','social science','hindi','english']}
print(student)
print(student['name'])
# print(student['phone'])# throw an error 
print(student.get('name'))
print(student.get('phone')) # will give a none insted of throwing and error
print(student.get('phone','this item is not found in this distonary')) #if item not found then it will show the second argument message 
student['phone']='999-666-5555'
print(student)
student.update({'name':'Abhisek'})
print(student)
del student['roll number']
print(student)
age=student.pop('age')
print(age)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
for key, value in student.items():
    print(key, value)