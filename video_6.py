nums=[1,2,3,4,5,6,7,]
for num in nums:
    if num==4:
        print('number found')
        break # break statement which break the sequence and it will go out of the loop
    print(num)

# ===============================================
for num in nums:
    if num==4:
        print('continue')
        continue # continue statement which continue  the sequence but only the match number will not be printed
    print(num)


# =================================================

# nested loop

for num in nums:
    for letter in 'abc':
        print(num, letter)


# ==========================================================
# range function
for i in range(1,11):
    print(i)# automatically prints up to 1 to 10

# ========================================================
#while loop
x=0
while x<10:
    print(x)
    x+=1
