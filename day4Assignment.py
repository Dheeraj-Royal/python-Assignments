name='Dheeraj'
age=20
height=5.11
marriedStatus=False
hobbies=['painting','playing','music','reading']
favFood=('biriyani','mushroom','paneer','dosa','eggBurji')
marks={'ssc':970,'inter_1+2':957,'1st_btech':945}

def fun_data_types(name,age,height,marrstatus,hob=[],favfood=(),marks={}):
    print("<<<FUNCTION_1 IS RUNNING>>>\n")
    print(f'Details of {name} are :')
    print('    %s Age is :%s and Height is :%s'%(name,age,height))
    print('    Married status of {1} is :{0}'.format(marrstatus,name))
    print("    Hobbies of Dheeraj are :",hob)
    print("    Favourite foods are :",favFood)
    print('    Marks of Dheeraj are :',marks.items())

fun_data_types(name,age,height,marriedStatus,hobbies,favFood,marks)



def fun_dict_ittiration(dic):
    print("\n\n<<<FUNCTION_2 IS RUNNING>>>\n")
    for key,val in dic.items():
        print(f"key is :{key} ,and its Value is :{val}")
details={
    'name':'Dheeraj',
    'age':20,
    'height':5.11,
    'place':'palamaner',
    'hobbies':['painting','playing'],
    'languages':('telugu','tamil','english')
}
fun_dict_ittiration(details)

def fun_list(a,b):
    print("\n\n<<<FUNCTION_3 IS RUNNING>>>\n")
    return [a,b]
print("\n\nEnter two values for function 3")
a = int(input("Enter a value for list :"))
b = int(input("Enter b value for list :"))
L = print(fun_list(a,b))
