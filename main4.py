import flet as ft

def main(page:ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.title = "Mi cuarta app"
    page.padding = 20
    page.theme_mode="light"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def add_note(e):
        new_note = create_note("Nueva Nota")
        grid.controls.append(new_note)
        page.update()

    def delete_note(note):
        grid.controls.remove(note)
        page.update()

    def create_note(text):    

        note_content = ft.TextField(value=text,multiline=True,bgcolor=ft.Colors.BLUE_GREY_50)

        note = ft.Container(
            content=ft.Column([note_content,ft.IconButton(icon=ft.Icons.DELETE,on_click=lambda _: delete_note(note))]),
            width=200,
            height=200,
            bgcolor=ft.Colors.BLUE_GREY_100,
            border_radius=10,
            padding=10
        )
        return note

    grid = ft.GridView(
        expand=True,
        max_extent=220,
        child_aspect_ratio=1,
        spacing=10,
        run_spacing=10,
    )

    notes = [
        "Comprar leche",
        "Llmar al medico",
        "Reunion a las 3 PM"
    ]
    
    for note in notes:
        grid.controls.append(create_note(note))

    page.add(ft.Row([
        ft.Text(value="Mis notas Adhesivas",size=24,weight="bold",color=ft.Colors.WHITE),
        ft.IconButton(icon=ft.Icons.ADD,on_click=add_note,icon_color=ft.Colors.WHITE)
    ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),grid)

ft.app(target=main)