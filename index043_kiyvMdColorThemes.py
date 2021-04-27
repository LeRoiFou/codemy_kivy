# Kivy - Codemy.com #043 : Using Color Themes For KivyMD - Python Kivy GUI Tutorial #43
# Lien : https://www.youtube.com/watch?v=bcWi_H2OqLQ

# KivyMD permet d'obtenir les widgets selon notre choix et de les générer automatiquement sur python.
# Cependant, les wigets sont déjà uniformisés, c'est pourquoi dans ce programme on apprend à choisir les couleurs
# à nos widgets.

# Liste des couleurs proposées :
# 'Red', 'Pink', 'Purple', 'DeepPurple' (violet foncé), 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal' (bleu / vert),
# 'Green', 'LightGreen','Lime' (or), 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray'

#  Lien sur le site KivyMd pour les couleurs : https://kivymd.readthedocs.io/en/latest/themes/theming/

# Éditeur : Laurent REYNAUD
# Date : 19-03-21


from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script
from kivymd.app import MDApp  # récupération de KivyMD


class MainApp(MDApp):  
    # classe permettant de construire les widgets : MDApp en argument car on a recours à la bibliothèque KivyMD

	def build(self):

    	# instructions pour les couleurs
		self.theme_cls.theme_style='Dark'
		self.theme_cls.primary_palette='DeepPurple'  # couleur des boutons
		self.theme_cls.accent_palette='Red' # je ne sais pas à quoi sert cette instruction...

        # cette instruction va récupérer le nom du fichier .kv à lier avec ce script
		return Builder.load_file('index043_kiyvMdColorThemes.kv')


if __name__ == '__main__':
    MainApp().run()
