import tkinter as tk
from tkinter import filedialog
import gmsh

class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI App")

        self.create_menu()
        self.create_canvas()

    def create_menu(self):
        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Load", command=self.load_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        menubar.add_cascade(label="File", menu=file_menu)

        self.root.config(menu=menubar)

    def create_canvas(self):
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(fill="both", expand=True)

    def new_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as new_file:
                new_file.write("")  # Creates an empty file

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Gmsh files", "*.msh")])
        if file_path:
            gmsh.initialize()
            gmsh.open(file_path)
            self.canvas.delete("all")  # Clear existing content
            gmsh.fltk.run()
            gmsh.finalize()

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            file_content = ""  # You can't save Gmsh geometry as text content
            with open(file_path, "w") as save_file:
                save_file.write(file_content)

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()