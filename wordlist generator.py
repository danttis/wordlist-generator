import random

vector = ["name","lastname","20","random_information","spouse"] # you can add more information that you find in the profiles or that you want
vector_number = ["1","2","3","4","12","123","1234","12345"] # You can also add more numbers or other combinations
cont = int(input("How many combinations do you want to create? \nEach combination generates 12 passwords: "))

line_break = "\n"
age = 2021 - int(vector[2]);
vector.append(str(age))
i = 0
file = open('wordlist.txt', 'w')

while True:
  
  file.write(vector[random.randint(0,5)]+vector[random.randint(0,5)]+line_break)
  file.write(vector[random.randint(0,5)]+vector[random.randint(0,5)]+line_break)
  file.write(vector[random.randint(0,5)]+vector[random.randint(0,5)]+line_break)
  file.write(vector[random.randint(0,5)]+vector[random.randint(0,5)]+line_break)
  file.write(vector[random.randint(0,5)]+vector[random.randint(0,5)]+line_break)
  file.write(vector[random.randint(0,5)]+vector[random.randint(0,5)]+line_break)
  file.write(vector[random.randint(0,5)]+vector_number[random.randint(0,7)]+line_break)
  file.write(vector[random.randint(0,5)]+vector_number[random.randint(0,7)]+line_break)
  file.write(vector[random.randint(0,5)]+vector_number[random.randint(0,7)]+line_break)
  file.write(vector[random.randint(0,5)]+vector_number[random.randint(0,7)]+line_break)
  file.write(vector[random.randint(0,5)]+vector_number[random.randint(0,7)]+line_break)
  file.write(vector[random.randint(0,5)]+vector_number[random.randint(0,7)]+line_break)

  i+=1
  if i == cont:
    break

file.close()
