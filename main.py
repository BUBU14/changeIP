import subprocess
from tkinter import *
from tkinter.filedialog import askopenfile
from getData import getData

root = Tk()

def getInfo(event):
    print("OK")

# filepath
def getDataIP(event):
    filepath = askopenfile(title="Ouvrir un csv", filetypes=[('csv files','.csv'),('all files','.*')])
    if filepath !=None:
        getData(filepath.name)

def razIP(event):
    subprocess.call('netsh interface ipv4 set address "Réseau local" dhcp', shell=True)

def changeIP(event):
    print("work in progress")

def showWlan(event):
    show = subprocess.call('netsh wlan show profiles', shell=True)
    print(show)


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
B_ShowWLAN = Button(F_change, text="WLAN")
B_raz = Button(F_change, text="raz")
B_create = Button(F_create, text="generer")
B_close = Button(root, text="fermer", command=root.quit)

# Liste
Li_file = Listbox(F_change)

# Generation Graphique
L_titre.pack()
L_ethCard.pack()
B_ShowWLAN.bind("<Button-1>",showWlan)
B_ShowWLAN.pack()
B_openFile.bind("<Button-1>",getDataIP)
B_openFile.pack()
Li_file.pack()
F_change.pack(side=LEFT, padx=30, pady=30)
B_change.bind("<Button-1>", changeIP)
B_change.pack()
B_raz.bind("<Button-1>", razIP)
B_raz.pack()
F_create.pack(side=RIGHT, padx=30, pady=30)
B_create.bind("<Button-1>", getInfo)
B_create.pack()
F_choice.pack()
B_close.pack()
root.mainloop()
