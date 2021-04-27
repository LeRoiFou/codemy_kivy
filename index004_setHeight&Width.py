"""
Kivy - Codemy.com #4 : How To Set The Height And Width of Widgets - Python Kivy GUI Tutorial #4
Lien : https://www.youtube.com/watch?v=AxKksRhcmOA&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=4

Dans ce programme on apprend à ajuster la hauteur et la largeur d'une grille comprenant des widgets ainsi que la hauteur
et la largeur d'un widget

Éditeur : Laurent REYNAUD
Date : 08-01-21
"""

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    """Classe permettant de configurer les widgets à afficher"""

    def __init__(self, **kwargs):
        """Constructeur"""

        """Appel aux attributs de la classe parente GridLayout"""
        super(MyGridLayout, self).__init__(**kwargs)

        """Configuration de la grille principale"""
        self.row_force_default = True  # arrêt de la hauteur automatique des widgets
        self.row_default_height = 120  # personnalisation de la hauteur automatique des widgets
        self.col_force_default = True  # arrêt la largeur automatique des widgets
        self.col_default_width = 100  # personnalisation de la largeur automatique des widgets
        self.cols = 1  # nombre de colonne

        """Configuration de la grille secondaire"""
        self.top_grid = GridLayout(row_force_default=True,  # arrêt de la hauteur automatique des widgets
                                   row_default_height=40,  # personnalisation de la hauteur automatique des widgets
                                   col_force_default=True,  # arrêt la largeur automatique des widgets
                                   col_default_width=100  # personnalisation de la largeur automatique des widgets
                                   )
        self.top_grid.cols = 2  # nombre de colonnes

        """1ère ligne située dans la grille secondaire"""
        self.top_grid.add_widget(Label(text='Nom : '))  # 1ère colonne : message à afficher
        self.name = TextInput()  # 2ème colonne : configuration du champs de saisie
        self.top_grid.add_widget(self.name)  # affichage de la 2ème colonne

        """2ème ligne située dans la grille secondaire"""
        self.top_grid.add_widget(Label(text='Pizza favorite : '))  # 1ère colonne : message à afficher
        self.pizza = TextInput(multiline=False)  # 2ème colonne : configuration du champs de saisie sur une seule ligne
        self.top_grid.add_widget(self.pizza)  # affichage de la 2ème colonne

        """3ème ligne située dans la grille secondaire"""
        self.top_grid.add_widget(Label(text='Couleur favorite : '))  # 1ère colonne : message à afficher
        self.color = TextInput(multiline=False)  # 2ème colonne : configuration du champs de saisie sur une seule ligne
        self.top_grid.add_widget(self.color)  # affichage de la 2ème colonne

        """Ajout de la grille secondaire dans l'application"""
        self.add_widget(self.top_grid)

        """Bouton d'exécution situé dans la grille principale tout en configurant les dimensions du bouton"""
        self.submit = Button(text='Soumettre',
                             font_size=32,  # taille de la police d'écriture
                             size_hint_y=None,  # arrêt de la hauteur automatique du widget
                             height=50,  # personnalisation de la hauteur du widget
                             size_hint_x=None,  # arrêt de la largeur automatique du widget
                             width=200  # personnalisation de la largeur du widget
                             )  # configuration du bouton
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
