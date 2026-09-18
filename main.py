import pyperclip
import subprocess
import flet as ft
from cryptography.fernet import Fernet


def main(page: ft.Page):
    page.title = "Crypto app"
    page.bgcolor = ft.Colors.BLACK
    page.padding = 20
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
 #---------------textfield----------------
    key_input = ft.TextField(
        label="fernet key",
        hint_text="press the key",
        password=True,
        can_reveal_password=True,
        expand=True,
        color=ft.Colors.GREEN_ACCENT,
        label_style=ft.TextStyle(color=ft.Colors.GREEN_ACCENT),
        border_color=ft.Colors.GREEN_700

    )
    message_input = ft.TextField(
        label="text",
        multiline=True,
        min_lines=2,
        color=ft.Colors.GREEN_ACCENT,
        label_style=ft.TextStyle(color=ft.Colors.GREEN_ACCENT),
        border_color=ft.Colors.GREEN_700
    )

    result_output = ft.TextField(
        label="Binary  (01)",
        multiline=True,
        min_lines=3,
        expand=True,
        read_only=True,
        color=ft.Colors.GREEN_ACCENT,
        label_style=ft.TextStyle(color=ft.Colors.GREEN_ACCENT),
        border_color=ft.Colors.GREEN_700
    
    )
#----------copy paste-----------------------------------------
    snack_bar = ft.SnackBar(
        content=ft.Text("copied!", color=ft.Colors.BLACK),
        bgcolor=ft.Colors.GREEN_ACCENT
       
    )
    page.overlay.append(snack_bar)
   
#-------------encrypt_click----------------
    def encrypt_click(e):
        try:
            cipher = Fernet(key_input.value.strip().encode())
            encrypted_bytes = cipher.encrypt(message_input.value.encode())
            
            binary_result = " ".join(format(byte, '08b') for byte in encrypted_bytes)
            result_output.value = binary_result
        except Exception:
            result_output.value = "first create a key "
        page.update()
#--------------decrypt-----------------------

    def decrypt_click(e):
        try:
            cipher = Fernet(key_input.value.strip().encode())
            
           
            binary_blocks = message_input.value.strip().split()
            
            
            encrypted_bytes = bytes(int(block, 2) for block in binary_blocks)
            
            
            decrypted = cipher.decrypt(encrypted_bytes)
            result_output.value = decrypted.decode()
        except Exception:
            result_output.value = "Warning! It's the wrong key, please try agaim"
        page.update()

    def generate_key(e):
        key_input.value = Fernet.generate_key().decode()
        page.update()

#--------------copying function--------------------------------
    def copy_click(e): 
            if (result_output.value and not result_output.value.startswith("Warning")
                                   and not result_output.value.startswith("first")):
                try:
                    pyperclip.copy(result_output.value)
                   
                    snack_bar.open = True
                except Exception as err:
                    result_output.value = f"copy error: {err}"
                   
                page.update()

    
    page.add(
        ft.Row([
            key_input,
            ft.IconButton(icon=ft.Icons.KEY, icon_color=ft.Colors.GREEN_ACCENT, on_click=generate_key)
        ]),
        message_input,
        ft.Row([
            ft.ElevatedButton(
                "encrypt", 
                bgcolor=ft.Colors.GREEN_ACCENT, 
                color=ft.Colors.BLACK, 
                on_click=encrypt_click
            ),
            ft.OutlinedButton(
                "decrypt)", 
                style=ft.ButtonStyle(color=ft.Colors.GREEN_ACCENT), 
                on_click=decrypt_click
            ),

        ]),
         ft.Row([
            result_output,
            ft.IconButton(
                icon=ft.Icons.COPY, 
                icon_color=ft.Colors.GREEN_ACCENT, 
                tooltip="copy", on_click=copy_click,
              
            )
        ])
    )

ft.app(target=main)
  