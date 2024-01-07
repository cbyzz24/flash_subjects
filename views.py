import flet as ft
from lists import civics_questions
from lists import history_questions
from civics import civics_page
from history import history_page


def views_handler(page):
    return{
        "/":ft.View(
            route="/",
            controls=[
                ft.Container(
                    height = 400,
                    width = 400,
                    bgcolor = "red",

                )
            ]
        ),

        "/civics":ft.View(
            route="/civics",
            controls=[
                civics_page,
            ]
        ),

         "/history":ft.View(
            route="/history",
            controls=[
                history_page,
            ]
        ),
        
    }