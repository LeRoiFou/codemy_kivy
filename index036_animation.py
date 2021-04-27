"""
Kivy - Codemy.com #36 : How To Create Animation With Kivy - Python Kivy GUI Tutorial #36
Lien : https://www.youtube.com/watch?v=1fTx2oKJMOQ

Dans ce programme on apprend à animer le bouton selon les instructions définies dans la fonction animate_it() ci-après

Éditeur : Laurent REYNAUD
Date : 27-01-21
"""

from kivy.app import App
from kivy.uix.widget import Widget  # lien entre le fichier kv et ce script
from kivy.lang import Builder  # récupération du nom du fichier kv à lier avec ce script
from kivy.animation import Animation  # pour l'animation des widgets

Builder.load_file('index036_animation.kv')  # cette instruction va récupérer le nom du fichier .kv à lier avec ce script


class MyLayout(Widget):  # Widget en argument car le constructeur de la classe est dans le fichier .kv

    def animate_it(self, widget, *args):
        """Fonction permettant d'animer les widgets"""

        """Instanciation de la classe Animation() en déclarant ce que l'on souhaite faire"""
        animate = Animation(background_color=(0, 0, 1, 1),  # changement de la couleur du bouton après avoir appuyé
                            duration=3,  # temps d'écoulement de l'animation
                            opacity=0.1  # degré d'opacité du bouton après avoir appuyé
                            )

        """Seconde animation en déclarant le même nom de variable mais cette fois recourt à l'instruction +="""
        animate += Animation(opacity=1,  # degré d'opacité du bouton après l'animation ci-avant
                             duration=2,  # temps d'écoulement de l'animation
                             size_hint=(1, 1)  # changement des dimensions du bouton
                             )

        """Troisième animation"""
        animate += Animation(size_hint=(.5, .5),  # dimensions à l'origine du bouton
                             duration=3,  # temps d'écoulement de l'animation
                             )

        """Quatrième animation"""
        animate += Animation(pos_hint={'center_x': .1}  # déplacement du bouton vers la gauche
                             )

        """Cinquième animation"""
        animate += Animation(pos_hint={'center_x': .5}  # retour du bouton à sa position d'origine
                             )

        """Démarrage de l'animation"""
        animate.start(widget)  # instruction mise dans le fichier kv pour le bouton : on_release: root.animate_it(self)

        """Callback : dès que l'animation est finie, appel de la fonction my_callback ci-après"""
        animate.bind(on_complete=self.my_callback)

    def my_callback(self, *args):
        """Fonction permettant de changer le texte après avoir animé le bouton"""

        self.ids.my_label.text = 'Wow ! Tu as vu ça ?!?'


class AwesomeApp(App):  # App en argument car on a recours à la bibliothèque kivy
    """Classe permettant de construire les widgets à partir de la classe ci-dessus : le nom de la classe importe car
    l'instruction ci-dessus : 'Builder.load_file('whatever.kv')' permet de récupérer le fichier .kv à rattacher à ce
    script"""

    def build(self):
        """Dans cette fonction, on appelle la classe MyLayout() ci-dessus"""
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
