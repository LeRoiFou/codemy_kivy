"""
Kivy - Codemy.com #30 : Popup Boxes For Kivy - Python Kivy GUI Tutorial #30 
Lien : https://www.youtube.com/watch?v=NzUTZj31AfM&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=30 

Dans ce programme on apprend à afficher une fenêtre pop-up 

Dans le fichier .kv, la 1ère ligne est affichée : "#:import Factory kivy.factory.Factory" -> équivaut à une variable 
globale car le bouton situé dans le bloc d'instruction 'MyLayout' nécessite de recourir au bloc d'instruction 'MyPopup' 
qui est dans un bloc à part de celui de 'MyLayout' 

Cette fenêtre ne peut avoir qu'un seul widget. Afin de détourner ça, il suffit de déclarer un 'BoxLayout' 

Éditeur : Laurent REYNAUD 
Date : 17-01-21 
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script

Builder.load_file('index030_popupBoxes.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


class MyLayout(Widget):  # Widget en argument car le constructeur de la classe est dans le fichier .kv

    pass


class AwesomeApp(App):  # App en argument car on a recours à la bibliothèque kivy
    """Classe permettant de construire les widgets à partir de la classe ci-dessus : le nom de la classe importe car
    l'instruction ci-dessus : 'Builder.load_file('whatever.kv')' permet de récupérer le fichier .kv à rattacher à ce
    script"""

    def build(self):
        """Dans cette fonction, on appelle la classe MyLayout() ci-dessus"""
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
