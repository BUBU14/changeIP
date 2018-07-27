import subprocess
import string
from tkinter import Tk, Listbox, Label, Button, Frame, StringVar
from tkinter import FLAT, GROOVE, LEFT, RAISED
from tkinter.filedialog import askopenfile
import csv
import socket
import netifaces



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


# recupere les adresse dans le fichier CSV
def getAdrr():
    for i, row in enumerate(data):
        print(data[i][0])
        Li_file.insert(1, data[i][0])


# remise en DHCP
def razIP(event):
    subprocess.call('netsh interface ipv4 set address "Connexion au réseau local" dhcp', shell=True)


#changr l'adresse IP
def changeIP(event):
    tmpName = Li_file.get(Li_file.curselection())
    for i, row in enumerate(data):
        if data[i][0] == tmpName :
            toSet = 'netsh interface ip set address  "Connexion au réseau local" static ' + data[i][1]+' '+data[i][2]+' '+data[i][3]
            print("Changements effectués")
            subprocess.call(toSet, shell=True)
            break

# recupere la configuration actuelle
def getConfig(event):
    MyIp = ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0])
    print(" mon IP :" + MyIp)
    Net_data = netifaces.interfaces()
    for l in Net_data:
        addrs = netifaces.ifaddresses(l)

        try :
            Ipv4 = addrs[2][0]
            addr = Ipv4['addr']
            if(addr == MyIp):
                print(addr , "---", MyIp)
                L_ip.configure(text=("IP : " + str(Ipv4['addr'])))
                L_ip.pack()
                L_mask.configure(text=("Mask : "+Ipv4['netmask']))
                L_mask.pack()
                L_pass.configure(text=("Broadcast : "+Ipv4['broadcast']))
                L_pass.pack()
                break
        except:
            break


def addConfig(event):
    print("add")

root = Tk()

# Frame
F_choice = Frame(root, bg="white", borderwidth=2, relief=FLAT)
F_change = Frame(F_choice, borderwidth=2, relief=GROOVE)
F_config = Frame(F_choice, borderwidth=2, relief=RAISED)
# Spinbox

# Label
L_titre = Label(root, text="Gestion adresse IP")
L_infoIP = Label(F_config, text="Configuration actuelle")
L_ip = Label(F_config, text="IP : ")
L_mask = Label(F_config, text="Masque : ")
L_pass = Label(F_config,text="passerelle : ")

# Text
# Button
B_openFile = Button(F_change, text="ouvrir fichier")
B_change = Button(F_change, text="changer")
B_getConf = Button(F_config, text="get config")
B_addConf = Button(F_config, text= "ajout config")
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
F_choice.pack()

B_getConf.bind("<Button-1>", getConfig)
B_getConf.pack()
L_infoIP.pack()
L_ip.pack()
L_mask.pack()
L_pass.pack()
B_addConf.bind("<Button-1>", addConfig)
B_addConf.pack()
F_config.pack()
B_close.pack()
root.mainloop()
