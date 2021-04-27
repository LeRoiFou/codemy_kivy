"""
Kivy - Codemy.com #35 : Using Images As Buttons - Python Kivy GUI Tutorial #35
Lien : https://www.youtube.com/watch?v=mEAjGChhwcs

Dans ce programme on créé un bouton à la forme d'une image (similaire tuto 66_ImageButton&Border de tkinter)

Éditeur : Laurent REYNAUD
Date : 18-01-21
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script

Builder.load_file('index035_imagesAsButtons.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


class MyLayout(Widget):  # Widget en argument car le constructeur de la classe est dans le fichier .kv

    def hello_on(self):
        """Fonction permettant d'afficher qu'on a bien appuyé sur le bouton et changement de l'image du bouton"""

        self.ids.my_label.text = 'Tu appuies sur le bouton !'
        self.ids.my_image.source = 'images/login_pressed.png'  # chargement de l'image du bouton appuyé

    def hello_off(self):
        """Fonction permettant de montrer l'image du bouton à l'origine"""

        self.ids.my_label.text = 'Salut !'
        self.ids.my_image.source = 'images/login.png'  # chargement de l'image du bouton non appuyé


class AwesomeApp(App):  # App en argument car on a recours à la bibliothèque kivy
    """Classe permettant de construire les widgets à partir de la classe ci-dessus : le nom de la classe importe car
    l'instruction ci-dessus : 'Builder.load_file('whatever.kv')' permet de récupérer le fichier .kv à rattacher à ce
    script"""

    def build(self):
        """Dans cette fonction, on appelle la classe MyLayout() ci-dessus"""
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
