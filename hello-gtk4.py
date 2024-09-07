
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    box1 = Gtk.Box()
    button1 = Gtk.Button(label="Hello")
    button2 = Gtk.Button(label="Run!")
    button3 = Gtk.Button(label="Canel!")
    box1.append(button1)
    box1.append(button2)
    box1.append(button3)

    win.set_child(box1)
    win.present()

app = Gtk.Application()
app.connect('activate', on_activate)

app.run(None)
