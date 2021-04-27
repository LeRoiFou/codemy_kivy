"""
Kivy - Codemy.com #25 : Sliders For Kivy - Python Kivy GUI Tutorial #25 
Lien : https://www.youtube.com/watch?v=18bvQW2OHZE&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=25 

Dans ce programme on apprend à utiliser un curseur 

Éditeur : Laurent REYNAUD 
Date : 17-01-21 
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script

Builder.load_file('index025_sliders.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


class MyLayout(Widget):  # Widget en argument car le constructeur de la classe est dans le fichier .kv

    def slide_it(self, *args):
        """Fonction permettant d'afficher l'échelle de graduation du curseur qui va de 1 à 50
        L'argument '*args' est un tuple de 2 composants : l'indice 1 est l'échelle de graduation du curseur qui va de 1
        à 50"""

        self.slide_text.text = str(int(args[1]))  # remplacement du titre par la graduation du curseur
        self.slide_text.font_size = str(int(args[1] * 5))  # taille de la police variant selon la graduation du curseur


class AwesomeApp(App):  # App en argument car on a recours à la bibliothèque kivy
    """Classe permettant de construire les widgets à partir de la classe ci-dessus : le nom de la classe importe car
    l'instruction ci-dessus : 'Builder.load_file('whatever.kv')' permet de récupérer le fichier .kv à rattacher à ce
    script"""

    def build(self):
        """Dans cette fonction, on appelle la classe MyLayout() ci-dessus"""
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
