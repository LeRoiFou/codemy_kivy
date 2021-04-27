"""
Kivy - Codemy.com #34 : Tabs For Kivy - Python Kivy GUI Tutorial #34
Lien : https://www.youtube.com/watch?v=hoEbMTE_k-M&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=34

Dans ce programme on apprend à faire des onglets (similaire au tuto 64_NoteBook de tkinter)

Éditeur : Laurent REYNAUD
Date : 18-01-21
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script
from kivy.uix.tabbedpanel import TabbedPanel  # pour les onglets

Builder.load_file('index034_tabs.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


class MyLayout(TabbedPanel):  # TabbedPanel en argument pour les onglets

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
