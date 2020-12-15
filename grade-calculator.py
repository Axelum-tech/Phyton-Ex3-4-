# general grade -student
exam_1 = float(input(" Your grade for the first exam: "))   # 0.2 float
exam_2 = float(input(" Your grade for the second exam: "))    # 0.2 float
diploma= float(input(" Your grade for diploma: "))   # 0.6 float


general_grade= 0.2*exam_1+0.2*exam_2+diploma*0.6

print("Formula for general grade:" , str(exam_1),"* 0.2 +",str(exam_2),"* 0.2 +",str(diploma),"* 0.6")
print("Your general grade is:" ,general_grade)