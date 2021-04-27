"""
Kivy - Codemy.com #9 : Setting Default Widget Properties - Python Kivy GUI Tutorial #9
Lien : https://www.youtube.com/watch?v=e73K1DoTNio&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=9

Dans ce programme on apprend à configurer les widgets selon un système similaire à un héritage : tous les widgets de la
fenêtre vont être configurés avec une même instruction. On apprend également à personnaliser la configuration d'un
widget avec la mise en place de ce système similaire à un héritage

Éditeur : Laurent REYNAUD
Date : 11-01-21
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script

Builder.load_file('index009_settingDefaultWidgetProperties.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


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
