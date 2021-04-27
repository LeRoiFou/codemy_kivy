"""
Kivy - Codemy.com #31 : Multiple Windows With ScreenManager - Python Kivy GUI Tutorial #31
Lien : https://www.youtube.com/watch?v=Prt_SKkZji8&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=31

Dans ce programme on apprend à afficher plusieurs fenêtres comme si on avait deux écrans

Éditeur : Laurent REYNAUD
Date : 18-01-21
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script
from kivy.uix.screenmanager import Screen, ScreenManager  # gestionnaire des écrans


class FirstWindow(Screen):
    """Classe pour le 1er écran"""
    pass


class SecondWindow(Screen):
    """Classe pour le 2ème écran"""
    pass


class WindowManager(ScreenManager):
    """Classe pour le gestionnaire d'écrans"""
    pass


kv = Builder.load_file('index031_multipleWindows.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


class AwesomeApp(App):  # App en argument car on a recours à la bibliothèque kivy
    """Classe permettant de construire les widgets à partir de la classe ci-dessus : le nom de la classe importe car
    l'instruction ci-dessus : 'Builder.load_file('whatever.kv')' permet de récupérer le fichier .kv à rattacher à ce
    script"""

    def build(self):
        """Dans cette fonction, on fait appel à la variable ci-dessus 'kv'"""
        return kv


if __name__ == '__main__':
    AwesomeApp().run()
