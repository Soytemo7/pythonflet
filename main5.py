import flet as ft
import os
import base64

def crear_producto(nombre,precio,color,imagen_nombre):

    imagen_path = os.path.join(os.path.dirname(__file__),"assets",imagen_nombre)
    try:
        with open(imagen_path,"rb") as imagen_file:
            imagen_bytes = base64.b64encode(imagen_file.read()).decode()
    except FileNotFoundError:
        print(f"Advertencia: La imagen {imagen_nombre} no existe en {imagen_path}")
        imagen_bytes=None

    return ft.Container(
        content=ft.Column([
            ft.Image(
                src_base64=imagen_bytes,
                width=150,
                height=150,
                fit=ft.ImageFit.CONTAIN,
                error_content=ft.Text("Imagen no encontrada") 
            ) if imagen_bytes else ft.Text("Imagen no encontrada"),            
            ft.Text(nombre,size=16,weight=ft.FontWeight.BOLD),
            ft.Text(value=f"${precio}",size=14),
            ft.ElevatedButton(text="Agregar al carrito",color=ft.Colors.WHITE)
        ]),
        bgcolor=color,
        border_radius=10,
        padding=20,
        alignment=ft.alignment.center
    )

def main(page:ft.Page):
    page.title = "Galeria de Productos responsiva"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
  

    productos = [
        crear_producto(nombre="Producto 1",precio=19.99,color=ft.Colors.BLUE_500,imagen_nombre="P1.jpg"),
        crear_producto(nombre="Producto 2",precio=29.99,color=ft.Colors.GREEN_500,imagen_nombre="P2.jpg"),
        crear_producto(nombre="Producto 3",precio=39.99,color=ft.Colors.ORANGE_500,imagen_nombre="P3.jpg"),
        crear_producto(nombre="Producto 4",precio=49.99,color=ft.Colors.PURPLE_500,imagen_nombre="P4.jpg")
    ]

    galeria = ft.ResponsiveRow(
        [ft.Container(producto,col={"sm":12,"md":6,"lg":3}) for producto in productos],
        run_spacing=20,
        spacing=20
    )

    contenido = ft.Column([
          ft.Text(value="Galeria de productos",size=32,weight=ft.FontWeight.BOLD),
          ft.Divider(height=20,color=ft.Colors.WHITE24),
          galeria
    ],scroll=ft.ScrollMode.AUTO,expand=True)

    page.add(contenido)

ft.app(target=main)