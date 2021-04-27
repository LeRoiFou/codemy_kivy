"""
Kivy - Codemy.com #19 : Math Calculator Buttons With eval() - Python Kivy GUI Tutorial #19
Lien : https://www.youtube.com/watch?v=xeXCrZrJazI&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=19

Dans ce programme on complète avec les autres opérations que les additions en recourant à l'instruction eval()
Eval () prend la str et la sépare et l'évalue, c'est-à-dire fait le calcul.

Et on a rajouté en complément la fonction pour le '%' afin de terminer l'application.

Éditeur : Laurent REYNAUD
Date : 14-01-21
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script
from kivy.core.window import Window  # configuration de la taille de la fenêtre principale

"""Taille de la fenêtre principale"""
Window.size = (500, 700)

Builder.load_file('index019_calculatorApp.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


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

        """Si le message 'Erreur' est affiché : réinitialisation de l'affichage des données"""
        if 'Erreur' in prior:
            prior = ''

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

        try:
            """Assignation de l'opération à effectuer"""
            answer = eval(prior)  # l'instruction eval permet de faire des opérations des str !!!

            """Affichage de l'opération"""
            self.ids.calc_input.text = str(answer)
        except ZeroDivisionError:
            self.ids.calc_input.text = 'Erreur'

    def percentage(self):
        """Fonction permettant d'effectuer le '%'"""

        """Assignation d'une variable des chiffres affichés à la calculatrice"""
        prior = self.ids.calc_input.text

        """Assignation de l'opération à effectuer"""
        answer = eval(prior)  # l'instruction eval permet de faire des opérations des str !!!

        if answer == '0':
            pass
        else:
            """Division du résultat affiché par 100"""
            answer = answer / 100
            """Affichage de l'opération"""
            self.ids.calc_input.text = str(answer)
            """Réinitialisation"""
            answer = '0'


class CalculatriceApp(App):  # App en argument car on a recours à la bibliothèque kivy
    """Classe permettant de construire les widgets à partir de la classe ci-dessus : le nom de la classe importe car
    l'instruction ci-dessus : 'Builder.load_file('whatever.kv')' permet de récupérer le fichier .kv à rattacher à ce
    script"""

    def build(self):
        """Dans cette fonction, on appelle la classe MyLayout() ci-dessus"""
        return MyLayout()


if __name__ == '__main__':
    CalculatriceApp().run()
