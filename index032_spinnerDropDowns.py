"""
Kivy - Codemy.com #32 : Spinner Dropdowns - Python Kivy GUI Tutorial #32
Lien : https://www.youtube.com/watch?v=Wu7kTFZtM6I&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=32

Dans ce programme on apprend à faire une liste déroulante

Éditeur : Laurent REYNAUD
Date : 18-01-21
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script

Builder.load_file('index032_spinnerDropDowns.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


class MyLayout(Widget):  # Widget en argument car le constructeur de la classe est dans le fichier .kv

    def spinner_clicked(self, value):
        """Fonction permettant d'afficher la pizza choisie"""
        self.ids.click_label.text = f"Vous avez sélectionné {value}"


class AwesomeApp(App):  # App en argument car on a recours à la bibliothèque kivy
    """Classe permettant de construire les widgets à partir de la classe ci-dessus : le nom de la classe importe car
    l'instruction ci-dessus : 'Builder.load_file('whatever.kv')' permet de récupérer le fichier .kv à rattacher à ce
    script"""

    def build(self):
        """Dans cette fonction, on appelle la classe MyLayout() ci-dessus"""
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
