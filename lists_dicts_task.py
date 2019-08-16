print("Welcome to the special recruitment program, please answer the following questions: ")
skills=['python' , 'C++' , 'javascript' , 'runnung' , 'eating']
cv={}

#the name input shows an error
#name =str(input('Your name: '))
age1 = int(input('age: '))
experience1 = int(input('how many years of experience do you have? '))

print("skills: ")

for skill in skills:
	x=1
	print(skill)
	x = x + 1

#cv["name"]=name
cv["age"]=age1
cv["experience"]=experience1
cv["skills"]=' '

skill=int(input("choose a skill from above: "))

skill2=int(input("choose another skill from above: "))

cv["skills"]=str(skills[skill-1]) , str(skills[skill2-1])

#the if statement wont work 
if (skill == myskill):
	print("you have been aceepted, ")
elif (skill2 == skills[0]):
	print("you have been aceepted, ")
else:
	print("sorry, you are not accepted")

#im using this print to check if the cv works or not
print(cv)
