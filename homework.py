import re
import sys
import copy
import array
import random

input = open(sys.argv[1], 'r')
output = open(sys.argv[2], 'w')
res = []
parser = []
buf = []
buf_start = []
start = ""
def random_gen(list_res):
    random_question = []
    random.shuffle(list_res)
    list_size = random.randint(0, len(list_res) - 1)
    for it in list_res[list_size]:
        random_question.append(it)
    return random_question
    
    

for line in input:
    parser.append(line[0 : len(line)-1])

for it in parser:
    if (len(it) != 0):
        buf.append(it)
        if(parser.index(it) == len(parser) - 1):
            buf_time1 = buf[:]
            res.append(buf_time1)
            del buf[:]
    else:
        buf_time=buf[:]
        res.append(buf_time)
        del buf[:]
        
for it in res.pop(0):
    start = it

buf_start = re.findall(r'-?\d+', start)
exam_size = int(buf_start[0])
difficulty = int(buf_start[1])

i = 0
flag = 0
ticket_constract = []
tickets = []

while (i != exam_size):
    process = copy.deepcopy(random_gen(res))
    
    if (flag == 0) and (int(process[2]) < difficulty):
        ticket_constract.append(process)
    
        flag = flag + 1
    
    else:
    
        if(int(process[2]) == (difficulty - int(ticket_constract[0][2]))) and (process[3] != ticket_constract[0][3]): 
            ticket_constract.append(process)
            
            tickets.append(ticket_constract[:])
            i = i + 1
            del ticket_constract[:]
            flag = 0
			

number_ticket = 0			
for i in tickets:

    number_ticket = number_ticket + 1
    output.write("------------------------ Number № " + str(number_ticket) + " ------------------------\n")
    for j in i:
	    output.write(str(j[0])+"\n")
	
    output.write("------------------------------------------------------------\n")