"""
Kivy - Codemy.com #047 : Speed Dial Button Menu With KivyMD - Python Kivy GUI Tutorial #47
Lien : https://www.youtube.com/watch?v=bcy2iksM3bc

Dans ce programme lorsqu'on appuye sur un bouton, des icônces s'affichent
Lien sur KivyMd concernant ce widget (MDFloatingActionButtonSpeedDial) :
https://kivymd.readthedocs.io/en/latest/components/button/#mdfloatingactionbuttonspeeddial

Éditeur : Laurent REYNAUD
Date : 15-05-2021
"""

from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script
from kivymd.app import MDApp  # récupération de KivyMD


class MainApp(MDApp):  
    # classe permettant de construire les widgets : MDApp en argument car on a recours à la bibliothèque KivyMD

    # dictionnaire des icônes à afficher
	data = {
	'language-python': 'Python', 
	'wikipedia': 'Mon dico', 
	'google-maps': 'Mes cartes',
	'youtube': 'Vidéos'
    }

	def callback(self, instance):
		# méthode permettant de modifier le texte affiché au centre de l'écran
		
		# si on sélectionne un des icônes, le texte affichera...
		if instance.icon == 'language-python':
			lang = 'Python'
		elif instance.icon == 'wikipedia':
			lang = 'Wikipedia'
		elif instance.icon == 'google-maps':
			lang = 'Mes cartes'
		elif instance.icon == 'youtube':
			lang = 'Youtube'
		self.root.ids.my_label.text = f"Tu as appuyé sur l'icône {lang}"

	def open(self):
		# méthode permettant d'afficher le texte ci-après lorsqu'on appuye le bouton

		self.root.ids.my_label.text = f"Ouvert !"

	def close(self):
		# méthode permettant d'afficher le texte ci-après lorsqu'on appuye le bouton

		self.root.ids.my_label.text = f"Fermé !"


	def build(self):
		self.theme_cls.theme_style = "Dark" # fond de la fenêtre de couleur noire
		self.theme_cls.primary_palette = "BlueGray"  # couleur par défaut des widgets
        # cette instruction va récupérer le nom du fichier .kv à lier avec ce script
		return Builder.load_file('index047_speedDialButtonMenu.kv')

if __name__ == '__main__':
    MainApp().run()