"""
Kivy - Codemy.com #23 : Image Viewer With FileChooserIconView and FileChooserListView - Python Kivy GUI Tutorial #23
Lien : https://www.youtube.com/watch?v=YlRd4rw_vBw&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=23

Dans ce programme on apprend à afficher des répertoires et des fichiers dans la fenêtre principale
Documentation kivy sur ce point : https://kivy.org/doc/stable/api-kivy.uix.filechooser.html

Éditeur : Laurent REYNAUD
Date : 16-01-21
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script

Builder.load_file('index023_imageViewer&FileChooser.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


class MyLayout(Widget):  # Widget en argument car le constructeur de la classe est dans le fichier .kv

    def selected(self, filename):
        """Fonction permettant d'afficher une image dans le cadre mis en place dans la fenêtre principale"""

        try:
            self.ids.my_image.source = filename[0]
        except:
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
