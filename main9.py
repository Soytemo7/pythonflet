import flet as ft

def main(page:ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.title = "Stack, Image y CircleAvatar"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "always"
    texto_titulo = ft.Text(value="Demostracion de Stack, Image y circleAvatar", size=30,weight=ft.FontWeight.BOLD,color=ft.Colors.BLUE_200)


    def create_example(title,description,content):
        return ft.Container(
            content=ft.Column([
                ft.Text(title,size=24,weight=ft.FontWeight.BOLD,color=ft.Colors.BLUE_200),
                ft.Text(description,color=ft.Colors.GREY_300),
                ft.Container(content=content,padding=10,border=ft.border.all(width=1,color=ft.Colors.BLUE_GREY_400))
            ]),
            margin=ft.margin.only(bottom=20)
        )
    
    stack_ejemplo = ft.Stack([
        ft.Container(width=200,height=200,bgcolor=ft.Colors.BLUE_900),
        ft.Container(width=150,height=150,bgcolor=ft.Colors.BLUE_700,left=25,top=25),
        ft.Container(width=100,height=100,bgcolor=ft.Colors.BLUE_900,left=50,top=50),
        ft.Text(value="Stack Demo",color=ft.Colors.WHITE,size=12,left=70,top=90)        
    ],width=200,height=200)

    stack_example = create_example(title="Stack",description="Stack permite superponer widgets uno encima de otro",content=stack_ejemplo)     

    imagen_internet = ft.Image(src="https://picsum.photos/200/200",width=200)
    imagen_local  = ft.Image(src="pythonflet\images\casa-kame-de-dragon-ball-3963.jpg",width=200)
    columna_imagen = ft.Column([
        imagen_internet,
        ft.Text(value="Imagen desde url",size=14,color=ft.Colors.GREY_300),
        imagen_local,
        ft.Text(value="imagen local (si esta disponible)",size=14,color=ft.Colors.GREY_300)
    ])

    imagen_example =create_example(title="Image",description="Image permite mostrar imagenes desde varias fuentes",content=columna_imagen)

    imagen_internet_avatar = ft.CircleAvatar(
        foreground_image_src="https://avatars.githubusercontent.com/u/5479691",
        radius=50
    )

    circulo_texto = ft.CircleAvatar(
        content=ft.Text(value="AB",color=ft.Colors.BLUE_GREY_800),
        radius=50,
        bgcolor=ft.Colors.BLUE_200
    )

    fila = ft.Row([imagen_internet_avatar,circulo_texto])

    circleavatar_example = create_example(
        title="CircleAvatar",
        description="Circle Avatar crea un avatar circular, util para perfiles de usuario.",
        content=fila
    )

    separador = ft.Divider(color=ft.Colors.BLUE_GREY_400)

    page.add(texto_titulo,separador,stack_example,separador,imagen_example,separador,circleavatar_example)
 
ft.app(target=main)
    
