import flet as ft
from cryptography.fernet import Fernet

def main(page: ft.Page):
    page.title = "Crypto app"
    page.bgcolor = ft.colors.BLACK
    page.padding = 20
    
    try:
        # Tüm UI kodu burada olacak
        page.add(ft.Text("Test başarılı"))
    except Exception as err:
        page.add(ft.Text(f"Hata: {err}"))

if __name__ == "__main__":
    ft.app(target=main)
