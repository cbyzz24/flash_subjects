import flet as ft
from views import views_handler

def main(page: ft.Page):
    page.window_width = 800
    page.window_height = 750
    page.bgcolor = "#27374D"
    page.title = "Flashademics"
    page.padding = 20
    page.scroll = "always"
    page.horizontal_alignment = "center"

    def route_change(route):
        print(page.route)
        page.views.clear()
        page.views.append(
            views_handler(ft.Page)[page.route]
        )


    page.on_route_change = route_change
    page.go("/")
    




    page.add(
        ft.Text(value="Test Script", bgcolor="green")
    )

    page.update()

ft.app(target=main)