import flet as ft

def main(page: ft.Page):
    page.title = "Test"
    page.add(ft.Text("Merhaba, app çalışıyor!"))

if __name__ == "__main__":
    ft.app(target=main)
