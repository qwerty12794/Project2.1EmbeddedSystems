from tkinter import *
from tkinter import messagebox
from tkinter import ttk


"""
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=Singleton):
    pass
"""
import matplotlib.pyplot as plt

from GUI.Arduino import python
from GUI.Centrale import metingen
#from GUI.Centrale import nieuwbordje


class GUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()
        self.columnconfigure(10, weight=1)
        self.rowconfigure(3, weight=1)
        self.pack(fill=BOTH, expand=1, padx=5, pady=5)

    def initUI(self):
        self.parent.title("Test")
        self.pack(fill=BOTH, expand=1)

def test():
    try:
        try1 = "try"
        print(try1)
        return try1
    except:
        try1="except"
        print(try1)
        return try1

def grafiekuur():
    plt.figure(1)
    plt.suptitle("Temperatuur/licht per minuut van het afgelopen uur.")
    plt.subplot(211)
    plt.plot(metingen.listtemp, 'r-')
    plt.xlabel("Minuut")
    plt.xlim([0, 60])
    plt.ylabel("Temperatuur")
    plt.grid(True)
    plt.subplot(212)
    plt.plot(metingen.listlight, 'r-')
    plt.xlabel("Minuut")
    plt.xlim([0, 60])
    plt.ylabel("Licht")
    plt.grid(True)
    plt.show()

def grafiekdag():
    plt.figure(1)
    plt.suptitle("Temperatuur/licht per uur van de afgelopen 24 uur")
    plt.subplot(211)
    plt.plot(metingen.listtempuur, 'r-')
    plt.xlabel("Uur")
    plt.xlim([0, 24])
    plt.ylabel("Temperatuur")
    plt.grid(True)
    plt.subplot(212)
    plt.plot(metingen.listlightuur, 'r-')
    plt.xlabel("Uur")
    plt.xlim([0, 24])
    plt.ylabel("Licht")
    plt.grid(True)
    plt.show()

def grafiekweek():
    plt.figure(1)
    plt.suptitle("Temperatuur/licht per dag van de afgelopen week")
    plt.subplot(211)
    plt.plot(metingen.listtempdag, 'r-')
    plt.xlabel("Dag")
    plt.xlim([0, 7])
    plt.ylabel("Temperatuur")
    plt.grid(True)
    plt.subplot(212)
    plt.plot(metingen.listlightdag, 'r-')
    plt.xlabel("Dag")
    plt.xlim([0, 7])
    plt.ylabel("Licht")
    plt.grid(True)
    plt.show()

def grafiekmaand():
    plt.figure(1)
    plt.suptitle("Temperatuur/licht per week van de afgelopen 4 weken")
    plt.subplot(211)
    plt.plot(metingen.listtempweek, 'r-')
    plt.xlabel("Week")
    plt.xlim([0, 4])
    plt.ylabel("Temperatuur")
    plt.grid(True)
    plt.subplot(212)
    plt.plot(metingen.listlightweek, 'r-')
    plt.xlabel("Week")
    plt.xlim([0, 4])
    plt.ylabel("Licht")
    plt.grid(True)
    plt.show()

def grafiekjaar():
    plt.figure(1)
    plt.suptitle("Temperatuur/licht per maand van de afgelopen 12 maanden.")
    plt.subplot(211)
    plt.plot(metingen.listtempmaand, 'r-')
    plt.xlabel("Maand")
    plt.xlim([0, 12])
    plt.ylabel("Temperatuur")
    plt.grid(True)
    plt.subplot(212)
    plt.plot(metingen.listlightmaand, 'r-')
    plt.xlabel("Maand")
    plt.xlim([0, 12])
    plt.ylabel("Licht")
    plt.grid(True)
    plt.show()


opvulling = 0

