from input_m import inp_m
from process_m import pro_m
from output_m import output
import welcome
import os
os.system("clear")
 
welcome.greet()

while(True):

    i = inp_m()
    p = pro_m(i)
    output(p)

