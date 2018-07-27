import subprocess
from tkinter import Tk, Listbox, Label, Button, Frame
from tkinter import FLAT, GROOVE, LEFT, RIGHT
from tkinter.filedialog import askopenfile
import csv

data = []

# Open csv and get data
def getData(filepath):
    with open(filepath, newline='') as csvfile:
        spamReader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for i , row in enumerate(spamReader):
            tmp = []
            if i != 0:
                for col in row:
                    tmp.append(col)
                data.append(tmp)

# filepath
def getDataIP(event):
    filepath = askopenfile(title="Ouvrir un csv", filetypes=[('csv files','.csv'),('all files','.*')])
    if filepath != None:
        getData(filepath.name)
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
            toSet = 'netsh interface ip set address  "Connexion au réseau local" static ' + data[i][1]+' '+data[i][2]+' '+data[i][3]
            print("Changements effectués")
            subprocess.call(toSet, shell=True)
            break

def getConfig(event):
    tmpConfig = subprocess.call('netsh interface ipv4 show address')


root = Tk()

# Frame
F_choice = Frame(root, bg="white", borderwidth=2, relief=FLAT)
F_change = Frame(F_choice, borderwidth=2, relief=GROOVE)

# Spinbox

# Label
L_titre = Label(root, text="Gestion adresse IP")


# Button
B_openFile = Button(F_change, text="ouvrir fichier")
B_change = Button(F_change, text="changer")
B_getConf = Button(F_change, text="get config")
B_raz = Button(F_change, text="raz")
B_close = Button(root, text="fermer", command=root.quit)

# Liste
Li_file = Listbox(F_change)

# Generation Graphique
L_titre.pack()
B_openFile.bind("<Button-1>", getDataIP)
B_openFile.pack()
Li_file.bind("<Double-Button-1>", changeIP)
Li_file.pack()
F_change.pack(side=LEFT, padx=30, pady=30)
B_change.bind("<Button-1>", changeIP)
B_change.pack()
B_raz.bind("<Button-1>", razIP)
B_raz.pack()
B_getConf.bind("<Button-1>", getConfig)
B_getConf.pack()
F_choice.pack()
B_close.pack()
root.mainloop()
