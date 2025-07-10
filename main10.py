import flet as ft
import time

def main(page:ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.title = "Simulador de Descarga"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text(value="Simulador de Descarga de Archivos",size=24,color=ft.Colors.WHITE)

    archivos = ft.Text(value="Selecciona archivos para descargar",size=16,color=ft.Colors.WHITE70)

    file_list = ft.Column([
        ft.Checkbox(label="Documento.pdf (2.5 MB)",value=False),
        ft.Checkbox(label="Imagen.jpg (5 MB)",value=False),
        ft.Checkbox(label="Video.mp4 (50 MB)",value=False),
        ft.Checkbox(label="Archivo.zip (100 MB)",value=False)
    ])

    def simular_descarga(e):
        archivos_seleccionados = [checkbox for checkbox in file_list.controls if checkbox.value]
        
        print(archivos_seleccionados)

        if not archivos_seleccionados:
            status_text.value = "Por favor, selecciona al menos 1 archivo"
            page.update()
            return
        progress_bar.value=0
        progress_ring.value=0
        page.update()

        total_size = sum([
        float(archivo.label.split("(")[1].split(" MB")[0])
        for archivo in archivos_seleccionados])      

        downloaded = 0

        for archivo in archivos_seleccionados:
            file_size = float(archivo.label.split("(")[1].split(" MB")[0])
            status_text.value = f"Descargando {archivo.label}..."

            for _ in range(10):
                time.sleep(0.3)
                downloaded += file_size/10
                progress = min(downloaded/total_size,1)
                progress_bar.value = progress
                progress_ring.value = progress
                page.update()
        
        progress_bar.value=1
        progress_ring.value=1
        status_text.value = "Descarga completada"
        page.update()

        time.sleep(1)
        progress_bar.value=0
        progress_ring.value=0
        status_text.value=""
        for checkbox in file_list.controls:
            checkbox.value = False
        page.update()

    contenedor = ft.Container(content=file_list,padding=20)

    progress_bar = ft.ProgressBar(width=400,color="amber",bgcolor="#263238",value=0)

    progress_ring = ft.ProgressRing(stroke_width=5,color="amber",value=0)

    fila = ft.Row([progress_bar,progress_ring],alignment=ft.MainAxisAlignment.CENTER)
    
    status_text = ft.Text(value="",color=ft.Colors.WHITE)

    boton_descargar = ft.ElevatedButton(text="Iniciar Descarga", on_click=simular_descarga,bgcolor=ft.Colors.AMBER,color=ft.Colors.BLACK)

    page.add(titulo,archivos,contenedor,fila,status_text,boton_descargar)

ft.app(target=main)