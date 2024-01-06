import flet as ft

def main(page: ft.Page):
    page.window_width = 800
    page.window_height = 750
    page.bgcolor = "#27374D"
    page.title = "Flashademics"
    page.padding = 20
    page.scroll = "always"
    page.horizontal_alignment = "center"
    




    page.add(
        ft.Text(value="Test Script")
    )

    page.update()

ft.app(target=main)