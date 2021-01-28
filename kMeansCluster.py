import sys
sys.path.append('./')
from kMeansInitialization import my_plot

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf


class Handler:
    def on_cluster_window_destroy(self, *args):
        Gtk.main_quit()
        
        
    def on_field_x_focus_out_event(self, *args):
        print("Pressed x field button\n", args)
        
        
    def on_field_y_focus_out_event(self, *args):
        print("Pressed y field button", args)
        
        
    def on_and_or_not_x_focus_out_event(self, *args):
        print("Pressed x... button", args)
        
        
    def on_and_or_not_y_focus_out_event(self, *args):
        print("Pressed y... button", args)
    
    
    def on_field1_expression_focus_out_event(self, entry, _):
        print(entry.get_text())


    def on_field2_expression_focus_out_event(self, entry, _):
        print(entry.get_text())


    def onCreateCluster(self, area):
        image = Gtk.Image()
        image.new_from_file("/etc/favicon.png")
               
    
    def onResizeCluster(self, x, y):
        print(f"{x} pixels wide, {y} pixels high")
        
            
    def onLoadCluster(self, *args):
        my_plot()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file("/var/tmp/plot.png")
        builder.get_object("cluster_area").set_from_pixbuf(pixbuf)
                
        

builder = Gtk.Builder()
builder.add_from_file("./cluster.glade")
builder.connect_signals(Handler())

window = builder.get_object("cluster_window")
window.show_all()

Gtk.main()
