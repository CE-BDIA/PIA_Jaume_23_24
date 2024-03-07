import flet as ft
import time

def main(page: ft.Page):
    page.title = "Hello world with Flet!!"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    
    text = ft.Text()
    page.add(text) # és una abreviatura de page.controls.append(t) i page.update()

    for i in range(10):
        text.value = f"Pas número {i}"
        page.update()
        time.sleep(1)

ft.app(target=main)