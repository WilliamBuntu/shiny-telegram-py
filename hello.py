# print('hello am learning pyhton')
# name = input('what is your name? :')
# print('hello your name is:' + name)
# print(f'hello your name is:{name}')
# n =int(input('enter any number :')) 
# if n > 0:
#     print('the number You entered is Positive')
# elif  n < 0:
#      print('the number You entered is Negative')

# else:
#       print('the number You entered is ZERO')
# n = set()
# n.add(23)
# n.add(24)
# n.add(25)
# n.add(26)
# n.add(27)
# n.add(242)

# n.remove(23)
# print(f'the set has {len(n)} elements')
# for n in range(7):
#     print('true love') 
#////// a function in python 
# def square(x):
#  return x*x

# for n in range(7):
#  print(f'the square of {n} is {square(n)}')

# class point():
#   def __init__(self,input1,input2):
#     self.x= input1
#     self.y= input2

#     p=point(34,76)
#     print(p.x )
#     print(p.y )
people =[
  { 'name': 'Gaju','house':'4points'},
   { 'name': 'Rose','house':'Hostel'},
    { 'name': 'James','house':'Amaro apartment'},
     { 'name': 'Alain','house':'Great house'}
  ]
def f(person):
    return person['name']  
  
people.sort(key=f)
print(people)