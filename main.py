import classify
import learn
import constants


def initialize():
    try:
        #Initializing
        print("Initializing perzeptron ...")
        number = int(input("How many inputs? "))
        listw = [] 
        lernrate = 0.0
        bias = 0.0
        cfunc = ""
        for i in range((number)):
            listw.append(float(input("What is the weight of the " + str(i+1) + ". input? ")))
        lernrate = float(input("What is the lernrate? "))
        bias = float(input("What is the bias? "))
        cfunc = func()
        print(f"{constants.GREEN}{constants.BOLD}Perzeptron successfully initialized.{constants.END}") #In green: brought to you by Neele.
        main(listw, lernrate, bias, cfunc)
    except ValueError:
        print("Invalid input. Please try again.")
        initialize()

def func():
    try:
        possible = ["h", "r", "i", "s", "t"]
        cfunc = input("What is the desired activation function (Heavy (h), ReLu (r), Identität (i), Sigmoid (s), tanh (z))? ")
        if cfunc not in possible:
            print("Invalid entry. Please try again.")
            func()
        else:
            return cfunc 
    except ValueError:
        print("Invalid input. Please try again.")
        func()

def main(listw, lernrate, bias, cfunc):
    try:
        result = 0.0
        print(listw)
        answer = input("Would you like to train the perceptron (t) or classify a point (c)? ")
        if (answer) == "t":
            print("Redirecting to Training (learn.py)")
#            iteration = int(input("How many iterations should be performed? "))
#            for i in range(iteration):
#                learn.learn(listw, lernrate, bias, cfunc)
#            main()
            learn.learn(listw, lernrate, bias, cfunc)

        elif (answer) == "c":
    #        print("Redirecting to Classification (classify.py)")
            result = classify.classify(listw, bias, cfunc)
            print(f"{constants.GREEN}{constants.BOLD}The returned value is: " + str(result) + f"{constants.END}")
            main(listw, lernrate, bias, cfunc)

        else:
            print("Please only enter 't' or 'c' ")
            main(listw, lernrate, bias, cfunc)
    except ValueError:
        print("Invalid input. Please try again.")
        main(listw, lernrate, bias, cfunc)

if __name__ == '__main__':
    initialize()