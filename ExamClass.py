import random
class Exam(object):
    
    __theory = []
    __practise = []
    __if_bilet = []
    __result = []
    __exam_size = 0
    __delta = 0
	
    def add_theory(self, num):
        self.__theory.append(num)

    def add_practise(self,num):
        self.__practise.append(num)

    def init_ex_size(self,num):
        self.__exam_size = num

    def init_delta(self,num):
        self.__delta = num

    def get_theory(self):
        return self.__theory

    def get_practise(self):
        return self.__practise

    def get_ex_size(self):
        return self.__exam_size

    def get_delta(self):
        return self.__delta

    def get_result(self):
        return self.__result
    def sort_theory_practise(self):
        self.__theory.sort()
        self.__practise.sort()

    def get_if_bilet(self):
        return self.__if_bilet
    

    def add_bilet(self):
        buffer_bilet = []
        flag = False
        i = 0
        while(i!=2):
            if (i == 0):
                num = random.randint(0,len(self.__theory)-1)
                if (self.__theory[num] < self.__if_bilet[0]):
                    buffer_bilet.append(self.__theory[num])
                    i = i + 1
                       
            
            if (i == 1):
                for it in self.__practise:
                    if (((it+buffer_bilet[0])>self.__if_bilet[0]) and ((it+buffer_bilet[0])<self.__if_bilet[1])):
                        buffer_bilet.append(it)
                        i = i + 1
                        break
                if(len(buffer_bilet)==1):
                    i = i - 1
                    buffer_bilet.pop()
                        
        self.__result.append(buffer_bilet)
        sum_bilet = buffer_bilet[0] + buffer_bilet[1]
		
        left_board = sum_bilet - ((self.__delta)/100) * sum_bilet
        right_board = sum_bilet + ((self.__delta)/100) * sum_bilet
		
        if (int(round(left_board)) > self.__if_bilet[0]):
            self.__if_bilet[0] = int(round(left_board))
        if (int(round(right_board)) < self.__if_bilet[1]):
            self.__if_bilet[1] = int(round(right_board))

    def calc_mediana(self):
        mediana1 = int(round(len(self.__theory)/2))
        mediana2 = int(round(len(self.__practise)/2))
		
        sum_mediana = self.__theory[mediana1] + self.__practise[mediana2]
		
        left_mediana = sum_mediana - (self.__delta)/100 * sum_mediana
        right_mediana = sum_mediana + (self.__delta)/100 * sum_mediana
		
        self.__if_bilet.append(int(round(left_mediana)))
        self.__if_bilet.append(int(round(right_mediana)))
