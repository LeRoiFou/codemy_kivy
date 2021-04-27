"""
Kivy - Codemy.com #28 : CheckBoxes For Kivy - Python Kivy GUI Tutorial #28
Lien : https://www.youtube.com/watch?v=RpAzki0UJPI&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=28

Dans ce programme on apprend à afficher une coche d'option (similaire cours 17_Checkboxes.py pour tkinter)

Éditeur : Laurent REYNAUD
Date : 17-01-21
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script

Builder.load_file('index028_checkBoxes.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


class MyLayout(Widget):  # Widget en argument car le constructeur de la classe est dans le fichier .kv

    """Assignation d'une liste vide"""
    checks = []

    def checkbox_click(self, instance, value, topping):  # value = True lorsqu'on coche et False lorsqu'on décoche
        """Fonction qui génère un message lorsqu'on coche la case"""

        if value:  # si on coche la case
            MyLayout.checks.append(topping)  # ajout des données dans la liste
            tops = ''  # assignation d'une espace
            for i in MyLayout.checks:
                tops = f"{tops} {i}"
            self.ids.output_label.text = f"Vous avez sélectionné : {tops}"
        else:
            MyLayout.checks.remove(topping)  # suppression des données dans la liste
            tops = ''  # assignation d'une espace
            for i in MyLayout.checks:
                tops = f"{tops} {i}"
            self.ids.output_label.text = f"Vous avez sélectionné : {tops}"


class AwesomeApp(App):  # App en argument car on a recours à la bibliothèque kivy
    """Classe permettant de construire les widgets à partir de la classe ci-dessus : le nom de la classe importe car
    l'instruction ci-dessus : 'Builder.load_file('whatever.kv')' permet de récupérer le fichier .kv à rattacher à ce
    script"""

    def build(self):
        """Dans cette fonction, on appelle la classe MyLayout() ci-dessus"""
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
