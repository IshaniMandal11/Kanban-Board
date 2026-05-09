# function
def hello_fun():
    psss
print(hello_fun)
# =========================================
def hellow(greeting, name='abhisek'): #this name will take abhisek by default
    # return 'this is a string return value'
    return '{},{}'.format(greeting,name)
print(hellow('hi',name='abhisek_i'))
# print(hellow().upper()) #so doing this no one will get to know what is inside the function . follows the DRY principle.
# ================================================
def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
course=['math','phy','art', 'art']
std_info={'name':'ishani','roll':1}
student_info(course,std_info)#it will gives you a tupple with packed with argument types inside it
student_info(*course,**std_info)#it will gives you unpacked arguments 
# =======================================================
month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31] #first place for index purpose
def is_leap(year): #return the leap year . false if it is a non leap year
    return year % 4==0 and (year%100!= 0 or year % 400 == 0)
def days_in_month(year,month):
    # returns the dayes in the month of the year
    if not 1 <= month <= 12:
        return 'Invalid month'

    if month == 2 and is_leap(year):
        return 29
    return month_days[month]
year=1999
month=8
print(is_leap(year))
print(days_in_month(year,month))
# ==========================================
# this is my module .py (ill use this code to import)
print('imported my_module which is in video_7.py')
text='test string'
def find_index(to_search, target):
    'find the text value in sequence'
    for i, value in enumerate(to_search):
        if value == target:
            return 1
    return -1

