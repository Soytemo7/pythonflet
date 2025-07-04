import flet as ft

def main(page:ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.title = "Mi segunda app"
    texto1 = ft.Text(value="Texto 1",size=24,color=ft.Colors.WHITE)
    texto2 = ft.Text(value="Texto 2",size=24,color=ft.Colors.WHITE)
    texto3 = ft.Text(value="Texto 3",size=24,color=ft.Colors.WHITE)

    fila_textos = ft.Row(
        controls=[texto1,texto2,texto3],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )

    boton1 = ft.FilledButton(text="Boton 1")
    boton2 = ft.FilledButton(text="Boton 2")
    boton3 = ft.FilledButton(text="Boton 3")

    fila_botones = ft.Row(
        controls=[boton1,boton2,boton3],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )    

    textos_columnas = [
        ft.Text(value="Columna 1 Fila 1",size=18,color=ft.Colors.WHITE),
        ft.Text(value="Columna 1 Fila 2",size=18,color=ft.Colors.WHITE),
        ft.Text(value="Columna 1 Fila 3",size=18,color=ft.Colors.WHITE),
    ]

    columna_texto = ft.Column(
        controls=textos_columnas
    )

    textos_columnas2 = [
        ft.Text(value="Columna 2 Fila 1",size=18,color=ft.Colors.WHITE),
        ft.Text(value="Columna 2 Fila 2",size=18,color=ft.Colors.WHITE),
        ft.Text(value="Columna 2 Fila 3",size=18,color=ft.Colors.WHITE),
    ]

    columna_texto2 = ft.Column(
        controls=textos_columnas2
    )

    fila_columnas = ft.Row(
        controls=[columna_texto,columna_texto2],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )

    page.add(fila_textos)    
    page.add(fila_botones)
    page.add(fila_columnas)
    

ft.app(target=main)

