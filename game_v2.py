'''
Game predict number
Computer write the number and predict it 
'''

import numpy as np


def random_predict(number:int=1) -> int:
    """Random predict number

    Args:
        number (int, optional): Written number. Defaults to 1.

    Returns:
        int: Number attemps
    """
    count=0

    while True:
        count+=1
        predict_number = np.random.randint(1,101)
        if(number == predict_number):
            break
    return(count)

def score_game(random_predict) ->int:
    """How many average of attemps need to predict the number?

    Args:
        random_predict ([type]): predict function

    Returns:
        int: average attemps
    """
    count_ls=[]
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f'Average attemps of your algorithm is : {score} attemps')
    return score

if __name__ == '__main__':
    #RUN
    score_game(random_predict)
