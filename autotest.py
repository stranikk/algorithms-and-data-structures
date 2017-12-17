import os
import re
from ExamClass import *        
from Parser import *

os.system('python3 main_homework.py input.txt output.txt')

file = open('output.txt', 'r')

file_input = open('input.txt', 'r')

res_parser = []
new_parser = []
end_range = 1
theory_diff = []
theory_type = []
practise_diff = []
practise_type = []
cheak_sum = []

get_exam = Exam()
parser(file_input,get_exam)
get_exam.sort_theory_practise()


for line in file:
    res_parser.append(line[0 : len(line)-1])

res_parser.pop(0)
res_parser.pop()
flag = 2
it = 0
for i in res_parser:
    if(flag==2) and (it!=2):
    	new_parser.append(i)
    	it = it + 1
    	if (it == 2):
    		flag = 0
    		it = 0
    else:
    	flag = flag + 1


for i in new_parser:
   
   for j in get_exam.get_theory():
    	
    	if(i==j[3]):
    		theory_type.append(j[2])
    		theory_diff.append(j[0])

for i in new_parser:
   
   for j in get_exam.get_practise():
    	
    	if(i==j[3]):
    		practise_type.append(j[2])
    		practise_diff.append(j[0])

for i in range(len(theory_diff)-1):
	if (theory_type[i] == practise_type[i]):
		print("Test is failed!!!")
	else:
		sum_bilet = theory_diff[i] + practise_diff[i]
		cheak_sum.append(sum_bilet)

delta = get_exam.get_delta()

for it in cheak_sum:
	left_board = int(round(it - it*delta/100))
	right_board = int(round(it + it*delta/100))

	for j in cheak_sum:
		if (j<left_board) or (j>right_board):
			flag = 1
			break
	if (flag == 1):
		print("Test is failed!!!")
		break
	if (end_range == int(len(cheak_sum))):
		print("Test is OK!!!")

	end_range = end_range + 1




