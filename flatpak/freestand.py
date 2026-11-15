#!/usr/bin/env python3
import sys, gi
gi.require_version("Gtk", "4.0")
gi.require_version("WebKit", "6.0")
from gi.repository import Gtk, WebKit, Gio

class App(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="io.github.acehern.freestand",
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = Gtk.ApplicationWindow(application=self, title="Free Stand",
                                        default_width=1100, default_height=800)
            view = WebKit.WebView()
            view.load_uri("file:///app/share/freestand/index.html")
            win.set_child(view)
        win.present()

App().run(sys.argv)
