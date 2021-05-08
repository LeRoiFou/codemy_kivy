"""
Kivy - Codemy.com #044 : Creating A Login Screen With KivyMD - Python Kivy GUI Tutorial #44
Lien : https://www.youtube.com/watch?v=G-Rp41BzGxg

Dans ce programme on apprend à créer une fenêtre où s'affiche le nom d'utilisateur avec le mot de passe à saisir
et deux boutons : connection et effacer

Lien sur KivyMd concernant le titre principal (MDLabel) : 
https://kivymd.readthedocs.io/en/latest/components/label/

Lien sur KivyMd concernant les champs de saisies avec des icônes (MDTextFieldRound) : 
https://kivymd.readthedocs.io/en/latest/components/text-field/

Lien sur KivyMd concernant les boutons arrondis (MDRoundFlatButton) :
https://kivymd.readthedocs.io/en/latest/components/button/#mdroundflatbutton

Éditeur : Laurent REYNAUD
Date : 26-03-21
"""

from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script
from kivymd.app import MDApp  # récupération de KivyMD


class MainApp(MDApp):  
    # classe permettant de construire les widgets : MDApp en argument car on a recours à la bibliothèque KivyMD

	def build(self):

		self.theme_cls.theme_style='Dark'  # couleur de la fenêtre
		self.theme_cls.primary_palette='BlueGray'  # couleur des boutons
		return Builder.load_file('index044_loginScreen.kv')  # accès au fichier

	def logger(self):
		self.root.ids.welcome_label.text = f"Salut {self.root.ids.user.text} !"


	def clear(self):	
		self.root.ids.welcome_label.text = "Bienvenue !"
		self.root.ids.user.text = ""
		self.root.ids.password.text = ""


if __name__ == '__main__':
	MainApp().run()
