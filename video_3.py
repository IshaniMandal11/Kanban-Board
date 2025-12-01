# LIST(mutable)
courses= ['history','math','physics', 'hindi']
print(courses)
print(len(courses))
print(courses[1])
print(courses[-1])
# print(courses[7]) # I'll get a error saying out of range
# list function
courses.append('art')# to insert at the end of the list
courses.insert(3,'science')
print(courses) # it will insert at the given index
courses_2=['music','cricket','footbal','dance']
courses.extend(courses_2)
print(courses)
courses.remove('math')
print(courses) #for removing specific item
courses.pop()
print(courses) #it will remove the last item automatically
courses.reverse()
print(courses)
courses.sort()
print(courses)
num=[8,4,9,7,1,3,10,5,6,2]
print(num)
num.sort(reverse=True)
print(num)
sorted_list=sorted(num) #sorted function gives the true or false then have to catch to print the sorted values 
print(sorted_list)
print(min(num))
print(max(num))
print(sum(num))
print(courses.index('history'))
print('art'in courses)#gives the true and false value
for index,item in enumerate(courses,start=1):
    print(index,item)
courses_str='---' .join(courses)  
print(courses_str) 
new_list=courses_str.split('---')
print(new_list)
# =======================================================================================
# tuples(immutable)
list_1=['1','2','3','4','5','6']
list_2=list_1
print(list_1)
print(list_2)
list_1[0]=10
print(list_1)
print(list_2)
# in list can be change the value 
# tuple_1=('1','2','3','4','5','6')
# tuple_2=tuple_1
# tuple_1[0]=10
# print(tuple_1)
# print(tuple_2)
# this will show an error saying assignment is not allowed in tuple 
# ===========================================================================
# SET
# SETS are the unorder and no dublicate value
set_1={'1','2','3','5','1','2'}
set_2={'1','2','9','11'}
set_1.intersection(set_2) #gives the same in both and the other element in the set_1
print(set_1.difference(set_2))
print(set_1.union(set_2))
print('2' in set_1)
print(set_1)
