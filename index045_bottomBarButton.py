"""
Kivy - Codemy.com #045 : Create A Bottom Bar Button with KivyMD - Python Kivy GUI Tutorial #45
Lien : https://www.youtube.com/watch?v=TjloR7XLTF4

Dans ce programme on apprend à créer une barre de menu située en haut de l'écran principal,
ainsi qu'une barre de menu située elle, en bas de l'écran principal, ainsi que l'insertion
d'un bouton en bas de cette barre de menu

Lien sur KivyMd concernant ce widget : https://kivymd.readthedocs.io/en/latest/components/toolbar/

Éditeur : Laurent REYNAUD
Date : 30-04-2021
"""

from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script
from kivymd.app import MDApp  # récupération de KivyMD


class MainApp(MDApp):  
    # classe permettant de construire les widgets : MDApp en argument car on a recours à la bibliothèque KivyMD

	def build(self):
		self.theme_cls.theme_style = "Dark" # fond de la fenêtre de couleur noire
		self.theme_cls.primary_palette = "BlueGray"  # couleur des widgets
        # cette instruction va récupérer le nom du fichier .kv à lier avec ce script
		return Builder.load_file('index045_bottomBarButton.kv')

	def presser(self):
		self.root.ids.my_label.text = "Tu as appuyé sur le bouton !"


if __name__ == '__main__':
    MainApp().run()
