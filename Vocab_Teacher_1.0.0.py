import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from random import *

#interne Wörterbücher als Listen (ergeben eine virtuelle Tabelle)
Englisch = []
Deutsch = []
Deutsch_alt = []
Infinitiv = []
Simple_Past = []
Past_Participle = []

#Funktion für Tolleranz; Groß-/Kleinschreibung wird angepasst
def grossKlein(Text):
    Grossbuchstaben = ["A", "À", "B", "C", "Ç", "D", "E", "É", "È", "Ê", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    Kleinbuchstaben = ["a", "à", "b", "c", "ç", "d", "e", "é", "è", "ê", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    Ausgabe = ""
    for x in Text:
        if x in Grossbuchstaben:
            Ausgabe += Kleinbuchstaben[Grossbuchstaben.index(x)]
        else:
            Ausgabe += x
    return Ausgabe

#Funktion, die setup.txt in Liste überführt
Setup = []
def setupLaden():
    try:
        with open("files/setup.txt", "r", encoding =" utf-8") as f:
            for line in f:
                wort = line.split(" ")
                Setup.append(wort[0])
                Setup.append(wort[1])
    except FileNotFoundError:
        print("Setup-Datei konnte nicht geladen werden.")

#globale Funktionen, die Wörterbücher von der Datei (.txt) in die globalen Listen überführt
def vokabelnAbfrageLaden(file):

    del Englisch[:]
    del Deutsch[:]
    del Deutsch_alt[:]
    laden_erfolgreich = False

    try:
        with open(file, "r", encoding = "utf-8") as f:
            for line in f:
                wort = line.split(" ")
                #Englisch
                englisch = wort[0].strip()
                Englisch_Pruefung = []
                for x in englisch:
                    Englisch_Pruefung.append(x)
                englisch_wort = ""
                for x in Englisch_Pruefung:
                    if x == "_":
                        Englisch_Pruefung[Englisch_Pruefung.index(x)] = " "
                for x in Englisch_Pruefung:
                    englisch_wort += x
                #Deutsch
                deutsch = wort[1].strip()
                Deutsch_Pruefung = []
                for x in deutsch:
                    Deutsch_Pruefung.append(x)
                deutsch_wort = ""
                for x in Deutsch_Pruefung:
                    if x == "_":
                        Deutsch_Pruefung[Deutsch_Pruefung.index(x)] = " "
                for x in Deutsch_Pruefung:
                    deutsch_wort += x
                #Deutsch alternativ
                deutsch_alt = wort[2].strip("\n")
                if deutsch_alt == "--":
                    deutsch_wort_alt = " "
                else:
                    Deutsch_Pruefung_alt = []
                    for x in deutsch_alt:
                        Deutsch_Pruefung_alt.append(x)
                    deutsch_wort_alt = ""
                    for x in Deutsch_Pruefung_alt:
                        if x == "_":
                            Deutsch_Pruefung_alt[Deutsch_Pruefung_alt.index(x)] = " "
                    for x in Deutsch_Pruefung_alt:
                        deutsch_wort_alt += x
                #Einfügen der Vokabeln
                Englisch.append(englisch_wort)
                Deutsch.append(deutsch_wort)
                Deutsch_alt.append(deutsch_wort_alt)
        laden_erfolgreich = True
        return laden_erfolgreich
    except FileNotFoundError:
        laden_erfolgreich = False
        return laden_erfolgreich

def verbenLaden(file):

    del Infinitiv[:]
    del Simple_Past[:]
    del Past_Participle[:]
    laden_erfolgreich = False

    try:
        with open(file, "r", encoding = "utf-8") as f:
            for line in f:
                wort = line.split(" ")
                infinitiv = wort[0]
                simple_past = wort[1].strip()
                past_participle = wort[2].strip("\n")
                Infinitiv.append(infinitiv)
                Simple_Past.append(simple_past)
                Past_Participle.append(past_participle)
        laden_erfolgreich = True
        return laden_erfolgreich
    except FileNotFoundError:
        laden_erfolgreich = False
        return laden_erfolgreich

#Mitwirkende
class Mitwirkende(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI() #siehe unten
    def initializeUI(self):
        self.setGeometry(10, 30, 1200, 800) #Größe & Position des Fensters
        self.setWindowTitle("Mitwirkende") #Bezeichnung
        self.setWindowIcon(QIcon("images/union_jack.png"))
        self.setUpFenster() #siehe unten
    def setUpFenster(self):
        Titel_Label = QLabel("Mitwirkende")
        Titel_Label.setFont(QFont("Arial", 40))
        Titel_Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        text = "Die Beteiligten wollen unbekannt bleiben.\n"
        text += "Programmiersprache ('Chief Executive Snack'): Python 3.14.2 \n"
        text += "GUI erstellt mit: PyQt6 \n"
        text += "Union Jack: https://pixabay.com/de/vectors/union-jack-flagge-unions-flagge-26119/"
        Text_Label = QLabel(text)
        Text_Label.setFont(QFont("Arial", 18))
        Text_Label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.Ende_Knopf = QPushButton("zurück")
        self.Ende_Knopf.setStyleSheet("background-color: lightblue")
        self.Ende_Knopf.setFont(QFont("Arial", 16))
        self.Ende_Knopf.clicked.connect(self.ende)
        VBox = QVBoxLayout()
        VBox.addWidget(Titel_Label)
        VBox.addWidget(Text_Label)
        VBox.addWidget(self.Ende_Knopf, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(VBox)
        
    def ende(self):
        #print("Mitwirkende-Fenster wurde geschlossen.")
        self.hide()
        MenuFenster.show()

class Hilfefenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI() #siehe unten

    def initializeUI(self):
        self.setGeometry(10, 30, 1200, 800) #Größe des Fensters
        self.setWindowTitle("Hilfe") #Bezeichnung
        self.setWindowIcon(QIcon("images/union_jack.png"))
        self.setUpFenster() #siehe unten

    def setUpFenster(self):
        #Titeltext
        Titel_Label = QLabel("Hilfe")
        Titel_Label.setFont(QFont("Arial", 36))
        Titel_Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        intro = "Auf dieser Seite werden für den Nutzer relevante technische Besonderheiten und Fehlerquellen erklärt.\n"
        intro += "Bei besonders anfälligen Stellen finden sich auch 'Hilfe/Anleitung-Knöpfe', die die gleichen Texte enthalten.\n"
        intro += "Sollten Fragen oder Probleme auftreten, hilft der Entwickler gerne."
        Einleitungs_Text = QLabel(intro)
        Einleitungs_Text.setFont(QFont("Arial", 15))
        Einleitungs_Text.setWordWrap(True)
        Einleitungs_Text.setAlignment(Qt.AlignmentFlag.AlignLeft)

        vm_text = "Im Vokabelmenü können .txt-Datei als Wörterbücher ausgewählt werden, indem man den Namen der Datei in das Feld eingibt.\n"
        vm_text += "Achtung: Der vollständige Dateiname (also mit Datentyp .txt) muss angegeben werden, weil sie sonst nicht geladen werden kann.\n"
        vm_text += "Außerdem muss die Datei im Arbeitsverzeichnis gespeichert werden. Das ist in diesem Fall das Verzeichnis mit der .exe-Datei für dieses Programm.\n"
        vm_text += "Die ausgewählte Datei muss per Knopfdruck bestätigt werden, damit sie geladen wird.\n"
        vm_text += "Für Deutsch-Englisch und Englisch-Deutsch wird die gleiche Datei verwendet und wird unter 'einfache Abfrage' eingegeben."
        VM_Text = QLabel(vm_text)
        VM_Text.setFont(QFont("Arial", 15))
        VM_Text.setWordWrap(True)
        VM_Text.setAlignment(Qt.AlignmentFlag.AlignLeft)

        ve_text = "Gib in der Textzeile des Editors den Namen der Datei nach dem Schema '[Dateiname].txt' ein, die geladen werden soll.\n"
        ve_text += "Falls es eine Datei mit dem Namen nicht geben sollte, wird sie automatisch beim Speichern erstellt.\n"
        ve_text += "Der bereits bestehende Text wird nach dem Laden im Schreibbereich angezeigt und kann bearbeitet werden.\n"
        ve_text += "Achte auf das richtige Schema bei der Eingabe.\nBei Vokabeln für die einfache Abfrage gilt: "
        ve_text += "[Englisch] [Deutsch] [alternatives Wort auf Deutsch].\n"
        ve_text += "Falls es kein Wort für etwas gibt, schreib '--'. Dies ist aus technischen Gründen notwendig.\n"
        ve_text += "Bei Dateien für die irregulären Verben gilt: [Infinitive] [Simple Past] [Past Participle]."
        VE_Text = QLabel(ve_text)
        VE_Text.setFont(QFont("Arial", 15))
        VE_Text.setWordWrap(True)
        VE_Text.setAlignment(Qt.AlignmentFlag.AlignLeft)

        absturz = "Abstürze des Programms können aus verschiedenen Gründen auftreten. Hier werden kurz die wahrscheinlichsten Probleme erklärt.\n"
        absturz += "Wenn man selbst erstellte Dateien als Wörterbücher verwendet, ist es möglich, dass sie zum Absturz führen, wenn das Schema"
        absturz += " nicht genau eingehalten wurde.\nSiehe hierfür auch den Hilfe-Text für den Editor."
        absturz += " Auch muss man darauf achten, diese Dateien im Arbeitsverzeichnis zu speichern.\n"
        absturz += "Wenn die .zip-Datei nicht ausgepackt wird, kann es zu Problemen kommen."
        Absturz_Text = QLabel(absturz)
        Absturz_Text.setFont(QFont("Arial", 15))
        Absturz_Text.setWordWrap(True)
        Absturz_Text.setAlignment(Qt.AlignmentFlag.AlignLeft)

        Seite_Combo = QComboBox()
        Seite_Combo.setFont(QFont("Arial", 15))
        Seite_Combo.addItems(["Einleitung", "Vokabelmenü", "Vokabeleditor", "Absturz"])
        Seite_Combo.activated.connect(self.seiteAnpassen)

        self.Ende_Knopf = QPushButton("zurück")
        self.Ende_Knopf.setFont(QFont("Arial", 16))
        self.Ende_Knopf.setStyleSheet("background-color: lightblue")
        self.Ende_Knopf.clicked.connect(self.ende)

        #Layout
        self.Stacked = QStackedLayout()
        self.Stacked.addWidget(Einleitungs_Text)
        self.Stacked.addWidget(VM_Text)
        self.Stacked.addWidget(VE_Text)
        self.Stacked.addWidget(Absturz_Text)

        VBox = QVBoxLayout()
        VBox.addWidget(Titel_Label)
        VBox.addWidget(Seite_Combo)
        VBox.addLayout(self.Stacked)
        VBox.addWidget(self.Ende_Knopf, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(VBox)

    def seiteAnpassen(self, index):
        self.Stacked.setCurrentIndex(index)

    def ende(self):
        self.hide()
        MenuFenster.show()

#Startfenster
class Startfenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI() #siehe unten

    def initializeUI(self):
        self.setGeometry(10, 30, 1200, 800) #Größe des Fensters
        self.setWindowTitle("Start") #Bezeichnung
        self.setWindowIcon(QIcon("images/union_jack.png"))
        self.setUpFenster() #siehe unten
        self.show() #zeigt sich selbst

    def setUpFenster(self):
        #Titeltext
        Titel_Label = QLabel("Vocab Teacher")
        Titel_Label.setFont(QFont("Arial", 44))
        Titel_Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        #Version
        Version_Label = QLabel("Version 0.0.0.0")
        Version_Label.setFont(QFont("Arial", 18))
        Version_Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        #Startknopf
        self.Start_Knopf = QPushButton()
        self.Start_Knopf.clicked.connect(self.start)
        image = "images/Start.png" #Nicht richtig; muss 'Start.png' heißen. Bild wird nicht richtig positioniert.
        try:
            with open(image):
                Bild = QIcon(image)
                self.Start_Knopf.setIcon(Bild)
                self.Start_Knopf.setIconSize(QSize(90, 90))
                self.Start_Knopf.setFixedSize(QSize(100, 100))
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
            print("Das Bild Start.png wurde nicht gefunden.")
            self.Start_Knopf.setText("Start")
            self.Start_Knopf.setFont(QFont("Arial", 18))
            self.Start_Knopf.setFixedSize(QSize(100, 35))

        H_Box = QHBoxLayout() #Layout-Klasse
        D_Flagge_Label = QLabel()
        D_Flagge_Label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        H_Box.addWidget(D_Flagge_Label)
        V_Box = QVBoxLayout()
        V_Box.addWidget(Titel_Label)
        V_Box.addWidget(Version_Label)
        H_Box.addLayout(V_Box)
        image = "images/Allemagne.png"
        try:
            with open(image):
                pixmap = QPixmap(image).scaled(300,200)
                transform = QTransform()
                transform.rotate(0)
                rotated_pixmap = pixmap.transformed(transform)
                D_Flagge_Label.setPixmap(rotated_pixmap)
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
            print("Das Bild Allemagne.png wurde nicht gefunden.")

        F_Flagge_Label = QLabel()
        F_Flagge_Label.setAlignment(Qt.AlignmentFlag.AlignRight)
        H_Box.addWidget(F_Flagge_Label)
        image = "images/union_jack.png"
        try:
            with open(image):
                pixmap = QPixmap(image).scaled(300,200)
                transform = QTransform()
                transform.rotate(0)
                rotated_pixmap = pixmap.transformed(transform)
                F_Flagge_Label.setPixmap(rotated_pixmap)
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
            print("Das Bild unions_jack.png wurde nicht gefunden.")
        V_Box = QVBoxLayout()
        V_Box.addLayout(H_Box)
        V_Box.addWidget(self.Start_Knopf, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(V_Box)
    
    def start(self):
        #print("Startfenster wurde geschlossen.")
        self.hide()
        MenuFenster.show()

class Menufenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI() #siehe unten
    def initializeUI(self):
        self.setGeometry(10, 30, 1200, 800) #Größe des Fensters
        self.setWindowTitle("Hauptmenü") #Bezeichnung
        self.setWindowIcon(QIcon("images/union_jack.png"))
        self.setUpFenster() #siehe unten
    def setUpFenster(self):
        #Oberflächenelemente

        #Titeltext
        Titel_Label = QLabel("Hauptmenü")
        Titel_Label.setFont(QFont("Arial", 44))
        Titel_Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        Abfrage_Label = QLabel("Abfrage-Modi")
        Abfrage_Label.setFont(QFont("Arial", 20))
        Abfrage_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        Weiteres_Label = QLabel("Weiteres")
        Weiteres_Label.setFont(QFont("Arial", 20))
        Weiteres_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.VM_Knopf = QPushButton("Vokabelmenü")
        self.VM_Knopf.setFont(QFont("Arial", 16))
        self.VM_Knopf.setStyleSheet("background-color: lightblue")
        self.VM_Knopf.clicked.connect(self.vm)
        self.VE_Knopf = QPushButton("Vokabeleditor")
        self.VE_Knopf.setFont(QFont("Arial", 16))
        self.VE_Knopf.setStyleSheet("background-color: lightblue")
        self.VE_Knopf.clicked.connect(self.ve)
        self.DE_Knopf = QPushButton("Deutsch-Englisch")
        self.DE_Knopf.setFixedWidth(220)
        self.DE_Knopf.setFont(QFont("Arial", 16))
        self.DE_Knopf.clicked.connect(self.de)
        self.DE_Knopf.setStyleSheet("background-color: lightblue")
        self.ED_Knopf = QPushButton("Englisch-Deutsch")
        self.ED_Knopf.setFixedWidth(220)
        self.ED_Knopf.setFont(QFont("Arial", 16))
        self.ED_Knopf.setStyleSheet("background-color: lightblue")
        self.ED_Knopf.clicked.connect(self.ed)
        self.Verb_Knopf = QPushButton("unregelmäßgie\nVerben")
        self.Verb_Knopf.setFixedWidth(220)
        self.Verb_Knopf.setFont(QFont("Arial", 16))
        self.Verb_Knopf.setStyleSheet("background-color: lightblue")
        self.Verb_Knopf.clicked.connect(self.verben)

        self.Hilfe_Knopf = QPushButton("Hilfe")
        self.Hilfe_Knopf.setFont(QFont("Arial", 16))
        self.Hilfe_Knopf.setStyleSheet("background-color: lightblue")
        self.Hilfe_Knopf.setFixedWidth(70)
        self.Hilfe_Knopf.clicked.connect(self.hilfe)
        self.Credits_Knopf = QPushButton("Mitwirkende")
        self.Credits_Knopf.setFont(QFont("Arial", 16))
        self.Credits_Knopf.setStyleSheet("background-color: lightblue")
        self.Credits_Knopf.setFixedWidth(130)
        self.Credits_Knopf.clicked.connect(self.credits)
        self.Beenden_Knopf = QPushButton("Programm beenden")
        self.Beenden_Knopf.setFont(QFont("Arial", 16))
        self.Beenden_Knopf.setStyleSheet("background-color: lightblue")
        self.Beenden_Knopf.clicked.connect(self.beenden)

        #Layout
        V_Box_Haupt = QVBoxLayout()
        V_Box_Haupt.addWidget(Titel_Label)
        V_Box_1 = QVBoxLayout()
        V_Box_1.addWidget(Abfrage_Label)
        V_Box_1.addWidget(self.DE_Knopf)
        V_Box_1.addWidget(self.ED_Knopf)
        V_Box_1.addWidget(self.Verb_Knopf)
        V_Box_2 = QVBoxLayout()
        V_Box_2.addWidget(Weiteres_Label)
        V_Box_2.addWidget(self.VM_Knopf)
        V_Box_2.addWidget(self.VE_Knopf)
        V_Box_2.addWidget(self.Hilfe_Knopf)
        V_Box_2.addWidget(self.Credits_Knopf)
        H_Box_1 = QHBoxLayout()
        H_Box_1.addLayout(V_Box_1)
        H_Box_1.addLayout(V_Box_2)
        V_Box_Haupt.addLayout(H_Box_1)
        V_Box_Haupt.addWidget(self.Beenden_Knopf, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(V_Box_Haupt)

    def vm(self):
        self.hide()
        VM.show()
    def ve(self):
        self.hide()
        VE.show()
    def ed(self):
        EDF.show()
    def de(self):
        self.hide()
        DEF.show()
    def verben(self):
        self.hide()
        VF.show()
    def credits(self):
        self.hide()
        Credits.show()
    def hilfe(self):
        self.hide()
        Hilfe.show()

    def beenden(self):
        print("Programm beendet.")
        self.close()

#Deutsch-Englisch
class Deutsch_Englisch(QWidget):
    gestartet = False
    vokabeln = []
    vokabel_index = 0
    def __init__(self):
        super().__init__()
        self.initializeUI()
    def initializeUI(self):
        self.setGeometry(10, 30, 1200, 800)
        self.setWindowTitle("Deutsch-Englisch-Abfrage")
        self.setWindowIcon(QIcon("images/union_jack.png"))
        self.setUpFenster()
    def setUpFenster(self):
        #Oberflächenelemente

        #Titel
        Titel_Label = QLabel("Deutsch-Englisch")
        Titel_Label.setFont(QFont("Arial", 36))
        Titel_Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        #Anzeige der zu übersetzenden Vokabel
        self.Wort_Label = QLabel()
        self.Wort_Label.setFont(QFont("Arial", 15))

        #Anzeige-Label (fix)
        Deutsch_Label = QLabel("Deutsch:")
        Deutsch_Label.setFont(QFont("Arial", 15))
        Englisch_Label = QLabel("Englisch:")
        Englisch_Label.setFont(QFont("Arial", 15))
        R_F_Label = QLabel("Richtig/Falsch:")
        R_F_Label.setFont(QFont("Arial", 15))
        Rueckmeldungs_Label = QLabel("Rückmeldung:")
        Rueckmeldungs_Label.setFont(QFont("Arial", 15))

        #Felder für Rückmeldung
        self.Richtig_Falsch_Label = QLabel() #richtig/falsch
        self.Richtig_Falsch_Label.setFont(QFont("Arial", 15))
        self.Rueckmeldung_Label = QLabel() #mehr Details zu Fehler
        self.Rueckmeldung_Label.setFont(QFont("Arial", 15))

        #Eingabefelder
        self.Eingabe_Edit = QLineEdit()
        self.Eingabe_Edit.setFont(QFont("Arial", 16))
        self.Eingabe_Edit.setFixedWidth(300)
        self.Eingabe_Edit.setClearButtonEnabled(True)
        self.Eingabe_Edit.setEnabled(False)

        #Startknopf
        self.Start_Knopf = QPushButton()
        image = "images/Start.png"
        try:
            with open(image):
                Bild = QIcon(image)
                self.Start_Knopf.setIcon(Bild)
                self.Start_Knopf.setIconSize(QSize(60, 60))
                self.Start_Knopf.setFixedSize(QSize(75, 75))
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
            print("Das Bild Start.png wurde nicht gefunden.")
            self.Start_Knopf.setText("Start")
            self.Start_Knopf.setFont(QFont("Arial", 18))
            self.Start_Knopf.setFixedSize(QSize(80, 30))
        self.Start_Knopf.clicked.connect(self.start)

        #Bestätigenknopf; löst Prüfung (Methode) aus
        self.Bestaetigen_Knopf = QPushButton("bestätigen")
        self.Bestaetigen_Knopf.setFont(QFont("Arial", 16))
        self.Bestaetigen_Knopf.setFixedSize(QSize(120, 30))
        self.Bestaetigen_Knopf.clicked.connect(self.startPruefung)
        self.Bestaetigen_Knopf.setEnabled(False)
        self.Bestaetigen_Knopf.setStyleSheet("background-color: lightblue")

        #Weitetknopf; nächste Vokabel wird angezeigt; Lösung, um Verbesserungen anbringen zu können
        self.Weiter_Knopf = QPushButton("weiter")
        self.Weiter_Knopf.setFont(QFont("Arial", 16))
        self.Weiter_Knopf.setFixedSize(QSize(80, 30))
        self.Weiter_Knopf.clicked.connect(self.weiter)
        self.Weiter_Knopf.setEnabled(False)
        self.Weiter_Knopf.setStyleSheet("background-color: lightblue")

        #man kehrt ins voherige Menü zurück
        self.Ende_Knopf = QPushButton("beenden")
        self.Ende_Knopf.setFont(QFont("Arial", 16))
        self.Ende_Knopf.setFixedSize(QSize(100, 30))
        self.Ende_Knopf.clicked.connect(self.ende)
        self.Ende_Knopf.setStyleSheet("background-color: lightblue")

        #Layout
        Haupt_VBox = QVBoxLayout()
        Form = QFormLayout()
        Haupt_VBox.addWidget(Titel_Label)
        Form.addRow(Deutsch_Label, self.Wort_Label)
        Form.addRow(Englisch_Label, self.Eingabe_Edit)
        Form.addRow(R_F_Label, self.Richtig_Falsch_Label)
        Form.addRow(Rueckmeldungs_Label, self.Rueckmeldung_Label)
        Haupt_VBox.addLayout(Form)
        HBox = QHBoxLayout()
        HBox.addWidget(self.Bestaetigen_Knopf)
        HBox.addWidget(self.Weiter_Knopf)
        Haupt_VBox.addLayout(HBox)
        Haupt_VBox.addWidget(self.Start_Knopf, alignment=Qt.AlignmentFlag.AlignCenter)
        Haupt_VBox.addWidget(self.Ende_Knopf, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(Haupt_VBox)

        #Tastenkombination
        self.shortcut = QShortcut(QKeySequence("Return"), self)
        self.shortcut.activated.connect(self.startPruefung)

    #Methoden
    def start(self):
        if self.gestartet == False:
            for x in range(0, len(Deutsch)):
                self.vokabeln.append(x)
            shuffle(self.vokabeln)
            if Deutsch_alt[self.vokabeln[self.vokabel_index]] == " ":
                text = Deutsch[self.vokabeln[self.vokabel_index]]
            else:
                text = Deutsch[self.vokabeln[self.vokabel_index]] + " oder " + Deutsch_alt[self.vokabeln[self.vokabel_index]]
            self.Wort_Label.setText(text)
            self.Eingabe_Edit.setEnabled(True)
            self.Bestaetigen_Knopf.setEnabled(True)
            self.Weiter_Knopf.setEnabled(True)
            self.Eingabe_Edit.setFocus()
            self.gestartet = True

    def startPruefung(self):
        self.pruefen(Englisch, Deutsch, Deutsch_alt)
    def pruefen(self, Englisch, Deutsch, Deutsch_alt):
        uebersetzung = self.Eingabe_Edit.text()
        rueckmeldung = ""
        if uebersetzung == Englisch[self.vokabeln[self.vokabel_index]]:
            self.Richtig_Falsch_Label.setText("Die Vokabel ist richtig!")
        else:
            self.Richtig_Falsch_Label.setText("Die Vokabel ist falsch!")
            rueckmeldung += "Richtig wäre: " + Englisch[self.vokabeln[self.vokabel_index]]
        if rueckmeldung == "":
            rueckmeldung = "Keine Fehler!"
        self.Rueckmeldung_Label.setText(rueckmeldung)
        
    def weiter(self):
        self.Eingabe_Edit.clear()
        self.Richtig_Falsch_Label.clear()
        self.Rueckmeldung_Label.clear()
        self.vokabel_index += 1
        if (len(Englisch)-1) >= self.vokabel_index:
            if Deutsch_alt[self.vokabeln[self.vokabel_index]] == " ":
                text = Deutsch[self.vokabeln[self.vokabel_index]]
            else:
                text = Deutsch[self.vokabeln[self.vokabel_index]] + " oder " + Deutsch_alt[self.vokabeln[self.vokabel_index]]
            self.Wort_Label.setText(text)
            self.Eingabe_Edit.setFocus()
        else:
            self.Wort_Label.setText("Alle Vokabeln wurden abgefragt.")
            self.Eingabe_Edit.setEnabled(False)
            self.Bestaetigen_Knopf.setEnabled(False)
            self.Weiter_Knopf.setEnabled(False)
            self.vokabeln = []
            self.vokabel_index = 0
            self.gestartet = False
    
    def ende(self):
        #print("Deutsch-Englisch-Abfrage beendet und Fenster geschlossen.")
        self.hide()
        MenuFenster.show()

#Französisch-Deutsch
class Englisch_Deutsch(QWidget):
    gestartet = False
    vokabeln = []
    vokabel_index = 0
    def __init__(self):
        super().__init__()
        self.initializeUI()
    def initializeUI(self):
        self.setGeometry(10, 30, 1200, 800)
        self.setWindowTitle("Englisch-Deutsch-Abfrage")
        self.setWindowIcon(QIcon("images/union_jack.png"))
        self.setUpFenster()
    def setUpFenster(self):
        #Oberflächenelemente

        #Titel
        Titel_Label = QLabel("Englisch-Deutsch")
        Titel_Label.setFont(QFont("Arial", 36))
        Titel_Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        #Anzeige der zu übersetzenden Vokabel
        self.Wort_Label = QLabel()
        self.Wort_Label.setFont(QFont("Arial", 15))

        #Anzeige-Label (fix)
        Deutsch_Label = QLabel("Englisch:")
        Deutsch_Label.setFont(QFont("Arial", 15))
        Franzoesisch_Label = QLabel("Deutsch:")
        Franzoesisch_Label.setFont(QFont("Arial", 15))
        R_F_Label = QLabel("Richtig/Falsch:")
        R_F_Label.setFont(QFont("Arial", 15))
        Rueckmeldungs_Label = QLabel("Rückmeldung:")
        Rueckmeldungs_Label.setFont(QFont("Arial", 15))

        #Felder für Rückmeldung
        self.Richtig_Falsch_Label = QLabel() #richtig/falsch
        self.Richtig_Falsch_Label.setFont(QFont("Arial", 15))
        self.Rueckmeldung_Label = QLabel() #mehr Details zu Fehler
        self.Rueckmeldung_Label.setFont(QFont("Arial", 15))

        #Eingabefelder
        self.Eingabe_Edit = QLineEdit()
        self.Eingabe_Edit.setFont(QFont("Arial", 16))
        self.Eingabe_Edit.setFixedWidth(300)
        self.Eingabe_Edit.setClearButtonEnabled(True)
        self.Eingabe_Edit.setEnabled(False)

        #Startknopf
        self.Start_Knopf = QPushButton()
        image = "images/Start.png" #Nicht richtig; muss 'Start.png' heißen. Bild wird nicht richtig positioniert.
        try:
            with open(image):
                Bild = QIcon(image)
                self.Start_Knopf.setIcon(Bild)
                self.Start_Knopf.setIconSize(QSize(60, 60))
                self.Start_Knopf.setFixedSize(QSize(75, 75))
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
            print("Das Bild Start.png wurde nicht gefunden.")
            self.Start_Knopf.setText("Start")
            self.Start_Knopf.setFont(QFont("Arial", 18))
            self.Start_Knopf.setStyleSheet("background-color: lightblue")
            self.Start_Knopf.setFixedSize(QSize(80, 30))
        self.Start_Knopf.clicked.connect(self.start)

        #Bestätigenknopf; löst Prüfung (Methode) aus
        self.Bestaetigen_Knopf = QPushButton("bestätigen")
        self.Bestaetigen_Knopf.setFont(QFont("Arial", 16))
        self.Bestaetigen_Knopf.setFixedSize(QSize(120, 30))
        self.Bestaetigen_Knopf.clicked.connect(self.startPruefung)
        self.Bestaetigen_Knopf.setEnabled(False)
        self.Bestaetigen_Knopf.setStyleSheet("background-color: lightblue")

        #Weitetknopf; nächste Vokabel wird angezeigt; Lösung, um Verbesserungen anbringen zu können
        self.Weiter_Knopf = QPushButton("weiter")
        self.Weiter_Knopf.setFont(QFont("Arial", 16))
        self.Weiter_Knopf.setFixedSize(QSize(80, 30))
        self.Weiter_Knopf.clicked.connect(self.weiter)
        self.Weiter_Knopf.setEnabled(False)
        self.Weiter_Knopf.setStyleSheet("background-color: lightblue")

        #man kehrt ins voherige Menü zurück
        self.Ende_Knopf = QPushButton("beenden")
        self.Ende_Knopf.setFont(QFont("Arial", 16))
        self.Ende_Knopf.setFixedSize(QSize(100, 30))
        self.Ende_Knopf.clicked.connect(self.ende)
        self.Ende_Knopf.setStyleSheet("background-color: lightblue")

        #Layout
        Haupt_VBox = QVBoxLayout()
        Form = QFormLayout()
        Haupt_VBox.addWidget(Titel_Label)
        Form.addRow(Deutsch_Label, self.Wort_Label)
        Form.addRow(Franzoesisch_Label, self.Eingabe_Edit)
        Form.addRow(R_F_Label, self.Richtig_Falsch_Label)
        Form.addRow(Rueckmeldungs_Label, self.Rueckmeldung_Label)
        Haupt_VBox.addLayout(Form)
        HBox = QHBoxLayout()
        HBox.addWidget(self.Bestaetigen_Knopf)
        HBox.addWidget(self.Weiter_Knopf)
        Haupt_VBox.addLayout(HBox)
        Haupt_VBox.addWidget(self.Start_Knopf, alignment=Qt.AlignmentFlag.AlignCenter)
        Haupt_VBox.addWidget(self.Ende_Knopf, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(Haupt_VBox)

        #Tastenkombination
        self.shortcut = QShortcut(QKeySequence("Return"), self)
        self.shortcut.activated.connect(self.startPruefung)

    #Methoden
    def start(self):
        if self.gestartet == False:
            for x in range(0, len(Deutsch)):
                self.vokabeln.append(x)
            shuffle(self.vokabeln)
            text = Englisch[self.vokabeln[self.vokabel_index]]
            self.Wort_Label.setText(text)
            self.Eingabe_Edit.setEnabled(True)
            self.Bestaetigen_Knopf.setEnabled(True)
            self.Weiter_Knopf.setEnabled(True)
            self.Eingabe_Edit.setFocus()
            self.gestartet = True

    def startPruefung(self):
        self.pruefen(Englisch, Deutsch, Deutsch_alt)
    def pruefen(self, Englisch, Deutsch, Deutsch_alt):
        uebersetzung = self.Eingabe_Edit.text()
        try:
            rueckmeldung = ""
            if Deutsch_alt[self.vokabeln[self.vokabel_index]] == " ":
                if uebersetzung == Deutsch[self.vokabeln[self.vokabel_index]]:
                    self.Richtig_Falsch_Label.setText("Die Vokabel ist richtig!")
                else:
                    vokabel = grossKlein(Deutsch[self.vokabeln[self.vokabel_index]])
                    uebersetzung = grossKlein(uebersetzung)
                    if uebersetzung == vokabel:
                        self.Richtig_Falsch_Label.setText("Die Vokabel ist fast richtig!")
                        rueckmeldung += "Beachte die Groß-/Kleinschreibung."
                    else:
                        self.Richtig_Falsch_Label.setText("Die Vokabel ist falsch!")
                        rueckmeldung += "Richt wäre: " + Deutsch[self.vokabeln[self.vokabel_index]]
            else:
                if uebersetzung == Deutsch[self.vokabeln[self.vokabel_index]] or uebersetzung == Deutsch_alt[self.vokabeln[self.vokabel_index]]:
                    self.Richtig_Falsch_Label.setText("Die Vokabel ist richtig!")
                else:
                    vokabel = grossKlein(Deutsch[self.vokabeln[self.vokabel_index]])
                    vokabel_alt = grossKlein(Deutsch_alt[self.vokabeln[self.vokabel_index]])
                    uebersetzung = grossKlein(uebersetzung)
                    if uebersetzung == vokabel or uebersetzung == vokabel_alt:
                        self.Richtig_Falsch_Label.setText("Die Vokabel ist fast richtig!")
                        rueckmeldung += "Beachte die Groß-/Kleinschreibung."
                    else:
                        self.Richtig_Falsch_Label.setText("Die Vokabel ist falsch!")
                        rueckmeldung += "Richtig wäre: " + Deutsch[self.vokabeln[self.vokabel_index]] + " oder " + Deutsch_alt[self.vokabeln[self.vokabel_index]]
            if rueckmeldung == "":
                rueckmeldung = "Keine Fehler!"
            self.Rueckmeldung_Label.setText(rueckmeldung)
        except IndexError:
            print("Fehler bei Prüfung")
        
    def weiter(self):
        self.Eingabe_Edit.clear()
        self.Richtig_Falsch_Label.clear()
        self.Rueckmeldung_Label.clear()
        self.vokabel_index += 1
        if (len(Deutsch)-1) >= self.vokabel_index:
            text = Englisch[self.vokabeln[self.vokabel_index]]
            self.Wort_Label.setText(text)
            self.Eingabe_Edit.setFocus()
        else:
            self.Wort_Label.setText("Alle Vokabeln wurden abgefragt.")
            self.Eingabe_Edit.setEnabled(False)
            self.Bestaetigen_Knopf.setEnabled(False)
            self.Weiter_Knopf.setEnabled(False)
            self.gestartet = False
            self.vokabeln = []
            self.vokabel_index = 0

    def ende(self):
        #print("Französisch-Deutsch-Abfrage beendet und Fenster geschlossen.")
        self.hide()
        MenuFenster.show()

class Verbenfenster(QWidget):
    gestartet = False
    vokabeln = []
    vokabel_index = 0
    def __init__(self):
        super().__init__()
        self.initializeUI()
    def initializeUI(self):
        self.setGeometry(10, 30, 1200, 800)
        self.setWindowTitle("Abfrage unregelmäßiger Verben")
        self.setWindowIcon(QIcon("images/union_jack.png"))
        self.setup()
    def setup(self):
        #Oberflächenelemente

        #Titel
        Titel_Label = QLabel("unregelmäßige Verben")
        Titel_Label.setFont(QFont("Arial", 36))
        Titel_Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        #Anzeige der zu übersetzenden Vokabel
        self.Wort_Label = QLabel()
        self.Wort_Label.setFont(QFont("Arial", 15))

        #Anzeige-Labels (fix)
        Eingabe_Anzeige_Label = QLabel("Eingabe")
        Eingabe_Anzeige_Label.setFont(QFont("Arial", 15))
        Infinitiv_Label = QLabel("Infinitiv:")
        Infinitiv_Label.setFont(QFont("Arial", 15))
        Simple_Past_Label = QLabel("Simple Past:")
        Simple_Past_Label.setFont(QFont("Arial", 15))
        Past_Participle_Label = QLabel("Past Participle:")
        Past_Participle_Label.setFont(QFont("Arial", 15))
        R_F_Anzeige_Label = QLabel("Richtig/Falsch:")
        R_F_Anzeige_Label.setFont(QFont("Arial", 15))
        Rueckmeldungs_Anzeige_Label = QLabel("Rückmeldung:")
        Rueckmeldungs_Anzeige_Label.setFont(QFont("Arial", 15))

        #Info_Label für Anweisung und Meldung, wenn alle Verben abgefragt worden sind
        self.Info_Label = QLabel("Unten erscheint, nachdem du 'Start' gedrückt hast, ein Verb. Schreibe in jede Zeile die angepasste Form und drücke auf\n'bestätigen', wenn alle Formen eingetragen sind.")
        self.Info_Label.setFont(QFont("Arial", 16))
        self.Info_Label.setWordWrap(True)

        #Felder für Rückmeldung
        self.Infinitiv_Richtig_Falsch_Label = QLabel() #richtig/falsch
        self.Infinitiv_Richtig_Falsch_Label.setFont(QFont("Arial", 15))
        self.Infinitiv_Rueckmeldung_Label = QLabel() #mehr Details zu Fehler
        self.Infinitiv_Rueckmeldung_Label.setFont(QFont("Arial", 15))

        self.Simple_Past_Richtig_Falsch_Label = QLabel()
        self.Simple_Past_Richtig_Falsch_Label.setFont(QFont("Arial", 15))
        self.Simple_Past_Rueckmeldung_Label = QLabel()
        self.Simple_Past_Rueckmeldung_Label.setFont(QFont("Arial", 15))

        self.Past_Participle_Richtig_Falsch_Label = QLabel()
        self.Past_Participle_Richtig_Falsch_Label.setFont(QFont("Arial", 15))
        self.Past_Participle_Rueckmeldung_Label = QLabel()
        self.Past_Participle_Rueckmeldung_Label.setFont(QFont("Arial", 15))

        #Eingabefelder
        self.Infinitiv_Edit = QLineEdit()
        self.Infinitiv_Edit.setFont(QFont("Arial", 16))
        self.Infinitiv_Edit.setFixedWidth(400)
        self.Infinitiv_Edit.setClearButtonEnabled(True)
        self.Infinitiv_Edit.setEnabled(False)

        self.Simple_Past_Edit = QLineEdit()
        self.Simple_Past_Edit.setFont(QFont("Arial", 16))
        self.Simple_Past_Edit.setFixedWidth(400)
        self.Simple_Past_Edit.setClearButtonEnabled(True)
        self.Simple_Past_Edit.setEnabled(False)

        self.Past_Participle_Edit = QLineEdit()
        self.Past_Participle_Edit.setFont(QFont("Arial", 16))
        self.Past_Participle_Edit.setFixedWidth(400)
        self.Past_Participle_Edit.setClearButtonEnabled(True)
        self.Past_Participle_Edit.setEnabled(False)

        #Startknopf
        self.Start_Knopf = QPushButton()
        image = "images/Start.png"
        try:
            with open(image):
                Bild = QIcon(image)
                self.Start_Knopf.setIcon(Bild)
                self.Start_Knopf.setIconSize(QSize(60, 60))
                self.Start_Knopf.setFixedSize(QSize(75, 75))
        except FileNotFoundError as error:
            print(f"Image not found. \nError: {error}")
            print("Das Bild Start.png wurde nicht gefunden.")
            self.Start_Knopf.setText("Start")
            self.Start_Knopf.setFont(QFont("Arial", 18))
            self.Start_Knopf.setFixedSize(QSize(80, 30))
        self.Start_Knopf.clicked.connect(self.start)

        #Bestätigenknopf; löst Prüfung (Methode) aus
        self.Bestaetigen_Knopf = QPushButton("bestätigen")
        self.Bestaetigen_Knopf.setFont(QFont("Arial", 16))
        self.Bestaetigen_Knopf.setFixedSize(QSize(120, 30))
        self.Bestaetigen_Knopf.clicked.connect(self.startPruefung)
        self.Bestaetigen_Knopf.setEnabled(False)
        self.Bestaetigen_Knopf.setStyleSheet("background-color: lightblue")

        #Weitetknopf; nächste Vokabel wird angezeigt; Lösung, um Verbesserungen anbringen zu können
        self.Weiter_Knopf = QPushButton("weiter")
        self.Weiter_Knopf.setFont(QFont("Arial", 16))
        self.Weiter_Knopf.setFixedSize(QSize(80, 30))
        self.Weiter_Knopf.clicked.connect(self.weiter)
        self.Weiter_Knopf.setEnabled(False)
        self.Weiter_Knopf.setStyleSheet("background-color: lightblue")

        #man kehrt ins voherige Menü zurück
        self.Ende_Knopf = QPushButton("beenden")
        self.Ende_Knopf.setFont(QFont("Arial", 16))
        self.Ende_Knopf.setFixedSize(QSize(100, 30))
        self.Ende_Knopf.clicked.connect(self.ende)
        self.Ende_Knopf.setStyleSheet("background-color: lightblue")

        #Layout
        Haupt_VBox = QVBoxLayout()
        Form = QFormLayout()
        Haupt_VBox.addWidget(Titel_Label)
        Form.addRow(Infinitiv_Label, self.Infinitiv_Edit)
        Form.addRow(Simple_Past_Label, self.Simple_Past_Edit)
        Form.addRow(Past_Participle_Label, self.Past_Participle_Edit)
        Grid = QGridLayout()
        Grid.addWidget(Eingabe_Anzeige_Label, 0, 0)
        Grid.addWidget(R_F_Anzeige_Label, 0, 2)
        Grid.addWidget(Rueckmeldungs_Anzeige_Label, 0, 3)
        Grid.addWidget(self.Infinitiv_Richtig_Falsch_Label, 1, 2)
        Grid.addWidget(self.Simple_Past_Richtig_Falsch_Label, 2, 2)
        Grid.addWidget(self.Past_Participle_Richtig_Falsch_Label, 3, 2)
        Grid.addWidget(self.Infinitiv_Rueckmeldung_Label, 1, 3)
        Grid.addWidget(self.Simple_Past_Rueckmeldung_Label, 2, 3)
        Grid.addWidget(self.Past_Participle_Rueckmeldung_Label, 3, 3)
        Grid.addLayout(Form, 1, 0, 4, 2)
        Haupt_VBox.addLayout(Grid)
        HBox = QHBoxLayout()
        HBox.addWidget(self.Bestaetigen_Knopf)
        HBox.addWidget(self.Weiter_Knopf)
        Haupt_VBox.addLayout(HBox)
        Haupt_VBox.addWidget(self.Start_Knopf, alignment=Qt.AlignmentFlag.AlignCenter)
        Haupt_VBox.addWidget(self.Ende_Knopf, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(Haupt_VBox)

        #Methoden
    def start(self):
        if self.gestartet == False:
            self.Info_Label = QLabel("Unten erscheint, nachdem du 'Start' gedrückt hast, ein Verb. Schreibe in jede Zeile die angepasste Form und drücke auf\n'bestätigen', wenn alle Formen eingetragen sind.")
            self.Infinitiv_Edit.setEnabled(True)
            self.Simple_Past_Edit.setEnabled(True)
            self.Past_Participle_Edit.setEnabled(True)
            self.Bestaetigen_Knopf.setEnabled(True)
            self.Weiter_Knopf.setEnabled(True)
            for x in range(0, len(Infinitiv)):
                self.vokabeln.append(x)
            shuffle(self.vokabeln)
            feld = randint(0,3)
            if feld == 0:
                text = Infinitiv[self.vokabeln[self.vokabel_index]]
                self.Infinitiv_Edit.setText(text)
                self.Infinitiv_Edit.setEnabled(False)
                self.Simple_Past_Edit.setFocus()
            elif feld == 1:
                text = Simple_Past[self.vokabeln[self.vokabel_index]]
                self.Simple_Past_Edit.setText(text)
                self.Simple_Past_Edit.setEnabled(False)
                self.Infinitiv_Edit.setFocus()
            else:
                text = Past_Participle[self.vokabeln[self.vokabel_index]]
                self.Past_Participle_Edit.setText(text)
                self.Past_Participle_Edit.setEnabled(False)
                self.Infinitiv_Edit.setFocus()
            self.gestartet = True

    def startPruefung(self):
        self.pruefen(Infinitiv, Simple_Past, Past_Participle, self.vokabel_index)
    def pruefen(self, Infinitiv, Simple_Past, Past_Participle, vokabel_index):
        infinitiv = self.Infinitiv_Edit.text()
        simple_past = self.Simple_Past_Edit.text()
        past_participle = self.Past_Participle_Edit.text()

        if infinitiv == Infinitiv[self.vokabeln[self.vokabel_index]]:
            self.Infinitiv_Richtig_Falsch_Label.setText("Richtig!")
            self.Infinitiv_Rueckmeldung_Label.setText("Kein Fehler!")
        else:
            self.Infinitiv_Richtig_Falsch_Label.setText("Falsch!")
            text = Infinitiv[self.vokabeln[self.vokabel_index]]
            self.Infinitiv_Rueckmeldung_Label.setText(text)

        if simple_past == Simple_Past[self.vokabeln[self.vokabel_index]]:
            self.Simple_Past_Richtig_Falsch_Label.setText("Richtig!")
            self.Simple_Past_Rueckmeldung_Label.setText("Kein Fehler!")
        else:
            self.Simple_Past_Richtig_Falsch_Label.setText("Falsch!")
            text = Simple_Past[self.vokabeln[self.vokabel_index]]
            self.Simple_Past_Rueckmeldung_Label.setText(text)

        if past_participle == Past_Participle[self.vokabeln[self.vokabel_index]]:
            self.Past_Participle_Richtig_Falsch_Label.setText("Richtig!")
            self.Past_Participle_Rueckmeldung_Label.setText("Kein Fehler!")
        else:
            self.Past_Participle_Richtig_Falsch_Label.setText("Falsch!")
            text = Past_Participle[self.vokabeln[self.vokabel_index]]
            self.Past_Participle_Rueckmeldung_Label.setText(text)

    def weiter(self):
        self.Infinitiv_Edit.clear()
        self.Simple_Past_Edit.clear()
        self.Past_Participle_Edit.clear()
        self.Infinitiv_Richtig_Falsch_Label.clear()
        self.Simple_Past_Richtig_Falsch_Label.clear()
        self.Past_Participle_Richtig_Falsch_Label.clear()
        self.Infinitiv_Rueckmeldung_Label.clear()
        self.Simple_Past_Rueckmeldung_Label.clear()
        self.Past_Participle_Rueckmeldung_Label.clear()

        self.vokabel_index += 1
        if (len(Infinitiv)-1) >= self.vokabel_index:
            self.Infinitiv_Edit.setEnabled(True)
            self.Simple_Past_Edit.setEnabled(True)
            self.Past_Participle_Edit.setEnabled(True)
            feld = randint(0,3)
            if feld == 0:
                text = Infinitiv[self.vokabeln[self.vokabel_index]]
                self.Infinitiv_Edit.setText(text)
                self.Infinitiv_Edit.setEnabled(False)
                self.Simple_Past_Edit.setFocus()
            elif feld == 1:
                text = Simple_Past[self.vokabeln[self.vokabel_index]]
                self.Simple_Past_Edit.setText(text)
                self.Simple_Past_Edit.setEnabled(False)
                self.Infinitiv_Edit.setFocus()
            else:
                text = Past_Participle[self.vokabeln[self.vokabel_index]]
                self.Past_Participle_Edit.setText(text)
                self.Past_Participle_Edit.setEnabled(False)
                self.Infinitiv_Edit.setFocus()
        else:
            self.Info_Label.setText("Alle Verben wurde abgefragt.")
            self.Infinitiv_Edit.setEnabled(False)
            self.Simple_Past_Edit.setEnabled(False)
            self.Past_Participle_Edit.setEnabled(False)
            self.Bestaetigen_Knopf.setEnabled(False)
            self.Weiter_Knopf.setEnabled(False)
            self.gestartet = False
            self.vokabeln = []
            for x in range(0, len(Infinitiv)):
                self.vokabeln.append(x)
            shuffle(self.vokabeln)
            self.vokabel_index = 0

    def ende(self):
        #print("Die Verben-Abfrage wurde beendet.")
        self.hide()
        MenuFenster.show()

#Vokabel-Editor
class Vokabel_Editor(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    def initializeUI(self):
        self.setGeometry(10, 30, 1200, 800)
        self.setWindowTitle("Vokabeleditor")
        self.setWindowIcon(QIcon("images/union_jack.png"))
        self.setUpFenster()
    def setUpFenster(self):
        #Oberflächenelemente

        #Titel
        Titel_Label = QLabel("Vokabeleditor")
        Titel_Label.setFont(QFont("Arial", 36))
        Titel_Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        #Datei
        Datei_Label = QLabel("Datei:")
        Datei_Label.setFont(QFont("Arial", 15))
        self.Datei_Edit = QLineEdit()
        self.Datei_Edit.setFont(QFont("Arial", 15))
        self.Datei_Edit.setClearButtonEnabled(True)
        self.Datei_Edit.setPlaceholderText("Datei.txt")

        #Bearbeitung
        self.Vokabel_Tedit = QTextEdit()
        self.Vokabel_Tedit.setFont(QFont("Arial", 15))

        #Knöpfe
        self.Laden_Knopf = QPushButton("laden")
        self.Laden_Knopf.setFont(QFont("Arial", 16))
        self.Laden_Knopf.setFixedSize(80, 30)
        self.Laden_Knopf.setStyleSheet("background-color: lightblue")
        self.Laden_Knopf.clicked.connect(self.laden)

        self.Speichern_Knopf = QPushButton("speichern")
        self.Speichern_Knopf.setFont(QFont("Arial", 16))
        self.Speichern_Knopf.setFixedSize(QSize(110, 30))
        self.Speichern_Knopf.setStyleSheet("background-color: lightblue")
        self.Speichern_Knopf.clicked.connect(self.speichern)

        self.Anleit_Knopf = QPushButton("Anleitung")
        self.Anleit_Knopf.setFont(QFont("Arial", 16))
        self.Anleit_Knopf.setFixedSize(110, 30)
        self.Anleit_Knopf.setStyleSheet("background-color: lightblue")
        self.Anleit_Knopf.clicked.connect(self.anleiten)

        self.Ende_Knopf = QPushButton("beenden")
        self.Ende_Knopf.setFont(QFont("Arial", 16))
        self.Ende_Knopf.setFixedSize(QSize(100, 30))
        self.Ende_Knopf.setStyleSheet("background-color: lightblue")
        self.Ende_Knopf.clicked.connect(self.ende)

        #Layout
        Form = QFormLayout()
        HBox = QHBoxLayout()
        VBox = QVBoxLayout()
        HBox.addWidget(self.Datei_Edit)
        HBox.addWidget(self.Laden_Knopf)
        VBox.addWidget(Titel_Label)
        Form.addRow(Datei_Label, HBox)
        VBox.addLayout(Form)
        VBox.addWidget(self.Vokabel_Tedit)
        VBox.addWidget(self.Speichern_Knopf, alignment=Qt.AlignmentFlag.AlignCenter)
        VBox.addWidget(self.Anleit_Knopf, alignment=Qt.AlignmentFlag.AlignCenter)
        VBox.addWidget(self.Ende_Knopf, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(VBox)
    
    #Methoden
    def laden(self):
        try:
            file = "files/"+self.Datei_Edit.text()
            with open(file, "r", encoding="utf-8") as f:
                text = ""
                for line in f:
                    text += line
                self.Vokabel_Tedit.setText(text)
        except FileNotFoundError as error:
            anleitung = """<p>Die gesuchte Datei existiert nicht.</p>"""
            QMessageBox.warning(self, "Fehler!", anleitung, QMessageBox.StandardButton.Ok)

    def speichern(self):
        file = "files/"+self.Datei_Edit.text()
        with open(file, "w", encoding="utf-8") as f:
            f.write(self.Vokabel_Tedit.toPlainText())

    def anleiten(self):
        print("Anleitung wird geladen.")
        anleitung = """<p>Gib in der Textzeile oben den Namen der Datei nach dem Schema '[Dateiname].txt' ein, die geladen werden soll.
        Falls es eine Datei mit dem Namen nicht geben sollte, wird sie automatisch beim Speichern erstellt.</p>
        <p>Der bereits bestehende Text wird nach dem Laden im Schreibbereich angezeigt und kann bearbeitet werden.</p>
        <p>Achte auf das richtige Schema bei der Eingabe.</p>
        <p>Bei Vokabeln für die einfache Abfrage gilt: 
        [Englisch] [Deutsch] [alternatives Wort auf Deutsch].</p>
        <p>Falls es kein Wort für etwas gibt, schreib '--'. Dies ist aus technischen Gründen notwendig.</p>
        <p>Bei Dateien für die irregulären Verben gilt: [Infinitive] [Simple Past] [Past Participle].</p>"""
        QMessageBox.information(self, "Anleitung", anleitung, QMessageBox.StandardButton.Ok)

    def ende(self):
        print("Editor-Fenster geschlossen.")
        self.hide()
        MenuFenster.show()

#Vokabel_Menue
class Vokabel_Menue(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    def initializeUI(self):
        self.setGeometry(10, 30, 1200, 800)
        self.setWindowTitle("Vokabelauswahl")
        self.setWindowIcon(QIcon("images/union_jack.png"))
        self.setUpFenster()
    def setUpFenster(self):
        #Oberflächenelemente

        #Titel
        Titel_Label = QLabel("Vokabelauswahl")
        Titel_Label.setFont(QFont("Arial", 36))
        Titel_Label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        Auswahl_Label = QLabel("Datei wählen")
        Auswahl_Label.setFont(QFont("Arial", 20))
        Auswahl_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        Ist_Label = QLabel("ausgewählte Dateien")
        Ist_Label.setFont(QFont("Arial", 20))
        Ist_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #Startet Anleitung
        self.Anleit_Knopf = QPushButton("Anleitung")
        self.Anleit_Knopf.setFont(QFont("Arial", 16))
        self.Anleit_Knopf.setStyleSheet("background-color: lightblue")
        self.Anleit_Knopf.setFixedWidth(110)
        self.Anleit_Knopf.clicked.connect(self.anleiten)

        #Auswahl
        breite = 400 #max.breite für Dateinamen

        #einfache Abfrage
        Abfrage_Label = QLabel("einfache Abfrage:")
        Abfrage_Label.setFont(QFont("Arial", 15))
        self.Abfrage_Edit = QLineEdit()
        self.Abfrage_Edit.setFixedWidth(breite)
        self.Abfrage_Edit.setClearButtonEnabled(True)
        self.Abfrage_Edit.setFont(QFont("Arial", 15))
        self.Abfrage_Bestaetigen_Knopf = QPushButton("laden")
        self.Abfrage_Bestaetigen_Knopf.setFont(QFont("Arial", 16))
        self.Abfrage_Bestaetigen_Knopf.setFixedWidth(70)
        self.Abfrage_Bestaetigen_Knopf.setStyleSheet("background-color: lightblue")
        self.Abfrage_Bestaetigen_Knopf.clicked.connect(self.vokabelnAbfrageLaden)

        #unregelmäßige Verben
        Verben_Label = QLabel("unregelmäßige Verben:")
        Verben_Label.setFont(QFont("Arial", 15))
        self.Verben_Edit = QLineEdit()
        self.Verben_Edit.setFixedWidth(breite)
        self.Verben_Edit.setClearButtonEnabled(True)
        self.Verben_Edit.setFont(QFont("Arial", 15))
        self.Verben_Bestaetigen_Knopf = QPushButton("laden")
        self.Verben_Bestaetigen_Knopf.setFont(QFont("Arial", 16))
        self.Verben_Bestaetigen_Knopf.setFixedWidth(70)
        self.Verben_Bestaetigen_Knopf.setStyleSheet("background-color: lightblue")
        self.Verben_Bestaetigen_Knopf.clicked.connect(self.verbenLaden)


        #Ist-Anzeigen

        #einfache Abfrage
        Abfrage_ist_Label = QLabel("einfache Abfrage:")
        Abfrage_ist_Label.setFont(QFont("Arial", 15))
        self.Abfrage_ist_Anzeige_Label = QLabel()
        self.Abfrage_ist_Anzeige_Label.setFont(QFont("Arial", 15))

        #unregelmäßige Verben
        Verben_ist_Label = QLabel("unregelmäßige Verben:")
        Verben_ist_Label.setFont(QFont("Arial", 15))
        self.Verben_ist_Anzeige_Label = QLabel()
        self.Verben_ist_Anzeige_Label.setFont(QFont("Arial", 15))

        #Ende
        self.Ende_Knopf = QPushButton("beenden")
        self.Ende_Knopf.setFont(QFont("Arial", 16))
        self.Ende_Knopf.setFixedWidth(100)
        self.Ende_Knopf.setStyleSheet("background-color: lightblue")
        self.Ende_Knopf.clicked.connect(self.ende)

        #Layout
        HBox1 = QHBoxLayout()
        HBox1.addWidget(self.Abfrage_Edit)
        HBox1.addWidget(self.Abfrage_Bestaetigen_Knopf)
        HBox2 = QHBoxLayout()
        HBox2.addWidget(self.Verben_Edit)
        HBox2.addWidget(self.Verben_Bestaetigen_Knopf)
        VBox_Haupt = QVBoxLayout()
        VBox_Haupt.addWidget(Titel_Label)
        Form1 = QFormLayout()
        Form1.addRow(Abfrage_Label, HBox1)
        Form1.addRow(Verben_Label, HBox2)
        Form2 = QFormLayout()
        Form2.addRow(Abfrage_ist_Label, self.Abfrage_ist_Anzeige_Label)
        Form2.addRow(Verben_ist_Label, self.Verben_ist_Anzeige_Label)
        VBox_1 = QVBoxLayout()
        VBox_1.addWidget(Auswahl_Label)
        VBox_1.addLayout(Form1)
        VBox_2 = QVBoxLayout()
        VBox_2.addWidget(Ist_Label)
        VBox_2.addLayout(Form2)
        VBox_Haupt.addLayout(VBox_1)
        VBox_Haupt.addLayout(VBox_2)
        VBox_Haupt.addWidget(self.Anleit_Knopf, alignment=Qt.AlignmentFlag.AlignCenter)
        VBox_Haupt.addWidget(self.Ende_Knopf, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(VBox_Haupt)
    
    #Methoden
    def anleiten(self):
        anleitung = """<p>In diesem Menü können .txt-Datei als Wörterbücher ausgewählt werden, indem man den Namen der Datei in das Feld eingibt.</p>
        <p>Achtung: Der vollständige Dateiname (also mit Datentyp .txt) muss angegeben werden, weil sie sonst nicht geladen werden kann.</p>
        <p>Außerdem muss die Datei im Arbeitsverzeichnis gespeichert werden. Das ist in diesem Fall das Verzeichnis mit der .exe-Datei für dieses Programm.</p>
        <p>Die ausgewählte Datei muss per Knopfdruck bestätigt werden, damit sie geladen wird.</p>
        <p>Für Deutsch-Englisch und Englisch-Deutsch wird die gleiche Datei verwendet und wird unter 'einfache Abfrage' angegeben.</p>"""
        QMessageBox.information(self, "Anleitung", anleitung, QMessageBox.StandardButton.Ok)

    def vokabelnAbfrageLaden(self):
        file = "files/"+self.Abfrage_Edit.text()
        geladen = vokabelnAbfrageLaden(file)
        if geladen == True:
            text = "Die Datei " + file + " wurde geladen."
        elif file == "--" or file == "":
            text = "Keine Datei"
        else:
            text = "Die Datei " + file + " konnte nicht geladen werden."
        self.Abfrage_ist_Anzeige_Label.setText(text)

    def verbenLaden(self):
        file = "files/"+self.Verben_Edit.text()
        geladen = verbenLaden(file)
        if geladen == True:
            text = "Die Datei " + file + " wurde geladen."
        elif file == "--" or file == "":
            text = "Keine Datei"    
        else:
            text = "Die Datei " + file + " konnte nicht geladen werden."
        self.Verben_ist_Anzeige_Label.setText(text)

    def sichern(self):
        with open("files/setup.txt", "w") as f:
            if self.Abfrage_Edit.text() != "":
                text = "files/"+self.Abfrage_Edit.text()
            else:
                text = "--"
            text += " "
            if self.Verben_Edit.text() != "":
                text += "files/"+self.Verben_Edit.text()
            else:
                text += "--"
            f.write(text)

    def ende(self):
        print("Menü geschlossen.")
        self.sichern()
        self.hide()
        MenuFenster.show()

#spätere Ausführung
if __name__ == '__main__':
    app = QApplication(sys.argv)

    setupLaden()
    Credits = Mitwirkende()
    Hilfe = Hilfefenster()
    SF = Startfenster()
    MenuFenster = Menufenster()
    DEF = Deutsch_Englisch()
    EDF = Englisch_Deutsch()
    VF = Verbenfenster()
    VE = Vokabel_Editor()
    VM = Vokabel_Menue()

    geladen = vokabelnAbfrageLaden(Setup[0])
    if geladen == True:
        text = "Die Datei " + Setup[0] + " wurde geladen."
        VM.Abfrage_ist_Anzeige_Label.setText(text)
        VM.Abfrage_Edit.setText(Setup[0])
    elif Setup[0] == "--":
        VM.Abfrage_ist_Anzeige_Label.setText("Keine Datei")
    else:
        text = "Die Datei " + Setup[0] + " konnte nicht geladen werden."
        VM.Abfrage_ist_Anzeige_Label.setText(text)
    
    geladen = verbenLaden(Setup[1])
    if geladen == True:
        text = "Die Datei " + Setup[1] + " wurde geladen."
        VM.Verben_ist_Anzeige_Label.setText(text)
        VM.Verben_Edit.setText(Setup[1])
    elif Setup[1] == "--":
        VM.Verben_ist_Anzeige_Label.setText("Keine Datei")
    else:
        text = "Die Datei " + Setup[1] + " konnte nicht geladen werden."
        VM.Verben_ist_Anzeige_Label.setText(text)

    sys.exit(app.exec())