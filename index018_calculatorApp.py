"""
Kivy - Codemy.com #18 : Fix Our Decimal Calculator Problem - Python Kivy GUI Tutorial #18
Lien : https://www.youtube.com/watch?v=AvbcELqNbx0&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=18

Dans ce programme on résout le problème de la décimale qui ne s'affiche qu'une seule fois lors du précédent programme

Éditeur : Laurent REYNAUD
Date : 14-01-21
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script
from kivy.core.window import Window  # configuration de la taille de la fenêtre principale

"""Taille de la fenêtre principale"""
Window.size = (500, 700)

Builder.load_file('index018_calculatorApp.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


class MyLayout(Widget):  # Widget en argument car le constructeur de la classe est dans le fichier .kv
    pass

    def clear(self):
        """Fonction permettant de réinitialiser les chiffres affichés en appuyant sur le bouton 'C'"""
        self.ids.calc_input.text = '0'

    def remove(self):
        """Fonction permettant d'effacer le dernier chiffre affiché en appuyant sur le bouton '<<'"""

        """Assignation d'une variable des chiffres affichés à la calculatrice"""
        prior = self.ids.calc_input.text

        """Suppression d'un chiffre de la liste"""
        prior = prior[:-1]

        """Affichage des chiffres déduction de celui qui a été supprimé"""
        self.ids.calc_input.text = prior

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

    def math_sign(self, sign):
        """Fonction permettant d'afficher l'opération + - * /"""

        """Assignation d'une variable des chiffres affichés à la calculatrice"""
        prior = self.ids.calc_input.text

        """Ajout du caractère '+' aux chiffres affichés"""
        self.ids.calc_input.text = f"{prior}{sign}"

    def pos_neg(self):
        """Fonction permettant d'activer le bouton '+/-'"""

        """Assignation d'une variable des chiffres affichés à la calculatrice"""
        prior = self.ids.calc_input.text

        """Vérification s'il y a déjà le signe '-'"""
        if '-' in prior:
            self.ids.calc_input.text = f"{prior.replace('-', '')}"
        else:
            self.ids.calc_input.text = f"-{prior}"

    def dot(self):
        """Fonction pour la décimale"""

        """Assignation d'une variable des chiffres affichés à la calculatrice"""
        prior = self.ids.calc_input.text
        num_list = prior.split('+')  # affichage des chiffres dans une liste sans le caractère '+'

        if '+' in prior and '.' not in num_list[-1]:
            """Si le signe '+' est affiché et que le dernier chiffre qui suit n'a pas de décimale, alors  
            ajout du caractère '.' aux chiffres affichés"""
            prior = f"{prior}."
            """Affichage du caractère '.' aux chiffres affichés"""
            self.ids.calc_input.text = prior
        elif '.' in prior:
            """Si le '.' a déjà été mis..."""
            pass
        else:
            """Ajout du caractère '.' aux chiffres affichés"""
            prior = f"{prior}."
            """Affichage du caractère '.' aux chiffres affichés"""
            self.ids.calc_input.text = prior

    def equals(self):
        """Fonction permettant d'effectuer l'opération"""

        """Assignation d'une variable des chiffres affichés à la calculatrice"""
        prior = self.ids.calc_input.text

        """L'opération est une addition"""
        if '+' in prior:
            num_list = prior.split('+')  # affichage des chiffres dans une liste sans le caractère '+'
            answer = 0.0  # assignation du chiffre 0.00
            for number in num_list:  # pour chaque chiffre de la liste
                answer = answer + float(number)  # le chiffre s'additionne au chiffre 0
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
