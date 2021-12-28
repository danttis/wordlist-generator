import random

vector = ["name","lastname","20","random_information","spouse"] # you can add more information that you find in the profiles or that you want
vector_number = ["1","2","3","4","12","123","1234","12345"] # You can also add more numbers or other combinations
cont = int(input("How many combinations do you want to create? \n"))

line_break = "\n"
age = 2021 - int(vector[2]);
vector.append(str(age))
i = 0
file = open('wordlist.txt', 'w')
def check_string(x):
    with open('wordlist.txt') as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if x in line:
            return False # The string is found
    return True  # The string does not exist in the file


for i in range(cont):
  a = vector[random.randint(0,5)]+vector[random.randint(0,5)]
  b = vector[random.randint(0,5)]+vector_number[random.randint(0,7)]
  if check_string(a):
    file.write(a+line_break)
  if check_string(b):
    file.write(b+line_break)
 
file.close()
