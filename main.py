#  python -m venv venv
# .\venv\Scripts\activate
# .\venv\Scripts\python.exe
# deactivate
# Ctrl + Shift + P, Select Interpreter, F:\Proyectos\pythonflet\venv\Scripts\python.exe          seleccionar interprete


# pip install flet

import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE_700
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.title = "Mi app"
    texto = ft.Text("Mi prmera app con Flet")    
    texto2 = ft.Text("Ejemplo 2")

    def cambiar_texto(e):
         texto2.value = "Suscribete"
         page.update()
        
    boton = ft.FilledButton(text="Cambiar texto",on_click=cambiar_texto)
    page.add(texto,texto2,boton)
    

ft.app(target=main)
