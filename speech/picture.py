from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget


class Pulser(Widget):
    bg_color = ObjectProperty([1, 1, 1, 1])

    def __init__(self, **kwargs):
        super(Pulser, self).__init__(**kwargs)
        Clock.schedule_once(self.start_pulsing, 2)

    def start_pulsing(self, *args):
        anim = Animation(bg_color=[1,0,0,1]) + Animation(bg_color=[1,1,1,1])
        anim.repeat = True
        anim.start(self)
        #pass


theRoot = Builder.load_string('''
Pulser:
    canvas:
        Color:
            rgba: self.bg_color
        Rectangle:
            pos: self.pos
            size: self.size
            source: './gif/loading.gif'

''')

class PulserApp(App):
    def build(self):
        return theRoot

if __name__ == "__main__":
    PulserApp().run()