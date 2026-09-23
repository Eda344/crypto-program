import flet as ft
from cryptography.fernet import Fernet

def main(page: ft.Page):
    page.title = "Crypto app"
    
    try:
        key_input = ft.TextField(label="fernet key")
        page.add(key_input)
        page.add(ft.Text("TextFields çalışıyor"))
    except Exception as err:
        page.add(ft.Text(f"Hata: {err}"))

if __name__ == "__main__":
    ft.app(target=main)
