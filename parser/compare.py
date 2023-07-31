import re

names_1 : list = []
names_2 : list = []

with open("parser/test.txt", 'r') as file_1, open("parser/text.txt") as file_2:
     for line in file_1:
          temp = line.split("(")
          try:
               # print(temp[0] + '(' + temp[1])
               names_1.append(temp[0] + temp[1])
          except:
               pass


     for line in file_2:
          temp = line.split("(")
          try:
               # print(temp[0] + '(' + temp[1])
               names_2.append(temp[0] + temp[1])
          except:
               pass


     for line_1 in names_1:
          for line_2 in names_2:
               if line_1.lower() == line_2.lower():
                    print(line_1)