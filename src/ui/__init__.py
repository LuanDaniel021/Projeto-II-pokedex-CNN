
from tkinterdnd2 import DND_FILES
import customtkinter as ctk

class Viewport( ctk.CTkFrame ):

    def __init__( self, master ):

        super().__init__( master )

        self.grid_columnconfigure(0, weight=1)
        self.pack(
            expand = True,
            fill = "both"
        )

        self.top = TabControl( self )

        self.center = ContentPanel( self )
        


class TabControl( ctk.CTkFrame ):

    def __init__( self, master ):

        super().__init__( master )
        
        self.pack(
            fill="x",
            padx=5,
            pady=5
        )

        self.tab_Entrada = ctk.CTkButton( self, text="Entrada" )
        self.tab_Entrada.pack(
            side="left",
            padx=5
        )

        self.tab_Resultado = ctk.CTkButton( self, text="Resultado" )
        self.tab_Resultado.pack(
            side="left",
            padx=5
        )


class ContentPanel( ctk.CTkFrame ):

    def __init__( self, master ):

        super().__init__( master )

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        self.result = PanelResult( self )
        self.input = PanelInput( self )


# --------------------------
# PAINEL 1 - INPUT
# --------------------------
class PanelInput( ctk.CTkFrame ):

    def __init__( self, master ):

        super().__init__( master )
        
        self.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.label = ctk.CTkLabel( self, text="Arraste uma imagem aqui" )
        self.label.pack( pady=20 )

        self.img_label = ctk.CTkLabel( self, text="" )

        # --- DRAG & DROP ---
        self.drop_area = ctk.CTkFrame(
            self,
            width=300,
            height=200
        )
        self.drop_area.pack( pady=20 )

        self.drop_area_label = ctk.CTkLabel( self.drop_area, text="Solte a imagem aqui" )
        self.drop_area_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        self.drop_area.drop_target_register( DND_FILES )
        
        self.btn_load = ctk.CTkButton( self, text="Ou clique para carregar" )
        self.btn_load.pack(pady=10)


# --------------------------
# PAINEL 2 - CONTAINER RESULT
# --------------------------
class PanelResult( ctk.CTkFrame ):

    def __init__( self, master ):

        super().__init__( master )
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.grid(
            row=0,
            column=0,
            sticky="nsew"
        )
        
        self.data = PanelData( self )

        self.empty = PanelEmpty( self )


# --------------------------
# SUBPAINEL - EMPTY
# --------------------------
class PanelEmpty( ctk.CTkFrame ):

    def __init__( self, master ):

        super().__init__( master )

        self.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        label = ctk.CTkLabel(
            self,
            text="Nenhum Pokemon analisado ainda",
            font=(
                "Arial",
                18
            )
        )
        label.pack( expand=True )


# --------------------------
# SUBPAINEL - DATA
# --------------------------
class PanelData(ctk.CTkFrame):

    def __init__( self, master ):

        super().__init__( master )

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        # direita - info
        right = ctk.CTkFrame(self)
        right.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.name = ctk.CTkLabel(
            right,
            text="Nome",
            font=("Arial", 20)
        )
        self.name.pack(
            anchor="n",
            pady=10
        )

        self.desc = ctk.CTkLabel(
            right,
            text="",
            wraplength=250,
            justify="left"
        )
        self.desc.pack(
            anchor="n",
            pady=10
        )
        
        # esquerda - imagem
        self.img = ctk.CTkLabel( self, text="" )
        self.img.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

