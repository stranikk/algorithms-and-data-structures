import re
import sys
from ExamClass import *

def parser(data,get_exam):
    parser = []
    flag = False
    for line in data:
        parser.append(line[0 : len(line)-1])

    for it in parser:
        
        if ((len(it)!=0)and(flag==True)):
            res = re.findall(r'\d+', it)
            if((len(res)!=2) or (int(res[1])!=0) and (int(res[1])!=1)):
                print("Error: incorrect format question")
                sys.exit()
            else:
                if (int(res[1])==0):
                    get_exam.add_theory(int(res[0]))
                if (int(res[1])==1):
                    get_exam.add_practise(int(res[0]))

        if ((len(it)!=0)and(flag==False)):
            flag = True
            result = re.findall(r'\d+', it)
            if(int(len(result))!=2):
                print("Error: incorrect start parametrs")
                sys.exit()
            get_exam.init_ex_size(int(result[0]))
            get_exam.init_delta(int(result[1]))

    len_questions = len(get_exam.get_theory())*len(get_exam.get_practise())

    if len_questions < get_exam.get_ex_size():
        print("Error: There are not enough questions for the exam")
        sys.exit()

					
def print_exam(data,get_exam):
    
    number_bilet = 0
    CONST_PARAM = "------------------------"
    CONST_END_PARAM = "------------------------\n"
    CONST_END = "------------------------------------------------------------\n"
    for it in get_exam.get_result():
        number_bilet = number_bilet + 1
        data.write('{0} {1} {2} {3}'.format(CONST_PARAM,"Number №",str(number_bilet),CONST_END_PARAM))

        for j in it:
            data.write(str(j)+"\n")
        data.write('{0}'.format(CONST_END))