import flet as ft



tf_user = ft.TextField(label="User Input", width=500, height=300, multiline=True, max_lines=15, min_lines=9, border_radius=55)
text_gpt = ft.TextField(label="GPT Text", color="#A78B71", multiline=True, max_lines=10, min_lines=15, border_radius=25, width=1500, height=500)

def create_row_1():
    container = ft.Container(
        width=300,
        height=500,
        content=tf_user,
        padding = ft.Padding(20,20,20,20),
    )

    card = ft.Card(
        elevation=15,
        color="#63719C",
        width=1500,
        height=100,
        content=container,
    )
    return ft.Row([
        card
    ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
def create_row_3():
    return ft.Row([
        text_gpt
    ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
def main(page: ft.Page):
    page.title ="FletGPT"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#dbe8f1"
    page.window_maximized = True

    r1 = create_row_1()

    def click_button(e):
        from GPT_Core import send_request
        text_gpt.value = send_request(tf_user.value)
        text_gpt.update()
        page.update()

    bt = ft.OutlinedButton(text="Send", width=350, height=50, on_click=click_button)
    row = ft.Row([
        bt,
    ],
        alignment=ft.MainAxisAlignment.END,
    )
    container =ft.Container(
        height=150,
        padding=ft.Padding(0, 0, 200, 0),
        content=row,
    )
    r3 = create_row_3()

    column = ft.Column(
        [
            r1,
            container,
            r3
        ],
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

    )

    page.add(column)

ft.app(target=main)