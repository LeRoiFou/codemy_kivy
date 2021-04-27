"""
Kivy - Codemy.com #2 : Input Boxes and Buttons - Python Kivy GUI Tutorial #2
Lien : https://www.youtube.com/watch?v=S41RPtdWe78&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=2

Dans ce programme on apprend les fonctionnalités de bases de la bibliothèque kivy :
-> Affichage d'un texte
-> Affichage d'un champ de saisi
-> Nombre de colonnes à afficher
-> Bouton d'exécution avec affichage du texte souhaité lorsqu'on appuye sur le bouton

Éditeur : Laurent REYNAUD
Date : 07-01-2021
"""

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    """Classer permettant de configurer les widgets à afficher"""

    def __init__(self, **kwargs):
        """Constructeur"""

        """Appel aux attributs de la classe parente GridLayout"""
        super(MyGridLayout, self).__init__(**kwargs)

        """Assignation du nombre de colonnes requises"""
        self.cols = 2

        """1ère ligne"""
        self.add_widget(Label(text='Nom : '))  # 1ère colonne : message à afficher
        self.name = TextInput(multiline=False)  # 2ème colonne : configuration du champs de saisie sur une seule ligne
        self.add_widget(self.name)  # affichage de la 2ème colonne

        """2ème ligne"""
        self.add_widget(Label(text='Pizza favorite : '))  # 1ère colonne : message à afficher
        self.pizza = TextInput(multiline=False)  # 2ème colonne : configuration du champs de saisie sur une seule ligne
        self.add_widget(self.pizza)  # affichage de la 2ème colonne

        """3ème ligne"""
        self.add_widget(Label(text='Couleur favorite : '))  # 1ère colonne : message à afficher
        self.color = TextInput(multiline=False)  # 2ème colonne : configuration du champs de saisie sur une seule ligne
        self.add_widget(self.color)  # affichage de la 2ème colonne

        """Bouton d'exécution"""
        self.submit = Button(text='Soumettre', font_size=32)  # configuration du bouton
        self.submit.bind(on_press=self.press)  # fonction ci-dessous appliquée après avoir appuyé sur le bouton
        self.add_widget(self.submit)  # affichage du bouton

    def press(self, instance):
        """Texte à afficher après avoir appuyé sur le bouton"""

        """Assignation des champs de saisis"""
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        """Affichage du texte après avoir appuyé sur le bouton"""
        self.add_widget(Label(text=f"Salut {name}, tu aimes la pizza {pizza}, et ta couleur favorite est {color}"))

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
