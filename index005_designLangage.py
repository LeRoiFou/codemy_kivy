"""
Kivy - Codemy.com #5 : Kivy Design Language - Python Kivy GUI Tutorial #5
Lien : https://www.youtube.com/watch?v=k4QCoS-hj-s&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=5

Dans ce programme, les configurations des widgets sont effectuées dans un fichier à part établi à partir de
Sublime Text (my.kv), ce qui permet d'alléger le programme ci-dessous.
Par rapport au programme précédent, le constructeur n'est plus présent car il a été initialisé dans le fichier my.kv

Éditeur : Laurent REYNAUD
Date : 11-01-21
"""

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce fichier


# from kivy.properties import ObjectProperty  # lien <-> le fichier kv et ce fichier pour exécuter la fonction du bouton


class MyGridLayout(Widget):
    """Classe permettant de configurer les widgets à afficher"""

    # name = ObjectProperty(None)
    # pizza = ObjectProperty(None)
    # color = ObjectProperty(None)

    def press(self):
        """Texte à afficher après avoir appuyé sur le bouton"""

        """Assignation des champs de saisis"""
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        """Affichage du texte après avoir appuyé sur le bouton"""
        # self.add_widget(Label(text=f"Salut {name}, tu aimes la pizza {pizza}, et ta couleur favorite est {color}"))
        print(f"Salut {name}, tu aimes la pizza {pizza}, et ta couleur favorite est {color}")

        """Réinitialisation des champs de saisis"""
        self.name.text = ''
        self.pizza.text = ''
        self.color.text = ''


class MyApp(App):
    """Classe permettant de construire les widgets à partir de la classe ci-dessus"""

    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
