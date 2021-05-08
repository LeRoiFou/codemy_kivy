"""
Kivy - Codemy.com #046 : Navbar With Icons with KivyMD - Python Kivy GUI Tutorial #46
Lien : https://www.youtube.com/watch?v=YynbD-netKg

Dans ce programme on apprend à crééer une barre de navigation située en bas de l'écran qui permet d'accéder
à plusieurs écrans comme si on avait des onglets
Lien sur KivyMd concernant ce widget : https://kivymd.readthedocs.io/en/latest/components/bottom-navigation/

Éditeur : Laurent REYNAUD
Date : 08-05-21
"""

from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script
from kivymd.app import MDApp  # récupération de KivyMD


class MainApp(MDApp):  
    # classe permettant de construire les widgets : MDApp en argument car on a recours à la bibliothèque KivyMD

	def build(self):

		self.theme_cls.theme_style = "Dark" # fond de la fenêtre de couleur noire
		self.theme_cls.primary_palette = "BlueGray"  # couleur par défaut des widgets
        # cette instruction va récupérer le nom du fichier .kv à lier avec ce script
		return Builder.load_file('index046_navbar.kv')


if __name__ == '__main__':
    MainApp().run()
