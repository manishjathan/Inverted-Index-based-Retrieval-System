import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "InvertedIndexDRS")
        self.set_border_width(10)
        self.set_size_request(200,100)

        #Layout
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 15)
        self.add(vbox)
        #Username

        self.label = Gtk.Label("Enter the word you want to search:")
        self.textEntry = Gtk.Entry()
        self.search_button = Gtk.Button(label="Search")
        self.search_button.set_size_request(20, 20)

        self.search_button.set_property("width-request", 20)
        self.search_button.set_property("height-request", 15)
        self.search_button.connect("clicked",self.search)

        vbox.pack_start(self.label, True, True, 0)
        vbox.pack_start(self.textEntry,True,True,0)
        vbox.pack_start(self.search_button,True,True,0)

        self.listbox = Gtk.ListBox()
        self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)

        chooseFile = Gtk.Button("Choose File")
        chooseFile.connect("clicked",self.on_file_clicked)

        vbox.pack_start(self.listbox,True,True,0)
        vbox.pack_start(chooseFile,True,True,0)

        chooseFolder = Gtk.Button("Choose Folder")
        chooseFolder.connect("clicked", self.on_folder_clicked)

        self.listbox2 = Gtk.ListBox()
        self.listbox2.set_selection_mode(Gtk.SelectionMode.NONE)
        vbox.pack_start(self.listbox2, True, True, 0)
        vbox.pack_start(chooseFolder,True,True,0)

    def search(self,button):
        string = self.textEntry.get_text()
        print(string)
    def on_file_clicked(self,button):
        dialog = Gtk.FileChooserDialog("Select a File",self,Gtk.FileChooserAction.OPEN,
                                       ("Cancel",Gtk.ResponseType.CANCEL,
                                       "Ok",Gtk.ResponseType.OK))
        response = dialog.run()
        if response == Gtk.ResponseType.OK:

            #Creating a row and adding it to the listbox
            row = Gtk.ListBoxRow()
            box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
            row.add(box)
            label = Gtk.Label(dialog.get_filename())
            box.pack_start(label, True, True, 0)
            self.listbox.add(row)
            self.listbox.show_all()

        elif response == Gtk.ResponseType.CANCEL:
            print("User didn't choose any file")
        dialog.destroy()

    def on_folder_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a folder", self,
                                       Gtk.FileChooserAction.SELECT_FOLDER,
                                       ("Cancel", Gtk.ResponseType.CANCEL,
                                        "Ok", Gtk.ResponseType.OK))
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            # Creating a row and adding it to the listbox
            row = Gtk.ListBoxRow()
            box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
            row.add(box)
            label = Gtk.Label(dialog.get_filename())
            box.pack_start(label, True, True, 0)
            self.listbox2.add(row)
            self.listbox2.show_all()

        elif response == Gtk.ResponseType.CANCEL:
            print("User didn't choose any folder")

        dialog.destroy()

window = MainWindow()
window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()