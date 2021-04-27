# Kivy - Codemy.com #041 : How To Teach Yourself KivyMD Quickly - Python Kivy GUI Tutorial #41
# Lien : https://www.youtube.com/watch?v=gW4byuP97K4
#
# Site : https://kivymd.readthedocs.io/en/latest/index.html
#
# Pour voir la démo des widgets, se mettre sur GitBash puis aller dans le répertoire :
# C:\Users\LRCOM\PycharmProjects\codemy_kivy\kivymd\KivyMD\demos
# Et sélectionner un des répertoires et puis saisir dans GitBash dès l'accès au répertoire souhaité : python main.py
#
# Dans ce cours on apprend à récupérer les instructions à mettre dans le fichier .py pour obtenir les widgets présentés
# dans KivyMd (similaire à QtDesigner pour PyQt). Pour cela, il existe un fichier .py pour chaque widget situés dans le
# répertoire suivant :
# C:\Users\LRCOM\PycharmProjects\codemy_kivy\kivymd\KivyMD\kivymd\uix
#
# Autre possibilité : aller sur la démo des widgets -> cliquer sur l'icône en haut à droite de la fenêtre où se trouve
# le widget souhaité et lorsqu'une nouvelle fenêtre apparaît, aller tout en bas et cliquer sur le lien pour accéder à
# la page @ avec le script lié au widget souhaité
#
# Autre exemple ci-dessous
#
# Éditeur : Laurent REYNAUD
# Date : 04-03-21

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script
from kivymd.app import MDApp  # récupérération de KivyMd

Builder.load_file('index041_kivyMd-3.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


class MyLayout(Widget):  # Widget en argument car le constructeur de la classe est dans le fichier .kv
    pass


class AwesomeApp(MDApp):  # App en argument car on a recours à la bibliothèque KivyMd cette fois-ci
    # Classe permettant de construire les widgets à partir de la classe ci-dessus : le nom de la classe importe car
    # l'instruction ci-dessus : 'Builder.load_file('whatever.kv')' permet de récupérer le fichier .kv à rattacher à ce
    # script.

    def build(self):
        """Fonction modifiée en récupérant l'instruction mentionnée dans le répertoire KivyMd..."""
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
