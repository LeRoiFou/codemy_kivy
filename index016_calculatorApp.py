"""
Kivy - Codemy.com #16 : Calculator Addition Function - Python Kivy GUI Tutorial #16
Lien : https://www.youtube.com/watch?v=pdQ_KZS_GRQ&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=16

Dans ce programme on apprend à additionner dans la calculatrice

Éditeur : Laurent REYNAUD
Date : 13-01-21
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script
from kivy.core.window import Window  # configuration de la taille de la fenêtre principale

"""Taille de la fenêtre principale"""
Window.size = (500, 700)

Builder.load_file('index016_calculatorApp.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


class MyLayout(Widget):  # Widget en argument car le constructeur de la classe est dans le fichier .kv
    pass

    def clear(self):
        """Fonction permettant de réinitialiser les chiffres affichés en appuyant sur le bouton 'C'"""
        self.ids.calc_input.text = '0'

    def button_press(self, button):
        """Fonction permettant d'afficher le bouton appuyé"""

        """Assignation d'une variable des chiffres affichés à la calculatrice"""
        prior = self.ids.calc_input.text

        """Détermine si le chiffre 0 est affiché"""
        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f"{button}"  # affichage du 1er chiffre
        else:
            self.ids.calc_input.text = f"{prior}{button}"  # affichage des chiffres suivants

    def add(self):
        """Fonction permettant d'afficher l'addition"""

        """Assignation d'une variable des chiffres affichés à la calculatrice"""
        prior = self.ids.calc_input.text

        """Ajout du caractère '+' aux chiffres affichés"""
        self.ids.calc_input.text = f"{prior}+"

    def substract(self):
        """Fonction permettant d'afficher la soustraction"""

        """Assignation d'une variable des chiffres affichés à la calculatrice"""
        prior = self.ids.calc_input.text

        """Ajout du caractère '-' aux chiffres affichés"""
        self.ids.calc_input.text = f"{prior}-"

    def multiply(self):
        """Fonction permettant d'afficher la multiplication"""

        """Assignation d'une variable des chiffres affichés à la calculatrice"""
        prior = self.ids.calc_input.text

        """Ajout du caractère 'x' aux chiffres affichés"""
        self.ids.calc_input.text = f"{prior}*"

    def divide(self):
        """Fonction permettant d'afficher la division"""

        """Assignation d'une variable des chiffres affichés à la calculatrice"""
        prior = self.ids.calc_input.text

        """Ajout du caractère '/' aux chiffres affichés"""
        self.ids.calc_input.text = f"{prior}/"

    def equals(self):
        """Fonction permettant d'effectuer l'opération"""

        """Assignation d'une variable des chiffres affichés à la calculatrice"""
        prior = self.ids.calc_input.text

        """L'opération est une addition"""
        if '+' in prior:
            num_list = prior.split('+')  # affichage des chiffres dans une liste sans le caractère '+'
            answer = 0  # assignation de l'entier 0
            for number in num_list:  # pour chaque chiffre de la liste
                answer = answer + int(number)  # le chiffre s'additionne au chiffre 0
            self.ids.calc_input.text = str(answer)  # Affichage du résultat sur la calculatrice


class CalculatriceApp(App):  # App en argument car on a recours à la bibliothèque kivy
    """Classe permettant de construire les widgets à partir de la classe ci-dessus : le nom de la classe importe car
    l'instruction ci-dessus : 'Builder.load_file('whatever.kv')' permet de récupérer le fichier .kv à rattacher à ce
    script"""

    def build(self):
        """Dans cette fonction, on appelle la classe MyLayout() ci-dessus"""
        return MyLayout()


if __name__ == '__main__':
    CalculatriceApp().run()
