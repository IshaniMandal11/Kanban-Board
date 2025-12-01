# print the welcome message
message='hellow world '
message1="this example for double quote to print the string"
message2="""this is multi 
line string with triple double quotes
to show the multi line string"""
message3='''this is the multiline
string with triple single quote 
to show the multiline string'''
print(message)
print(message1)
print(message2)
print(message3)
# ==========================================================
# scape sequence character(this is use to print the character which is normally used to operate or have some predefined character)
print("\"this is the scape sequence character example \" (like wise we can add any character after backslace)")
# ============================================================
# some function in string and string slicing
# len()-->this function is used to find the lenth of a string 
print(len(message3))
print(message[0]) # prints the 0'th index character
print(message[0:12])
print(message[0:6])
print(message[7:])
print(message[-5:0]) #wont work in my case
print(message.lower())
print(message.upper())
print(message.count("hellow")) # gives the number of time's  it apper
print(message.find('world')) # gives the index from the string when it is first time appers
print(message.replace('world','universe'))# it take the argument which is has to be replace with whom and it does ot change the original string untill you replace it specifically by assigning to the same string 
# ================================================================
# string concatination 
greeting='hello'
name='ishani'
message=greeting +' , '+ name +' nice to meet you.'
print(message)
message='{},{}. welcome !'.format(greeting, name)
print(message)
message=f'{ greeting},{name.upper()}. namaste!'
print(message)
print(dir(message)) # gives all the function which can be used with this variable
# print(help()) # to know more about any particular function 