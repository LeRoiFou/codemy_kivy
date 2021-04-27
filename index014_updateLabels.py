"""
Kivy - Codemy.com #14 : How To Update Labels - Python Kivy GUI Tutorial #14
Lien : https://www.youtube.com/watch?v=7Sks1Ld1DWY&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=14

Dans ce programme on apprend à changer le message affiché dans le widget Label après avoir appuyé sur le bouton
d'exécution

Éditeur : Laurent REYNAUD
Date : 13-01-21
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script

Builder.load_file('index014_updateLabels.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


class MyLayout(Widget):  # Widget en argument car le constructeur de la classe est dans le fichier .kv

    def press(self):
        """Fonction permettant d'afficher dans le widget Label les mots saisis dans le champ TextInput après avoir
        appuyé sur le bouton d'exécution"""

        """Assignation d'une variable pour la saisie faite dans le widget TextInput"""
        name = self.ids.name_input.text

        """Mise à jour du widget Label"""
        self.ids.name_label.text = f"Salut {name} !"

        """Réinitialisation du champ de saisie (widget TextInput)"""
        self.ids.name_input.text = ''


class AwesomeApp(App):  # App en argument car on a recours à la bibliothèque kivy
    """Classe permettant de construire les widgets à partir de la classe ci-dessus : le nom de la classe importe car
    l'instruction ci-dessus : 'Builder.load_file('whatever.kv')' permet de récupérer le fichier .kv à rattacher à ce
    script"""

    def build(self):
        """Dans cette fonction, on appelle la classe MyLayout() ci-dessus"""
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
