"""
Kivy - Codemy.com #049 : Build An Image Swiper App For KivyMD - Python Kivy GUI Tutorial #49
Lien : https://www.youtube.com/watch?v=gDLjaMF15mk

Dans ce programme on apprend à créer une application avec un balayage de photos

Lien sur KivyMd concernant ce widget (MDSwiper) :
https://kivymd.readthedocs.io/en/latest/components/mdswiper/?highlight=swiper#

Éditeur : Laurent REYNAUD
Date : 27-05-21
"""

from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script
from kivymd.app import MDApp  # récupération de KivyMD


class MainApp(MDApp):  
    # classe permettant de construire les widgets : MDApp en argument car on a recours à la bibliothèque KivyMD

	def build(self):

		self.theme_cls.theme_style = "Dark" # fond de la fenêtre de couleur noire
		self.theme_cls.primary_palette = "BlueGray"  # couleur par défaut des widgets
        # cette instruction va récupérer le nom du fichier .kv à lier avec ce script
		return Builder.load_file('index049_imageSwiper.kv')


if __name__ == '__main__':
    MainApp().run()