import flet as ft
import random

def main(page:ft.Page):
    page.bgcolor=ft.Colors.BLUE_GREY_800
    page.title ="Juego de Adivinanzas"
    page.theme_mode =ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment =ft.MainAxisAlignment.CENTER
    titulo = ft.Text(value="Cards, Divider y VerticalDivider",size=30,weight=ft.FontWeight.BOLD)     

    numero_secreto = random.randint(1,10)
    intentos = 0
    def verificar_intento(e):
        nonlocal intentos
        intento = int(input_numero.value)
        intentos += 1
        if intento == numero_secreto:
            resultado.value = f"Correcto, adivinaste en {intentos} intentos"
            resultado.color = ft.Colors.GREEN
            verificar_btn.disabled = True
        elif intento < numero_secreto:
            resultado.value = "Demasiado Bajo. Intenta de nuevo"
            resultado.color =ft.Colors.ORANGE
        else:
            resultado.value="Demasiado alto. Intenta de nuevo"
            resultado.color =ft.Colors.ORANGE
        
        intentos_text.value=f"Intentos: {intentos}"
        page.update()
    
    
    def reiniciar_juego(e):
        nonlocal numero_secreto,intentos
        numero_secreto =random.randint(1,10)
        intentos=0
        resultado.value = "Adivina el numero entre 1 y 10"
        resultado.color = ft.Colors.WHITE
        intentos_text.value = "Intentos: 0"
        verificar_btn.disabled = False
        page.update()

    titulo_juego = ft.Text(value="Juego de Adivinanza",size=20,weight=ft.FontWeight.BOLD)
    input_numero = ft.TextField(label="Tu intento",width=100)
    verificar_btn = ft.ElevatedButton(text="Verificar",on_click=verificar_intento)
    resultado = ft.Text("Adivina el numero entre 1 y 10")
    intentos_text = ft.Text("Intentos: 0")
    reiniciar_btn = ft.ElevatedButton(text="Reiniciar juego",on_click=reiniciar_juego)
    
    card_simple = ft.Card(
        content=ft.Container(
            content=ft.Text("Esta es una card simple"),
            padding=10
        ),
        width=200,
        height=100
    ) 


    divider_simple = ft.Divider(height=1,color=ft.Colors.BLUE_200)
    divider_vertical = ft.VerticalDivider(width=1,color=ft.Colors.BLUE_200)

    card1 = ft.Card(
        content=ft.Container(
            content=ft.Column([titulo_juego,input_numero,verificar_btn,resultado,intentos_text,reiniciar_btn],alignment=ft.MainAxisAlignment.CENTER,spacing=20),
            padding=10
        ),
        width=300,
        height=400
    ) 

    def cambiar_tema(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.bgcolor = ft.Colors.BLUE_GREY_100
            tema_btn.text = "Modo Oscuro"
        else:
            page.theme_mode = ft.ThemeMode.DARK
            page.bgcolor = ft.Colors.BLUE_GREY_800
            tema_btn.text = "Modo Claro"
        page.update()
        
    titulo_tema = ft.Text(value="Cambiar Tema",size=20,weight=ft.FontWeight.BOLD)
    tema_btn = ft.ElevatedButton(text="Modo Claro",on_click=cambiar_tema)

    columa_tema = ft.Column([titulo_tema,tema_btn],alignment=ft.MainAxisAlignment.CENTER,spacing=20)

    card2 = ft.Card(
        content=ft.Container(
            content=columa_tema,
            padding=10
        ),
        width=200,
        height=150
    ) 

    layout = ft.Row([
        card1,
        divider_vertical,
        card2
    ],alignment=ft.MainAxisAlignment.CENTER)

    page.add(titulo,divider_simple,layout,ft.Divider(height=1,color=ft.Colors.BLUE_200),ft.Text("Suscribete",size=20))

ft.app(target=main)