def main():
    instellingenvenster_dict={}
    statusvenster_dict={}

    #maakt een instellingenvenster aan voor een bordje
    class instellingenvenster:

        def __init__(self,welkearduino,Arduinotab):
            self.welkearduino = welkearduino
            self.nummer = (1 + int(python.Arduino.get(self.welkearduino).nummer))
            self.instellingenvenstertje = Tk()
            self.instellingenvenstertje.wm_title('Instellingen')
            instellingenvenster_dict.update({self.nummer : self.instellingenvenstertje})
            self.instellingenvenstertje.geometry("300x200+300+300")
            self.ivensterlabel = ttk.Label(self.instellingenvenstertje, text='Instellingen bord %d' % self.nummer)
            self.ivensterlabel.grid(row=0,column=1)
            self.isep1 = ttk.Separator(self.instellingenvenstertje)
            self.isep1.grid(row=1,column=0,sticky='ew')
            self.isep2 = ttk.Separator(self.instellingenvenstertje)
            self.isep2.grid(row=1,column=1,sticky='ew')
            self.isep3 = ttk.Separator(self.instellingenvenstertje)
            self.isep3.grid(row=1,column=2,stick='ew')
            self.iwhitespace1 = ttk.Label(self.instellingenvenstertje)
            self.iwhitespace1.grid(row=2,column=1)
            self.iuitrollengte = ttk.Label(self.instellingenvenstertje, text='Uitrollengte: ')
            self.iuitrollengte.grid(row=3,column=1)

            def set50cm(self):
                stuurcommando(self.welkearduino, 7)
                isluit(self)

            def set100cm(self):
                stuurcommando(self.welkearduino, 8)
                isluit(self)

            def set150cm(self):
                stuurcommando(self.welkearduino, 9)
                isluit(self)


            self.i50cm = ttk.Button(self.instellingenvenstertje, text='50 cm', command= lambda: set50cm(self))
            self.i50cm.grid(row=4,column=0)
            self.i100cm = ttk.Button(self.instellingenvenstertje, text='100 cm', command= lambda: set100cm(self))
            self.i100cm.grid(row=4,column=1)
            self.ihelemaal= ttk.Button(self.instellingenvenstertje, text='Helemaal', command= lambda: set150cm(self))
            self.ihelemaal.grid(row=4,column=2)


            def isluit(self):

                del instellingenvenster_dict[self.nummer]
                self.instellingenvenstertje.destroy()
                Arduinotab.instellingenbordknop.state(["!disabled"])





            self.instellingenvenstertje.protocol("WM_DELETE_WINDOW", lambda:isluit(self))

    #maakt een tabblad aan voor een bordje
#oeuoeu
#    def nieuwebordje():
#        nieuwbordjetab()
#        metingen.leesnieuweport()

    def nieuwbordjetab():
        arduino = python.Arduino.scan()
#        for i in range(len(python.Arduino.arduinos)):
#            welkearduino = python.Arduino.arduinos[i]
        for i in python.Arduino.arduinos:
            Arduinotab(i)
#            Arduinotab(python.Arduino.get(i).nummer)

    def stuurcommando(welke, commando):
        return python.Arduino.get(welke).commandosturen(commando)

    def whilelooparduino(welke):
        python.Arduino.get(welke).whileloopmeting()

    def stuurnaaralle(commando):
        for k,v in python.Arduino.arduinos:
            python.Arduino.arduinos[k].commandosturen(commando)

    def comportopzetten(welke):
        python.Arduino.get(welke).openserial()

    class Arduinotab:

        def __init__(self,welkearduino):
            self.welkearduino = welkearduino
            self.comport = python.Arduino.get(welkearduino)
            print("arduinotab_printcomport: ",self.comport)
#            self.a = ( 1 + int(python.Arduino.get(self.welkearduino).nummer))
            self.a = (1 + welkearduino)
#            python.Arduino.get(self.welkearduino).openserial()
            self.nieuweframe = ttk.Frame(notebook, width=100, height=200)
            notebook.add(self.nieuweframe, text='Bord %d' % self.a)
            notebook.pack()
            self.bordlabel = ttk.Label(self.nieuweframe, text='Bord %d' % self.a)
            self.bordlabel.grid(row=0,column=0)
            self.bordsep1 = ttk.Separator(self.nieuweframe,orient="horizontal")
            self.bordsep1.grid(row=1,column=0,sticky='ew')
            self.bordsep2 = ttk.Separator(self.nieuweframe, orient="horizontal")
            self.bordsep2.grid(row=1, column=1, sticky='ew')
            self.bordsep3 = ttk.Separator(self.nieuweframe, orient="horizontal")
            self.bordsep3.grid(row=1, column=2, sticky='ew')
            self.borduitgeroldlabel1 = ttk.Label(self.nieuweframe, text ='Uitgerold:')
            self.borduitgeroldlabel1.grid(row=2,column=1)
            self.bordwhitespace1= ttk.Label(self.nieuweframe)
            self.bordwhitespace1.grid(row=4,column=1)
            self.bordgrafieklabel= ttk.Label(self.nieuweframe, text ='Grafiek')
            self.bordgrafieklabel.grid(row=5,column=1)
