import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Compras"
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.padding = 20

    titulo = ft.Text(value="Lista de compras con Flet",size=30,weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE,text_align=ft.TextAlign.CENTER)

    shopping_list = ft.Column(scroll=ft.ScrollMode.AUTO)

    item_input = ft.TextField(
        hint_text="Añadir articulo...",
        border_color=ft.Colors.AMBER,
        color=ft.Colors.WHITE,
        width=300,
        text_align=ft.TextAlign.CENTER
    )

    quantity_input = ft.TextField(
        hint_text="Cantidad",
        border_color=ft.Colors.AMBER,
        color=ft.Colors.WHITE,
        width=100,
        text_align=ft.TextAlign.CENTER
    )

    categories = ["Sin categoria","Alimentos","Limpieza","Electorncia","Ropa"]

    def add_item(e):
        if item_input.value:
            quantity = quantity_input.value if quantity_input.value else "1"

            def update_category(e):
                category_text.value = f"Categoria: {e.control.value}"
                page.update()

            category_dropdown = ft.Dropdown(
                options=[ft.dropdown.Option(category) for category in categories],
                value=categories[2],
                on_change=update_category,
                color=ft.Colors.AMBER,
                width=150
            )

            category_text = ft.Text(value=f"Categoria: {categories[0]}",color=ft.Colors.AMBER_200)

            new_item = ft.ListTile(
                leading=ft.Checkbox(value=False,fill_color=ft.Colors.AMBER),
                title=ft.Text(value=f"{item_input.value} (x{quantity})",color=ft.Colors.WHITE),
                subtitle=ft.Row([
                    category_text,category_dropdown
                ],alignment=ft.MainAxisAlignment.START,spacing=10),
                trailing=ft.IconButton(
                    icon=ft.Icons.DELETE,
                    icon_color=ft.Colors.RED_400,
                    on_click=lambda _: shopping_list.controls.remove(new_item) or page.update()
                )
            )

            shopping_list.controls.append(new_item)
            item_input.value=""
            quantity_input.value=""
            page.update()

    add_button = ft.OutlinedButton(
        text="Añadir a la Lista",
        on_click=add_item,
        style=ft.ButtonStyle(
            color=ft.Colors.AMBER,
            side=ft.BorderSide(2, ft.Colors.AMBER)
        )
    )

    fila_input = ft.Row([item_input,quantity_input,add_button],alignment=ft.MainAxisAlignment.CENTER,spacing=10)

    def clear_list(e):
        shopping_list.controls.clear()
        page.update()

    clear_button = ft.IconButton(
        icon=ft.Icons.CLEANING_SERVICES,
        tooltip="Limpiar lista",
        on_click=clear_list,
        icon_color=ft.Colors.AMBER
    )

    def show_stats(e):
        total_items = len(shopping_list.controls)
        checked_items = sum(1 for item in shopping_list.controls if item.leading.value)
        category_counts = {}

        for item in shopping_list.controls:
            category = item.subtitle.controls[1].value
            category_counts[category] = category_counts.get(category, 0) + 1

        stats_text = f"Total: {total_items}, Comprados: {checked_items}, Pendientes: {total_items - checked_items}\n"
        stats_text += "Categorías:\n" + "\n".join([f"{cat}: {count}" for cat, count in category_counts.items()])

        snack = ft.SnackBar(content=ft.Text(stats_text, color=ft.Colors.BLACK), bgcolor=ft.Colors.AMBER)

        page.overlay.append(snack)
        snack.open = True
        page.update()
    
    stats_button = ft.TextButton(
        text="Estadisticas",
        on_click=show_stats,
        style=ft.ButtonStyle(
            color=ft.Colors.AMBER
        )
    )

    fila_botones = ft.Row([clear_button,stats_button],alignment=ft.MainAxisAlignment.CENTER,spacing=10)

    page.add(titulo,fila_input,fila_botones,ft.Divider(height=20,thickness=2,color=ft.Colors.AMBER),shopping_list)

ft.app(target=main)
