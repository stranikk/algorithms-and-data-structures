import re
import sys
from ExamClass import *        
from Parser import *

def main():

    programm_input = open(sys.argv[1], 'r')
    programm_output = open(sys.argv[2], 'w')
    i = 0
    get_exam = Exam()

    parser(programm_input,get_exam)

    get_exam.sort_theory_practise()
    get_exam.calc_mediana()

    for i in range(get_exam.get_ex_size()):
        get_exam.add_bilet()

    print_exam(programm_output,get_exam)

if __name__ == "__main__":
    main()






