import flet as ft
from lists import civics_questions
from lists import history_questions


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
                ft.Container(
                    height = 400,
                    width = 400,
                    bgcolor = "blue",

                )
            ]
        ),

         "/history":ft.View(
            route="/history",
            controls=[
                ft.Container(
                    height = 400,
                    width = 400,
                    bgcolor = "orange",

                )
            ]
        ),
        
    }