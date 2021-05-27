"""
Récapitulatif

Widgets et les différents instructions pour Kivy

Éditeur : Laurent REYNAUD
Date : 21-05-2021
"""

# récupération du nom du fichier kv à lier avec ce script
from kivy.lang import Builder
# récupération de KivyMD
from kivymd.app import MDApp

class MainApp(MDApp):  
	"""classe permettant de construire les widgets : 
	MDApp en argument car on a recours à la bibliothèque KivyMD"""

	# dictionnaire des icônes à afficher
	# concerne MDFloatingActionButtonSpeedDial
	data = { 
	'wikipedia': 'Mon dico', 
	'google-maps': 'GPS',
	'youtube': 'Musiques',
	'volume-off': 'Muet',
    }

	def build(self):

		# fond de couleur de la fenêtre
		# -> Dark : couleur noire
		# -> Light : couleur blanche
		self.theme_cls.theme_style = "Light" 
		# couleur par défaut des widgets
		self.theme_cls.primary_palette = "BlueGray"
		# cette instruction va récupérer le nom du fichier .kv à lier avec ce script
		return Builder.load_file('recap.kv')

if __name__ == '__main__':
    MainApp().run()
