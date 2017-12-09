import os
import re

os.system('python3 /Users/nikitakurganov/Desktop/algorithms-and-data-structures-master/main_homework.py /Users/nikitakurganov/Desktop/algorithms-and-data-structures-master/input.txt /Users/nikitakurganov/Desktop/algorithms-and-data-structures-master/output.txt')

file = open('/Users/nikitakurganov/Desktop/algorithms-and-data-structures-master/output.txt', 'r')

file_input = open('/Users/nikitakurganov/Desktop/algorithms-and-data-structures-master/input.txt', 'r')

parser = file.read()
parser_delta = file_input.read()

cheak_sum = []
sum_bilet = 0
flag = 0
end_range = 1

d = re.findall(r'\d+',parser)
get_bilet = re.findall(r'\d+',parser_delta)
delta = int(get_bilet[1])

for i in range(len(d)+1):
	if (i%3 != 0) and (i!= int(len(d))):
		
		sum_bilet = int(d[i]) + sum_bilet
	else:
		if (sum_bilet!=0):
		    cheak_sum.append(sum_bilet)
		    sum_bilet = 0


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