#            self.statusknop= ttk.Button(self.nieuweframe, text='Status opvragen', command = statusopvragen)
#            self.statusknop.grid(row=3, column = 1)
            self.uurknop= ttk.Button(self.nieuweframe,text='Uur', command = grafiekuur)
            self.uurknop.grid(row=6,column=0)
            self.dagknop= ttk.Button(self.nieuweframe,text='Dag', command = grafiekdag)
            self.dagknop.grid(row=6,column=1)
            self.weekknop= ttk.Button(self.nieuweframe,text='Week', command = grafiekweek)
            self.weekknop.grid(row=6,column=2)
            self.maandknop= ttk.Button(self.nieuweframe,text='Maand', command = grafiekmaand)
            self.maandknop.grid(row=7,column=0)
            self.jaarknop= ttk.Button(self.nieuweframe, text='Jaar', command = grafiekjaar)
            self.jaarknop.grid(row=7,column=1)
            self.bordwhitespace2 = ttk.Label(self.nieuweframe)
            self.bordwhitespace2.grid(row=8,column=1)
            self.bordsep4 = ttk.Separator(self.nieuweframe, orient="horizontal")
            self.bordsep4.grid(row=9,column=0,sticky='ew')
            self.bordsep5 = ttk.Separator(self.nieuweframe, orient="horizontal")
            self.bordsep5.grid(row=9, column=1,sticky='ew')
            self.bordsep6 = ttk.Separator(self.nieuweframe, orient="horizontal")
            self.bordsep6.grid(row=9, column=2,sticky='ew')
            self.inrolknop = ttk.Button(self.nieuweframe, text='Inrollen', command = lambda: stuurcommando(self.welkearduino, 4))
            self.inrolknop.grid(row=10,column=0)
            self.uitrolknop = ttk.Button(self.nieuweframe,text='Uitrollen', command = lambda: stuurcommando(self.welkearduino, 3))
            self.uitrolknop.grid(row=10,column=2)
            self.bordsep7 = ttk.Separator(self.nieuweframe, orient="horizontal")
            self.bordsep7.grid(row=11, column=0, sticky='ew')
            self.bordsep8 = ttk.Separator(self.nieuweframe, orient="horizontal")
            self.bordsep8.grid(row=11, column=1, sticky='ew')
            self.bordsep9 = ttk.Separator(self.nieuweframe, orient="horizontal")
            self.bordsep9.grid(row=11, column=2, sticky='ew')
            self.instellingenbordknop = ttk.Button(self.nieuweframe,text='Instellingen Bordje',command=lambda: instellingvensterenknop(self))
            self.instellingenbordknop.grid(row=12,column=1)
            self.bordwhitespace3 = ttk.Label(self.nieuweframe)
            self.bordwhitespace3.grid(row=13,column=1)
            self.sluitknop = ttk.Button(self.nieuweframe,text='Sluit tabblad',command=self.nieuweframe.destroy)
            self.sluitknop.grid(row=14,column=2)
            self.statusknop = ttk.Button(self.nieuweframe, text='Status opvragen',command=lambda: statusopvragenknop(self))
            self.statusknop.grid(row=3, column=1)
#            whilelooparduino(welkearduino)

            def instellingvensterenknop(self):
                instellingenvenster(self.welkearduino,self)
                self.instellingenbordknop.state(["disabled"])

            def statusopvragenknop(self):
                statusopvragen(self)
                self.statusknop.state(["disabled"])

    class statusopvragen:
        def __init__(self,Arduinotab):
            resultaat = stuurcommando(Arduinotab.welkearduino, 5)
            self.nummer = (1 + int(python.Arduino.get(Arduinotab.welkearduino).nummer))
            self.window = Tk()
            self.window.wm_title("Status")
            statusvenster_dict.update({self.nummer: self.window})
            self.label = ttk.Label(self.window, text="")
            self.label.grid(row=1, column=1)
            if resultaat == 3:
                self.label = ttk.Label(self.window, text = "Rolluik is omhoog")
                self.label.grid(row=1,column=1)
            elif resultaat == 4:
                self.label = ttk.Label(self.window, text = "Rolluik is omlaag")
                self.label.grid(row=1,column=1)
            else:
                self.label = ttk.Label(self.window, text = "Geen status gevonden")
                self.label.grid(row=1,column=1)

            def sluitstatus(self):
                del statusvenster_dict[self.nummer]
                Arduinotab.statusknop.state(["!disabled"])
                self.window.destroy()

            self.window.protocol("WM_DELETE_WINDOW", lambda: sluitstatus(self))



    root = Tk()
    root.wm_title('Centraal')

    maxrol= 150
    maxtemp= 25

    """""
    def setmaxtemp(waarde):
        main.maxtemp = waarde
        if(metingen.tempvalue >= waarde):
            metingen.arduino(4)
    """

    root.geometry("600x450+300+300")
    notebook = ttk.Notebook(root)
    centraalframe = ttk.Frame(notebook, width=100, height=200)
    notebook.add(centraalframe, text='Centraal')
    notebook.pack()
    #Grafiekknop = ttk.Button(centraalframe, text = "grafiek", command=grafiekminuut)
    #Grafiekknop.place(x=10,y=10)
    centraallabel = ttk.Label(centraalframe,text= 'Centraal')
    centraallabel.grid(row = 1, column = 1 )
    whitespace1 = ttk.Label(centraalframe)
    whitespace1.grid(row = 2, column = 1)
    sep1 = ttk.Separator(centraalframe, orient="horizontal")
    sep1.grid(row = 3, column = 1, sticky= 'ew')
    sep2 = ttk.Separator(centraalframe, orient="horizontal")
    sep2.grid(row=3, column=2, sticky='ew')
    sep3 = ttk.Separator(centraalframe, orient="horizontal")
    sep3.grid(row=3, column=0, sticky='ew')
    centraalbordenaan = ttk.Label(centraalframe, text='Aantal borden aan: %d' % python.Arduino.ardcount)
    centraalbordenaan.grid(row=4, column=1)
    whitespace2 = ttk.Label(centraalframe)
    whitespace2.grid(row=5,column=1)
    sep4 = ttk.Separator(centraalframe, orient="horizontal")
    sep4.grid(row = 6, column = 1, sticky= 'ew')
    sep5 = ttk.Separator(centraalframe, orient="horizontal")
    sep5.grid(row=6, column=2, sticky='ew')
    sep6 = ttk.Separator(centraalframe, orient="horizontal")
    sep6.grid(row=6, column=0, sticky='ew')
    whitespace3 = ttk.Label(centraalframe)
    whitespace3.grid(row=7,column=1)
    maxitemplabel = ttk.Label(centraalframe, text ='Maximale temperatuur(°C)')
    maxitemplabel.grid(row = 8, column = 0)
    maxirollabel = ttk.Label(centraalframe, text='Maximale uitrollengte(CM)')
    maxirollabel.grid(row = 8, column = 2)
    maxitempbox = ttk.Combobox(centraalframe)
    maxitempbox.grid(row = 9, column =0)
    maxirolbox = OptionMenu(centraalframe, maxrol, 50, 100, 150)
    maxirolbox.grid(row = 9, column =2)
    whitespace4 = ttk.Label(centraalframe)
    whitespace4.grid(row=10,column=1)
    leegmakenknop = ttk.Button(centraalframe,text='Leegmaken',command=lambda: maxitempbox.delete(0, 'end'))
    leegmakenknop.grid(row = 11, column = 0)
    #TODO: accepteren
    #accepterenknop = ttk.Button(centraalframe,text='Accepteren',command = setmaxtemp(maxitempbox.get()))
    #accepterenknop.grid(row=11,column=2)
