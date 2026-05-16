import csv
import perzept
import main

def learn(listw, lernrate, bias, cfunc):
    #print("Hello Learn")
    trainingdata = []
    print(listw)
    with open('learning_data.csv', 'r', encoding='utf-8') as daten:
        reader = csv.reader(daten)
        for sdat in reader:
            trainingdata = []
            sdat = sdat[0].split(';')
#            print(sdat)
            for i in range(len(sdat) -1):
                trainingdata.append(sdat[i])
                trainingdata[-1] = float(trainingdata[-1])
#            print(trainingdata)
            listwsave = listw
            listw = trainw(trainingdata, sdat[-1], listw, lernrate, bias, cfunc)
            bias = trainb(trainingdata, sdat[-1], listwsave, lernrate, bias, cfunc)            
    main.main(listw, lernrate, bias, cfunc)


def trainw(data, label, listw, lernrate, bias, cfunc):
    result = perzept.percept(data, listw, bias, cfunc)
    if result != label:
        for i in range(len(listw)):
            listw[i] = listw[i] + lernrate * (float(label) - float(result)) * data[i]
        print(listw)
    return listw

def trainb(data, label, listw, lernrate, bias, cfunc):
    result = perzept.percept(data, listw, bias, cfunc)
    if result != label:
        bias = bias - 1 * lernrate * (float(label) - float(result))
    print(bias)
    return bias