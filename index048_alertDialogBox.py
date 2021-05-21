"""
Kivy - Codemy.com #048 : Alert Dialog Boxes For KivyMD - Python Kivy GUI Tutorial #48
Lien : https://www.youtube.com/watch?v=tToJBfDgCsc

Dans ce programme on apprend à créer un message d'alerte
Lien sur KivyMd concernant ce widget () qui est insauré cette fois-ci sur le fichier python :
https://kivymd.readthedocs.io/en/latest/components/dialog/

Éditeur : Laurent REYNAUD
Date : 21-05-21
"""

from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script
from kivymd.app import MDApp  # récupération de KivyMD
from kivymd.uix.dialog import MDDialog  # message d'alerte
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton


class MainApp(MDApp):  
    # classe permettant de construire les widgets : MDApp en argument car on a recours à la bibliothèque KivyMD

	dialog = None

	def build(self):

		self.theme_cls.theme_style = "Dark" # fond de la fenêtre de couleur noire
		self.theme_cls.primary_palette = "BlueGray"  # couleur par défaut des widgets
        # cette instruction va récupérer le nom du fichier .kv à lier avec ce script
		return Builder.load_file('index048_alertDialogBox.kv')

	def show_alert_dialog(self):
		# méthode pour afficher une nouvelle fenêtre de message d'alerte
		
		if not self.dialog:
			self.dialog = MDDialog(
				title = "Mon 1er message d'alerte",
				text = "C'est juste un texte qui va ici...",
				buttons =[
                    MDFlatButton(
                        text = "Quand j'appuie ici je quitte", text_color=self.theme_cls.primary_color, 
                        on_release = self.close_dialog
                    	),
                    MDRectangleFlatButton(
                        text = "Un nouveau message va s'afficher", text_color=self.theme_cls.primary_color, 
                        on_release = self.neat_dialog
                    	),
                	],
				)
		self.dialog.open()

	def close_dialog(self, obj):
		# méthode permettant de fermer la fenêtre de message d'alerte
		
		self.dialog.dismiss()

	def neat_dialog(self, obj):
		# méthode permettant de fermer la fenêtre de message d'alerte et de changer le texte

		# fermeture de la fenêtre de message d'alerte
		self.dialog.dismiss()

		# changement du texte central de la fenêtre principal
		self.root.ids.my_label.text = "Fenêtre de message d'alerte fermée !"

if __name__ == '__main__':
    MainApp().run()