#    accepterenknop = ttk.Button(centraalframe,text='Accepteren',command = setmaxtemp(maxitempbox.get()))
#    accepterenknop.grid(row=11,column=2)
    whitespace5 = ttk.Label(centraalframe)
    whitespace5.grid(row=12,column=1)
    sep7 = ttk.Separator(centraalframe, orient="horizontal")
    sep7.grid(row=13, column=0, sticky='ew')
    sep8 = ttk.Separator(centraalframe, orient="horizontal")
    sep8.grid(row=13, column=1, sticky='ew')
    sep9 = ttk.Separator(centraalframe, orient="horizontal")
    sep9.grid(row=13, column=2, sticky='ew')
    whitespace6 = ttk.Label(centraalframe)
    whitespace6.grid(row=14,column=1)

    openknop = ttk.Button(centraalframe,text='Alle luiken open', command=lambda: stuurnaaralle(3))
    openknop.grid(row=15, column=0)
    #TODO: Alle luiken sluiten
    sluitknop = ttk.Button(centraalframe,text='Alle luiken sluiten')
    sluitknop.grid(row=15,column=2)
    whitespace7 = ttk.Label(centraalframe)
    whitespace7.grid(row=16,column=1)
    sep10 = ttk.Separator(centraalframe, orient="horizontal")
    sep10.grid(row=17,column=0,sticky='ew')
    sep11 = ttk.Separator(centraalframe, orient="horizontal")
    sep11.grid(row=17, column=1,sticky='ew')
    sep12 = ttk.Separator(centraalframe, orient="horizontal")
    sep12.grid(row=17, column=2,sticky='ew')
    whitespace8 = ttk.Label(centraalframe)
    whitespace8.grid(row=18,column=1)
    nieuwbordknop = ttk.Button(centraalframe,text = 'Nieuw bordje aansluiten',command=nieuwbordjetab)
    nieuwbordknop.grid(row=19,column=1)
    whitespace9 = ttk.Label(centraalframe)
    whitespace9.grid(row=20,column=1)
#    meting = Label(root,textvariable=test())
#    meting.place(x=100,y=50)
#    meting.pack()
#    gui.addtab()
    def vraag():
        if messagebox.askokcancel("Stoppen", "Weet je zeker dat je wilt stoppen?"):
            root.destroy()
            for k,v in instellingenvenster_dict.items():

                v.destroy()
            for x,y in statusvenster_dict.items():

                y.destroy
            plt.close()
    root.protocol("WM_DELETE_WINDOW", vraag)
    root.mainloop()


if __name__ == '__main__':
    main()


