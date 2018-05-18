import csv

# Open csv and get data
def openFile(filepath):
    with open(filepath, newline='') as csvfile:
        spamReader = csv.reader(csvfile, delimiter=';', quotechar='|')
        data = []
        for row in spamReader:
            tmp = []
            for col in row:
                tmp.append(col)
            data.append(tmp)
    return data

# check if data place is not empty
def CheckDataPlace(data):
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if (col==''):
                print("ERREUR colonne = ",i,"ligne =",j)
                return 1
    print("FILE OK!")
    return 0

def getData(filepath):
    data = openFile(filepath)
    print("je suis ok")
    CheckDataPlace(data)