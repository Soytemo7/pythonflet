import flet as ft
import random

def main(page:ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.title = "Tabs en Flet"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text(value="Ejemplo de Tabs en Flet",size=24,color=ft.Colors.WHITE)

    def ganerar_tareas():
        tareas = ["Hacer compra","Llamar al medico","Estudiar","Comer"]
        # return [random.choice(tareas) for _ in range(2)]
        return random.sample(tareas,4)

    lista_tareas = ft.ListView(spacing=10,padding=20)
    
    def actualizar_tareas():
        lista_tareas.controls.clear()
        for tarea in ganerar_tareas():
            lista_tareas.controls.append(ft.Text(tarea,color=ft.Colors.WHITE))
        page.update()

    actualizar_tareas()
    boton_actualizar = ft.ElevatedButton(text="Actualizar Tareas",on_click=lambda _: actualizar_tareas())
    contenido_tareas = ft.Column([lista_tareas,boton_actualizar])

    campo_nombre = ft.TextField(label="Nombre",bgcolor=ft.Colors.BLUE_GREY_700)
    campo_email = ft.TextField(label="Emnail",bgcolor=ft.Colors.BLUE_GREY_700)
    boton_guardar = ft.ElevatedButton("Guardar perfil")
    contenido_perfil = ft.Column([campo_nombre,campo_email,boton_guardar])

    switch_notificaciones = ft.Switch(label="Notificaciones",value=True)
    slider_volumen = ft.Slider(min=0,max=100,divisions=10,label="Volumen")
    contenido_config = ft.Column([switch_notificaciones,slider_volumen])

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Tareas",icon=ft.Icons.LIST_ALT,content=contenido_tareas),
            ft.Tab(text="Perfil",icon=ft.Icons.PERSON,content=contenido_perfil),
            ft.Tab(text="Configuracion",icon=ft.Icons.SETTINGS,content=contenido_config)
        ],
        expand=1
    )

    page.add(titulo,tabs)

ft.app(target=main)

