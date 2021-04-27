"""
Kivy - Codemy.com #039 : How To Create a Switch With Kivy - Python Kivy GUI Tutorial #39
Lien : https://www.youtube.com/watch?v=4-PASskUCW0

Dans ce programme on apprend un nouveau wigdet : switch (similaire au programme tkinter : 161_onOffButtonSwitch) qui est
un interrupteur 'On/Off'

Éditeur : Laurent REYNAUD
Date : 19-02-21
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script

Builder.load_file('index039_switch.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


class MyLayout(Widget):  # Widget en argument car le constructeur de la classe est dans le fichier .kv

    def switch_click(self, switchObject, switchValue):
        """Le paramètre switchValue affecte le booléen False lorsque l'interrupteur est sur Off et inversement"""
        if switchValue:
            self.ids.my_label.text = 'Tu as appuyé sur On !'
        else:
            self.ids.my_label.text = 'Tu as appuyé sur Off !'
            self.ids.my_switch.disabled = False  # True : lorsqu'on appuye sur 'On' l'interrupteur est désactivé


class AwesomeApp(App):  # App en argument car on a recours à la bibliothèque kivy
    """Classe permettant de construire les widgets à partir de la classe ci-dessus : le nom de la classe importe car
    l'instruction ci-dessus : 'Builder.load_file('whatever.kv')' permet de récupérer le fichier .kv à rattacher à ce
    script"""

    def build(self):
        """Dans cette fonction, on appelle la classe MyLayout() ci-dessus"""
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
