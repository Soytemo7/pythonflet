import flet as ft
# pip install openpyxl
from openpyxl import Workbook
from datetime import datetime

def main(page:ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.title = "DataTable en Flet con Excel"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER

    titulo = ft.Text(value="DataTable en Flet",size=24,color=ft.Colors.WHITE)

    data_table = ft.DataTable(
        bgcolor=ft.Colors.BLUE_GREY_700,
        border=ft.border.all(width=2,color=ft.Colors.BLUE_GREY_200),
        border_radius=10,
        vertical_lines=ft.border.BorderSide(3,ft.Colors.BLUE_GREY_200),
        horizontal_lines=ft.border.BorderSide(1,ft.Colors.BLUE_GREY_400),
        columns=[
            ft.DataColumn(ft.Text(value="ID",color=ft.Colors.BLUE_200)),
            ft.DataColumn(ft.Text(value="Nombre",color=ft.Colors.BLUE_200)),
            ft.DataColumn(ft.Text(value="Edad",color=ft.Colors.BLUE_200)),
        ],
        rows=[]
    )

    def agregar_file(e):
        nueva_fila = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(len(data_table.rows)+1),color=ft.Colors.WHITE)),
                ft.DataCell(ft.Text(nombre_input.value,color=ft.Colors.WHITE)),
                ft.DataCell(ft.Text(edad_input.value,color=ft.Colors.WHITE)) 
            ]
        )
        data_table.rows.append(nueva_fila)
        nombre_input.value = ""
        edad_input.value=""
        page.update()
    

    def guardar_excel(e):
        wb = Workbook()
        ws = wb.active
        ws.title="BBDD"
        ws.append(["ID","Nombre","Edad"])
        for row in data_table.rows:
            ws.append([cell.content.value for cell in row.cells])

            fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
            nombre_archivo = f"{fecha_hora}_datos_tabla.xlsx"
            wb.save(nombre_archivo)

            snack_bar = ft.SnackBar(content=ft.Text(f"Datos guardados en {nombre_archivo}"))
            page.overlay.append(snack_bar)
            snack_bar.open=True
            page.update()

    nombre_input = ft.TextField(label="Nombre",bgcolor=ft.Colors.BLUE_GREY_700,color=ft.Colors.WHITE)
    edad_input = ft.TextField(label="Edad",bgcolor=ft.Colors.BLUE_GREY_700,color=ft.Colors.WHITE)
    agregar_boton = ft.ElevatedButton(text="Agregar",on_click=agregar_file,color=ft.Colors.WHITE,bgcolor=ft.Colors.BLUE)
    guardar_boton = ft.ElevatedButton(text="Guardar en Excel",on_click=guardar_excel,color=ft.Colors.WHITE,bgcolor=ft.Colors.GREEN)

    input_container = ft.Row(
        controls=[nombre_input,edad_input,agregar_boton,guardar_boton],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(titulo,data_table,input_container)

ft.app(target=main)