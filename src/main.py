
from dataclasses import dataclass
from tkinterdnd2 import TkinterDnD
from tkinter import filedialog
from typing import List
from ui import Viewport
from PIL import Image

import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Application( TkinterDnD.Tk ):

    def __init__( self ):

        super().__init__()

        self.title("Pokedex")
        self.geometry("800x500")
        self.resizable(False, False)

        self.view = self.start()


    def load(self) -> None:
        path = filedialog.askopenfilename(
            filetypes=[("Imagens", "*.png *.jpg *.jpeg *.webp")]
        )

        if path:
            self.process_image(path)


    def on_drop(self, event) -> None:
        path = event.data.strip("{}")
        self.process_image(path)


    def process_image(self, path) -> None:
        try:
            img = Image.open(path)

            ctk_img = ctk.CTkImage(
                img, size=(200, 200)
            )

            self.view.center.result.empty.destroy()

            self.view.center.result.data.img.configure(
                image=ctk_img
            )

            self.view.center.result.tkraise()
        
        except Exception as e:
            self.view.center.input.label.configure(text=f"Erro: {e}")


    def start(self) -> Viewport:
        
        view = Viewport( self )

        view.top.tab_Entrada.configure(
            command=lambda: self.view.center.input.tkraise()
        )

        view.top.tab_Resultado.configure(
            command=lambda: self.view.center.result.tkraise()
        )

        view.center.input.drop_area.dnd_bind(
            "<<Drop>>", self.on_drop  
        )
        
        view.center.input.btn_load.configure(
            command=lambda: self.load()
        )
        
        return view


if __name__ == "__main__":

    Application().mainloop()

