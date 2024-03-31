import flet as ft


def main(page: ft.Page):

    def aumenta(e):
        valor = numero.value
        novo_valor = int(valor) + 1
        numero.value = str(novo_valor)
        if novo_valor % 10 == 0:
            valor_alc.value = str(novo_valor)

        linha.update()
    
    def diminui(e):
        valor = numero.value
        if int(valor) >= 1:

            novo_valor = int(valor) - 1
            numero.value = str(novo_valor)


        linha.update()


    linha = ft.Container(
        
        content=ft.Column(controls=[ft.Row(
            controls=[
        ft.Container(
            content=ft.Text(value='-'),
            width=85,
            height=55,
            bgcolor=ft.colors.AMBER,
            alignment=ft.alignment.center,
            border_radius=5,
            margin=ft.Margin(0,0,0,23),
            on_click=diminui

        ),
        numero := ft.TextField(
            width=80,
            height=80,
            value=0,
            text_align=ft.TextAlign.CENTER,
            disabled=True,
            border_color=ft.colors.BLACK,
            color=ft.colors.BLACK

        ),
        ft.Container(
            content=ft.Text(value='+'),
            width=85,
            height=55,
            bgcolor=ft.colors.AMBER,
            alignment=ft.alignment.center,
            border_radius=5,
            margin=ft.Margin(0,0,0,23),
            on_click=aumenta

        )


        ],
        alignment=ft.MainAxisAlignment.CENTER,
        
        ),
        valor_alc := ft.Text(
            color=ft.colors.BLACK
        )
        ],
        alignment=ft.MainAxisAlignment.CENTER,

        ),



        
        
    )
    
    page.add(
        ft.Container(expand=True),
        linha,
        ft.Container(expand=True),
    )




ft.app(target=main)