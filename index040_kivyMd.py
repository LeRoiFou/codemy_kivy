# Kivy - Codemy.com #040 : Intro To KivyMD Installation - Python Kivy GUI Tutorial #40
# Lien : https://www.youtube.com/watch?v=ycoKlFV3-iU

# Site : https://material.io/design
# Site : https://kivymd.readthedocs.io/en/latest/index.html
# Site : https://github.com/kivymd/KivyMD

# . Créer un environnement virtuel afin de travailler dans ce répertoire et non sur l'ordinateur, aller sur GitBash et
# sur le répertoire créé puis saisir : python -m venv virt
# . Puis saisir pour accéder à cet environnement virtuel :
# source virt/Scripts/activate
# . Puis copie UNE PAR UNE du site kivymd des instructions suivantes :
#     -> git clone https://github.com/kivymd/KivyMD.git --depth 1
#     -> cd KivyMD
#     -> pip install .
# . Puis installer le module pillow : pip install Pillow
# . Puis installer le module kivy : pip install kivy
# . Saisir : 'pip freeze' pour voir tous les modules installés dans cet environnement virtuel

# kivyMd présente des modèles d'application - Dans ce cours on une démo des widgets présents et à utiliser avec Kivy
# Pour voir la démo des widgets, se mettre sur GitBash puis aller dans le répertoire :
# "C:\Users\LRCOM\PycharmProjects\codemy_kivy\kivymd\KivyMD\demos"
# Et sélectionner un des répertoires et puis saisir dans GitBash dès l'accès au répertoire souhaité : python main.py

# Éditeur : Laurent REYNAUD
# Date : 27-02-21


from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script

Builder.load_file('my_kivy.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


class MyLayout(Widget):  # Widget en argument car le constructeur de la classe est dans le fichier .kv

    pass


class AwesomeApp(App):  # App en argument car on a recours à la bibliothèque kivy
    """Classe permettant de construire les widgets à partir de la classe ci-dessus : le nom de la classe importe car
    l'instruction ci-dessus : 'Builder.load_file('whatever.kv')' permet de récupérer le fichier .kv à rattacher à ce
    script"""

    def build(self):
        """Dans cette fonction, on appelle la classe MyLayout() ci-dessus"""
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
