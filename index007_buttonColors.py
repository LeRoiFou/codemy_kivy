"""
Kivy - Codemy.com #7 : Changing Kivy Button Colors - Python Kivy GUI Tutorial #7
Lien : https://www.youtube.com/watch?v=2IuAQ1HUpU4&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=7

Dans ce programme on apprend à changer la couleur des widgets.
Pour obtenir les codes couleurs RGB / hexadécimaux, il existe le lien ci-dessous :
https://duckduckgo.com/?q=color+picker&atb=v242-1&ia=answer

Éditeur : Laurent REYNAUD
Date : 11-01-21
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script

Builder.load_file('index007_buttonColors.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


class MyGridLayout(Widget):  # Widget en argument car le constructeur de la classe est dans le fichier .kv
    """La classe ne comprend plus que la fonction attribuée au bouton d'exécution car le constructeur est dans le
    fichier .kv"""

    def press(self):
        """Texte à afficher après avoir appuyé sur le bouton"""

        """Assignation des champs de saisis"""
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        """Affichage du texte après avoir appuyé sur le bouton"""
        print(f"Salut {name}, tu aimes la pizza {pizza}, et ta couleur favorite est {color}")

        """Réinitialisation des champs de saisis"""
        self.name.text = ''
        self.pizza.text = ''
        self.color.text = ''


class AwesomeApp(App):  # App en argument car on a recours à la bibliothèque kivy
    """Classe permettant de construire les widgets à partir de la classe ci-dessus : le nom de la classe importe car
    l'instruction ci-dessus : 'Builder.load_file('whatever.kv')' permet de récupérer le fichier .kv à rattacher à ce
    script"""

    def build(self):
        """Dans cette fonction, on apelle la classe MyGridLayout() ci-dessus"""
        return MyGridLayout()


if __name__ == '__main__':
    AwesomeApp().run()
