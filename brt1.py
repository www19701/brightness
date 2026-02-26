import gi
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class BrightnessSlider(Gtk.Window):
    def __init__(self):
        super().__init__(title="Brightness Control")
        self.set_default_size(300, 50)

        # Create a horizontal scale (slider) from 1 to 100
        self.adjustment = Gtk.Adjustment(value=43, lower=1, upper=100, step_increment=1)
        self.slider = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=self.adjustment)
        self.slider.set_digits(0)
        self.slider.connect("value-changed", self.on_value_changed)

        self.add(self.slider)

    def on_value_changed(self, widget):
        value = int(widget.get_value())
        # Call GhostBSD backlight CLI tool
        subprocess.run(["backlight", str(value)])

win = BrightnessSlider()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
