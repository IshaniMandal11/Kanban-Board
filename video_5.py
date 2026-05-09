# ture and false value called boolen
if True:
    print('condition is true')
if False:
    print('condition is False')
language='java'
if language=='python':
    print('condition is true the language is python')
elif language=='java':
    print('condition is true the language is java')
else:
    print('No match')



# AND 
# OR
# NOT
# python does not have swith case
user ="admin"
logged_in=True
if user=='admin' and logged_in:
    print('admin page')
else:
    print('bad crads')

if user=='admin' and logged_in:
    print('admin page')
else:
    print('bad crads')

if not logged_in:
    print('plesae login')
else:
    print('welcome to the page')


# ============================================================
# difference between the == and is (is evauate the object is same or not )
a=[1,2,3]
b=[1,2,3]
print(a==b)
print(a is  b)
a=[1,2,3]
b=a
print(a == b)
print(a is b) #now this will be true becouse refereing to same object
print(id(a))
print(id(b))
# the values which is evauate as false in condition
#false
condition=False
if condition :
    print('evauated to true ')
else:
    print('evaluated to false')


#none
condition=None
if condition :
    print('evauated to true ')
else:
    print('evaluated to false')
#any number 
condition= 0
if condition :
    print('evauated to true ')
else:
    print('evaluated to false')

#any number non zero in negative
condition= -1
if condition :
    print('evauated to true ')
else:
    print('evaluated to false')


#any number non zero and non negative
condition= 10
if condition :
    print('evauated to true ')
else:
    print('evaluated to false')


#any empty sequence. for example "",{},(),[]
condition=''
if condition :
    print('evauated to true ')
else:
    print('evaluated to false')


#any empty maping eg. {}
condition={}
if condition :
    print('evauated to true ')
else:
    print('evaluated to false')
