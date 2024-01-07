import flet as ft
from lists import history_questions
from random import randint


def history_page(page: ft.Page):
    page.window_width = 800
    page.window_height = 750
    page.bgcolor = "#27374D"
    page.title = "Flashademics"
    page.padding = 20
    page.scroll = "always"
    page.horizontal_alignment = "center"

    questions = [
    ("Which ancient civilization developed the first system of writing?", "Sumerians"),
    ("Who was the founder of Buddhism?", "Siddhartha Gautama"),
    ("What was the Silk Road?", "A network of trade routes connecting the East and West"),
    ("What empire was ruled by Julius Caesar and Augustus?", "Roman Empire"),
    ("Which Chinese dynasty is known for the construction of the Great Wall?", "Qin Dynasty"),
    ("Who was Mansa Musa and why is he significant?", "Mansa Musa was the ruler of the Mali Empire and known for his pilgrimage to Mecca, showcasing Mali's wealth."),
    ("What was the significance of the Battle of Marathon?", "A decisive Greek victory over the Persians during the Persian Wars"),
    ("Who wrote 'The Prince' and what was its main theme?", "Niccolò Machiavelli; the main theme is political realism and advice for rulers"),
    ("What was the primary motivation for European exploration in the 15th century?", "Desire for new trade routes and resources"),
    ("What was the Columbian Exchange?", "The exchange of goods, ideas, and diseases between the Old World and the New World"),
    ("What was the impact of the Black Death on Europe in the 14th century?", "Significant population decline and social upheaval"),
    ("Who was Zheng He and what was his contribution to Chinese history?", "A Chinese explorer who led seven voyages during the Ming Dynasty, expanding Chinese influence"),
    ("What was the Industrial Revolution and where did it begin?", "A period of economic and technological change; it began in England"),
    ("What was the significance of the Haitian Revolution?", "First successful slave revolt leading to the establishment of the independent state of Haiti"),
    ("Who were the main leaders of the Mexican Revolution?", "Emiliano Zapata and Pancho Villa"),
    ("What was the 'White Man's Burden' and who popularized this concept?", "The idea that Europeans had a moral responsibility to civilize other cultures; popularized by Rudyard Kipling"),
    ("What was the main cause of World War I?", "Assassination of Archduke Franz Ferdinand of Austria-Hungary"),
    ("What was the Treaty of Versailles and how did it impact Germany?", "The peace treaty that ended World War I; it imposed harsh penalties on Germany, contributing to economic and political instability"),
    ("What were the main causes of the Russian Revolution of 1917?", "Social inequality, economic hardship, and the impact of World War I"),
    ("Who were the major leaders of the Allied Powers during World War II?", "Winston Churchill, Franklin D. Roosevelt, Joseph Stalin"),
    ("What was the Holocaust and how did it impact Jewish communities?", "Systematic genocide of six million Jews by the Nazis during World War II; led to profound and lasting effects on Jewish communities worldwide"),
    ("What was the Cold War and what were its main characteristics?", "A geopolitical tension between the United States and the Soviet Union, characterized by ideological and political rivalry"),
    ("What was apartheid and in which country did it occur?", "A system of racial segregation in South Africa"),
    ("What was the Green Revolution and how did it impact agriculture?", "Introduction of new technologies and crop varieties, leading to increased agricultural productivity"),
    ("What were the causes and consequences of the Iranian Revolution in 1979?", "Causes included dissatisfaction with the Shah's regime; consequences included the establishment of an Islamic Republic"),
    ("Who was Nelson Mandela and what role did he play in South Africa's history?", "Anti-apartheid activist and the first black president of South Africa, promoting reconciliation and unity"),
    ("What was the Rwandan Genocide and what were its root causes?", "Ethnic violence resulting in the mass killing of Tutsis by Hutus; root causes included historical tensions and political manipulation"),
    ("What is globalization and how has it affected economies and cultures?", "The increasing interconnectedness of the world; it has led to economic interdependence and cultural exchange"),
    ("What is the significance of the United Nations in global affairs?", "An international organization aimed at maintaining peace and cooperation among nations"),
    ("What is the concept of 'total war' and how did it manifest during the 20th century?", "A conflict involving all aspects of a society; manifested in both World Wars with widespread mobilization and civilian involvement")
]

    
    question_count = len(questions)

    def display_question(e):
        answer_text.value = ""
        global random_question
        random_question = randint(0, question_count-1)
        question_text.value = questions[random_question][0]
        page.update()

    def display_answer(e):
        answer_text.value = questions[random_question][1]
        page.update()

    title_label = ft.Container(
        content=ft.Text(value="AP World History", size=25, color="white"),
        margin=20
    )
    button_row = ft.Row(
        alignment="center",
        #height=250,
        controls=[
            ft.ElevatedButton(bgcolor="#00818A", color="white", text="Next Question", width=160, on_click=display_question),
            ft.ElevatedButton(bgcolor="#00818A", color="white", text="Answer", width=160, on_click=display_answer), 
        ]
    )

    question_container_header = ft.Text(value="Question:", size=20, color="white", text_align="center", width=600, bgcolor="")

    answer_container_header = ft.Text(value="Answer:", size=20, color="white", text_align="center", width=600, bgcolor="")

    question_text = ft.Text(value="", size=20, color="white", text_align="center", width=600)

    answer_text = ft.Text(value="", size=20, color="white", text_align="center", width=600)

    content_layout = ft.Column(
        width=600,
        horizontal_alignment="center",
        controls=[
            ft.Container(
                content=ft.Stack(
                    controls=(
                        ft.Container((question_container_header), margin=10),
                        ft.Container((question_text), margin=55),
                    ),
                ),
                bgcolor="#526D82",
                width=600,
                height=250,
                border_radius=6,
                #padding=ft.padding.symmetric(85)
                    
            ),
            ft.Container(
                content=button_row, margin=10,
            ),
            ft.Container(
                content=ft.Stack(
                    controls=(
                        ft.Container((answer_container_header), margin=10),
                        ft.Container((answer_text), margin=80),
                    ),
                ),
                bgcolor="#526D82",
                width=600,
                height=250,
                border_radius=6,
                #padding=ft.padding.symmetric(90),
            )
                
        ]
    )


    page.add(
        title_label,
        content_layout,

    )

    page.update()

    
ft.app(target=history_page)
