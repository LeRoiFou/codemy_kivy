"""
Kivy - Codemy.com #8 : Kivy Box Layout - Python Kivy GUI Tutorial #8
Lien : https://www.youtube.com/watch?v=ZFGAz6vZx1E&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=8

Dans ce programme on apprend à changer l'orientation des boutons, à changer la taille des boutons et à positionner les
boutons sur une ligne.
Pour cela, il faut recourir à l'instruction BoxLayout dans le fichier .kv

Éditeur : Laurent REYNAUD
Date : 11-01-21
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script

Builder.load_file('index008_boxLayout.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


class MyLayout(Widget):  # Widget en argument car le constructeur de la classe est dans le fichier .kv
    pass


class AwesomeApp(App):  # App en argument car on a recours à la bibliothèque kivy
    """Classe permettant de construire les widgets à partir de la classe ci-dessus : le nom de la classe importe car
    l'instruction ci-dessus : 'Builder.load_file('whatever.kv')' permet de récupérer le fichier .kv à rattacher à ce
    script"""

    def build(self):
        """Dans cette fonction, on apelle la classe MyGridLayout() ci-dessus"""
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
