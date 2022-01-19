name='Dheeraj'
age=20
height=5.11
marriedStatus=False
hobbies=['painting','playing','music','reading']
favFood=('biriyani','mushroom','paneer','dosa','eggBurji')
marks={'ssc':970,'inter_1+2':957,'1st_btech':945}

print(f'Details of {name} are :')
print('    %s Age is :%s and Height is :%s'%(name,age,height))
print('    Married status of {1} is :{0}'.format(marriedStatus,name))
print("    Hobbies of Dheeraj are :",hobbies)
print("    Favourite foods are :",favFood)
print('    Marks of Dheeraj are :',marks.items())
