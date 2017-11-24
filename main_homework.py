import re
import sys
import copy
import array
import random


class Exam(object):
    """docstring for Exam"""
    def __init__(self, theory,practise,if_bilet,result,exam_size,delta,mediana):
        self.theory = theory
        self.practise = practise
        self.if_bilet = if_bilet
        self.result = result
        self.exam_size = exam_size
        self.delta = delta
        self.mediana = mediana

    def add_theory(self, num):
        self.theory.append(num)

    def add_practise(self,num):
        self.practise.append(num)

    def init_ex_size(self,num):
        self.exam_size = num

    def init_delta(self,num):
        self.delta = num

    def get_theory(self):
        return self.theory

    def get_practise(self):
        return self.practise

    def get_ex_size(self):
        return self.exam_size

    def get_delta(self):
        return self.delta

    def get_result(self):
        return self.result
    def sort_theory_practise(self):
        self.theory.sort()
        self.practise.sort()

    def get_if_bilet(self):
        return self.if_bilet
    def get_mediana(self):
        return self.mediana

    def add_bilet(self):
        buffer_bilet = []
        flag = False
        i = 0
        while(i!=2):
            if (i == 0):
                num = random.randint(0,len(self.theory)-1)
                if (self.theory[num] < self.if_bilet[0]):
                    buffer_bilet.append(self.theory[num])
                    i = i + 1
                       
            
            if (i == 1):
                for it in self.practise:
                    if (((it+buffer_bilet[0])>self.if_bilet[0]) and ((it+buffer_bilet[0])<self.if_bilet[1])):
                        buffer_bilet.append(it)
                        i = i + 1
                        break
                        #print(buffer_bilet)
        self.result.append(buffer_bilet)
        #print(buffer_bilet)
        sum_bilet = buffer_bilet[0] + buffer_bilet[1]
        if (int(round(sum_bilet - (((self.delta)/100) * sum_bilet))) > self.if_bilet[0]):
            self.if_bilet[0] = int(round(sum_bilet - (((self.delta)/100) * sum_bilet)))
        if (int(round(sum_bilet + (((self.delta)/100) * sum_bilet))) < self.if_bilet[1]):
            self.if_bilet[1] = int(round(sum_bilet + (((self.delta)/100) * sum_bilet)))



    def calc_mediana(self):
        if (len(self.theory)>len(self.practise)):
            self.mediana = int(round(len(self.theory)/2))
        else:
            self.mediana = int(round(len(self.practise)/2))

        self.if_bilet.append(int(round(self.theory[self.mediana] - (((self.delta)/100) * self.theory[self.mediana]))))
        self.if_bilet.append(int(round(self.theory[self.mediana] + (((self.delta)/100) * self.theory[self.mediana]))))


input = open(sys.argv[1], 'r')
output = open(sys.argv[2], 'w')

parser = []
errors = 0
flag = False
i = 0
number_bilet = 0

get_exam = Exam([],[],[],[],0,0,0)
    
for line in input:
    parser.append(line[0 : len(line)-1])


for it in parser:
    if ((len(it)!=0)and(flag==False)):
        flag = True
        result = re.findall(r'\d+', it)
        if(len(result)!=2):
            print("Error: incorrect start parametrs")
            break
        get_exam.init_ex_size(int(result[0]))
        get_exam.init_delta(int(result[1]))
        
    if ((len(it)!=0)and(flag==True)):
        res = re.findall(r'\d+', it)
        
        if((len(res)!=2) and ((int(res[1])!=0) or (int(res[1])!=1))):
            errors = errors + 1
            print("Error: incorrect format question " + str(errors))
            continue
        else:
            if (int(res[1])==0):
                get_exam.add_theory(int(res[0]))
            if (int(res[1])==1):
                get_exam.add_practise(int(res[0]))

get_exam.sort_theory_practise()
get_exam.calc_mediana()

for i in range(get_exam.get_ex_size()):
    get_exam.add_bilet()

#print("exam: ")
#print(get_exam.get_result())

for it in get_exam.get_result():
    number_bilet = number_bilet + 1
    output.write("------------------------ Number № " + str(number_bilet) + " ------------------------\n")

    for j in it:
        output.write(str(j)+"\n")
    output.write("------------------------------------------------------------\n")







