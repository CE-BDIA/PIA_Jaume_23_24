import flet as ft


def main(page: ft.Page):
    def change_color_text(e):
        output_text.color = f"{color_dropdown.value}"
        page.update()

    output_text = ft.Text("Text amb color")
    # submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=200,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
        on_change=change_color_text
    )
    page.add(ft.Row([color_dropdown]), output_text)

ft.app(target=main)