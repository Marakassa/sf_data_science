'''Game predict number'''

import numpy as np

number = np.random.randint(1,101)
count=0

while True:
    count+=1
    predict_number = int(input("Predict the number from 1 to 100: "))
    
    if(predict_number > number):
        print("The number too big!")
    elif(predict_number < number):
        print("The number too small!")
    else:
        print(f"You predict the number. Number is = {number} in {count} attempts")
        break
