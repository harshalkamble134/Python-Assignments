# 1. Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five.
# [19, 19, 5, 5, 5, 5, 5]
# Output:
# True
# [19, 15, 15, 5, 3, 3, 5, 2]
# Output:12

# False

a=[]
while True:
    i=input("enter the list items: ")
    if i=="":
        break
    else:
        a.append(i) 
count19=0
count5=0
for num1 in a:
    if num1==19:
        count19+=1
    elif num1==5:
        count5+=1
if count19==2 and count5>=3:
    print(True)
else:
    print(False)

# 2. Write a Python program that accept a list of integers and check the length and the fifth element. Return true if the length of the list is 8 and fifth element occurs thrice in the said list. 
# Input:
# [19, 19, 15, 5, 5, 5, 1, 2]
# Output:
# True
# Input:
# [19, 15, 5, 7, 5, 5, 2]
# Output:
# False

a=[]
while True:
    i=input("enter the list items: ")
    if i=="":
        break
    else:
        a.append(i) 
print(a)
x=a[4]
count=0
for i in a:
    if i==x:
        count+=1
if count==3 and len(a)==8:
    print(True)
else:
    print(False)

# 3.  Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators. 
# Input: The dance, held in the school gym, ended at midnight.
# Output:
# [['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]


a='The dance, held in the school gym, ended at midnight.'
b=a.split(',')
c=""
for i in range (len(b)):
  c+=b[i]
d=c.split()
q=[]
for i in a:
  if i==' ' or i==",":
    q.append(i)
w=[]
w.append(d)
w.append(q)
print(w)

# 4. Write a Python program to find missing numbers from a list. Input : [1,2,3,4,6,7,10]
# Output : [5, 8, 9]

a=[1,2,3,4,5,6,7,8,9,10]
s=[1,2,3,4,6,7,10]
d=[]
for i in a:
  if i not in s:
    d.append(i)
print(d) 

# 5. Write a Python program to push all zeros to the end of a list. Input : [0,2,3,4,6,7,10]
# Output : [2, 3, 4, 6, 7, 10, 0]

# a=[0,2,3,4,6,7,10]
a=[]
while True:
    i=input("enter the list items: ")
    if i=="":
        break
    else:
        a.append(i)
for i in a:
  if i=="0":
    a.remove(i)
    a.append(i)
print(a) 



#Question1

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
list_out=[]
odd=[]
even=[]
for i in range(0,len(listOne)):
    if i%2!=0:
        odd.append(listOne[i])
        list_out.append(listOne[i])
for i in range(0,len(listTwo)):
    if i%2==0:
        even.append(listTwo[i])
        list_out.append(listTwo[i])

print("Element at odd-index positions from list one")
print(odd)
print("Element at even-index positions from list one")
print(even)
print("Printing Final third list")
print(list_out)


#Question 2

# Given a number count the total number of digits in a number
count=0
num=int(input("Enter the Number"))
if num==0:
    print("Invalid")
while num>0:
     x=num%10
     num=num//10
     count=count+1
print("total number of digits in a number :",count)


#Question 3
# Write a Python program to print the numbers of a
# specified list after removing even numbers from it.


list=[]
while True:
    num=input("Enter the number : ")
    if num=="":
            break
    if num.isdigit() :
        if int(num)%2==0:
            continue
        else:
            list.append(int(num))
    else:
        print("Please Enter Only Numbers")
print(list)
