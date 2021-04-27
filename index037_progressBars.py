"""
Kivy - Codemy.com #37 : How To Create Progress Bars With Kivy - Python Kivy GUI Tutorial #37 
Lien : https://www.youtube.com/watch?v=D1Lg3oR_qig 

Dans ce programme on apprend à créer une barre de progression 

Éditeur : Laurent REYNAUD 
Date : 03-02-21 
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script

Builder.load_file('index037_progressBars.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


class MyLayout(Widget):  # Widget en argument car le constructeur de la classe est dans le fichier .kv

    def press_it(self):
        """Fonction permettant d'afficher le taux de progression de la barre en appuyant sur le bouton d'exécution"""

        """Assignation de la valeur de la progression de la barre"""
        current = self.ids.my_progress_bar.value

        """Si on arrive au bout de la barre de progression..."""
        if current == 1:
            current = 0  # remise à niveau de la barre de progression à sa position d'origine

        """Progression de la barre de 25 % à chaque fois qu'on appuye sur le bouton"""
        current += .25  # incrémentation de +.25
        self.ids.my_progress_bar.value = current  # mise à jour de la barre de progression

        """Mise à jour de l'étiquette"""
        self.ids.my_label.text = f"Progression de {int(current * 100)} %"


class AwesomeApp(App):  # App en argument car on a recours à la bibliothèque kivy
    """Classe permettant de construire les widgets à partir de la classe ci-dessus : le nom de la classe importe car
    l'instruction ci-dessus : 'Builder.load_file('whatever.kv')' permet de récupérer le fichier .kv à rattacher à ce
    script"""

    def build(self):
        """Dans cette fonction, on appelle la classe MyLayout() ci-dessus"""
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
