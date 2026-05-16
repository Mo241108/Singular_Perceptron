import perzept
import main

def classify(listw, bias, cfunc):
    #print("Hello Classify")
    listx = []
    try:
        if listx == []:
            for i in range(len(listw)):
                listx.append(float(input("What is your " + str(i+1) + ". input? ")))
    except ValueError:
        print("Invalid input. Please try again.")
        classify(listw, bias, cfunc)
#    print(listw)
#    print(b)
#    print(cfunc)
#    print(listx)
    result = perzept.percept(listx, listw, bias, cfunc)

    return result

if __name__ == "__main__":
    classify()