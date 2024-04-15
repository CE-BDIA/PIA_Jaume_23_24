import flet as ft


def main(page):
    def add_task(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.on_submit = set_focus_on_textfield
        button.disabled = True
        page.update()

    def set_focus_on_textfield(e):
        new_task.focus()
        page.update()

    def check_value(e):
        if new_task.value != "":
            button.disabled = False
            new_task.on_submit = add_task
        else:
            button.disabled = True
            new_task.on_submit = set_focus_on_textfield
        button.update()

    new_task = ft.TextField(hint_text="Tasca pendent", width=300,
                            on_change=check_value, on_submit = set_focus_on_textfield)
    button = ft.ElevatedButton("Afegir", disabled=True, on_click=add_task)
    page.add(ft.Row([new_task, button]))


ft.app(target=main)
