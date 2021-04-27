"""
Kivy - Codemy.com #1 : Intro To Kivy - Installing Kivy on Windows - Python Kivy GUI Tutorial #1
Lien : https://www.youtube.com/watch?v=dLgquj0c5_U&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=1

Dans ce programme on apprend à installer kivy qui est assez spécifique.
-> création d'un nouveau projet en sélectionnant Virtuelenv dans l'environnement utilisé
-> installation des packages Cython et Kivy
Lien pour installer l'outil kivy :
https://stackoverflow.com/questions/49971489/how-do-i-get-kivy-installed-in-a-pycharm-virtualenv

kivy est installé dans un environnement virtuel car on installant le package kivy, d'autres packages se sont installés

Éditeur : Laurent REYNAUD
Date : 07-01-2021
"""

import kivy
from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        return Label(text='Hello World !', font_size=72)


if __name__ == '__main__':
    MyApp().run()
