import subprocess
from tkinter import *
from tkinter.filedialog import askopenfile
import csv

root = Tk()

data = []
# Open csv and get data
def getData(filepath):
    with open(filepath, newline='') as csvfile:
        spamReader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamReader:
            tmp = []
            for col in row:
                tmp.append(col)
            data.append(tmp)

# filepath
def getDataIP(event):
    filepath = askopenfile(title="Ouvrir un csv", filetypes=[('csv files','.csv'),('all files','.*')])
    if filepath !=None:
        data = getData(filepath.name)
        getAdrr()

def getAdrr():
    for i, row in enumerate(data):
        print(data[i][0])
        Li_file.insert(1, data[i][0])


def razIP(event):
    subprocess.call('netsh interface ipv4 set address "Connexion au réseau local" dhcp', shell=True)


def changeIP(event):
    tmpName = Li_file.get(Li_file.curselection())
    for i, row in enumerate(data):
        if data[i][0] == tmpName :
            print("Match adress")
            toSet = 'netsh interface ip set address  "Connexion au réseau local" static ' + data[i][1]+' '+data[i][2]+' '+data[i][3]
            print(type(toSet))
            subprocess.call(toSet, shell=True)
            break

def showWlan(event):
    show = subprocess.call('netsh interface ip show config', shell=True)
    print(show)

# Input

# Frame
F_choice = Frame(root, bg="white", borderwidth=2, relief=FLAT)
F_change = Frame(F_choice, borderwidth=2, relief=GROOVE)
F_create = Frame(F_choice, borderwidth=2, relief=SUNKEN)

# Spinbox

# Label
L_titre = Label(root, text="Gestion adresse IP")
L_ethCard = Label(F_change, text="carte Ethernet")

# Button
B_openFile = Button(F_change, text="ouvrir fichier")
B_change = Button(F_change, text="changer")
B_raz = Button(F_change, text="raz")
B_close = Button(root, text="fermer", command=root.quit)

# Liste
Li_file = Listbox(F_change)

# Generation Graphique
L_titre.pack()
L_ethCard.pack()
B_openFile.bind("<Button-1>",getDataIP)
B_openFile.pack()
Li_file.pack()
F_change.pack(side=LEFT, padx=30, pady=30)
B_change.bind("<Button-1>", changeIP)
B_change.pack()
B_raz.bind("<Button-1>", razIP)
B_raz.pack()
F_create.pack(side=RIGHT, padx=30, pady=30)
F_choice.pack()
B_close.pack()
root.mainloop()
