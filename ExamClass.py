import random
import sys
class Exam(object):
    
    __theory = []
    __practise = []
    __run_board = []
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

    
    

    def add_bilet(self):
        buffer_bilet = []
        flag = False
        i = 0
        k = 0
        run_left_board = self.__run_board[0]
        run_right_board = self.__run_board[1]
        bruteforse_len = len(self.__practise) * len(self.__theory)

        while(i!=2):
            if (i == 0):
                num = random.randint(0,len(self.__theory)-1)
                if (self.__theory[num] < run_left_board):
                    buffer_bilet.append(self.__theory[num])
                    i = i + 1
                       
            
            if (i == 1):
                for it in self.__practise:
                    if (((it+buffer_bilet[0])>run_left_board) and ((it+buffer_bilet[0])<run_right_board)):
                        buffer_bilet.append(it)
                        i = i + 1
                        break
                if(len(buffer_bilet)==1):
                    i = i - 1
                    buffer_bilet.pop()
            k = k + 1

            if (k==bruteforse_len):
                print("Error: Unable to create the exam. Choose another delta or change the number of questions")
                sys.exit()
              
        self.__result.append(buffer_bilet)
        theory_question = buffer_bilet[0]
        practise_questions = buffer_bilet[1]

        sum_bilet = theory_question + practise_questions
		
        calc_delta_of_bilet = ((self.__delta)/100) * sum_bilet
        
        left_board_bilet = sum_bilet - calc_delta_of_bilet
        right_board_bilet = sum_bilet + calc_delta_of_bilet

        
        if (int(round(left_board_bilet)) > run_left_board):
            self.__run_board[0] = int(round(left_board_bilet))
        if (int(round(right_board_bilet)) < run_right_board):
            self.__run_board[1] = int(round(right_board_bilet))

    def calc_mediana(self):
        theory_mediana = int(round(len(self.__theory)/2))
        practise_mediana = int(round(len(self.__practise)/2))
		
        sum_mediana = self.__theory[theory_mediana] + self.__practise[practise_mediana]
        print(sum_mediana)
        calc_delta_of_mediana = (self.__delta)/100 * sum_mediana

        left_mediana = sum_mediana - calc_delta_of_mediana
        right_mediana = sum_mediana + calc_delta_of_mediana
		
        self.__run_board.append(int(round(left_mediana)))
        self.__run_board.append(int(round(right_mediana)))
