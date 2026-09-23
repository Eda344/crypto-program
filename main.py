import flet as ft
import traceback

def main(page: ft.Page):
    page.title = "Crypto app"
    page.bgcolor = "black"
    page.padding = 20
    page.scroll = "adaptive"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    try:
        from cryptography.fernet import Fernet

        key_input = ft.TextField(
            label="fernet key",
            hint_text="press the key",
            password=True,
            can_reveal_password=True,
            expand=True,
            color="greenAccent",
            border_color="green",
        )
        message_input = ft.TextField(
            label="text",
            multiline=True,
            min_lines=2,
            color="greenAccent",
            border_color="green",
        )

        result_output = ft.TextField(
            label="Binary (01)",
            multiline=True,
            min_lines=3,
            expand=True,
            read_only=True,
            color="greenAccent",
            border_color="green",
        )

        snack_bar = ft.SnackBar(
            content=ft.Text("copied!", color="black"),
            bgcolor="greenAccent",
        )
        page.overlay.append(snack_bar)

        def encrypt_click(e):
            try:
                cipher = Fernet(key_input.value.strip().encode())
                encrypted_bytes = cipher.encrypt(message_input.value.encode())
                binary_result = " ".join(format(byte, "08b") for byte in encrypted_bytes)
                result_output.value = binary_result
            except Exception:
                result_output.value = "first create a key "
            page.update()

        def decrypt_click(e):
            try:
                cipher = Fernet(key_input.value.strip().encode())
                binary_blocks = message_input.value.strip().split()
                encrypted_bytes = bytes(int(block, 2) for block in binary_blocks)
                decrypted = cipher.decrypt(encrypted_bytes)
                result_output.value = decrypted.decode()
            except Exception:
                result_output.value = "Warning! It's the wrong key, please try again"
            page.update()

        def generate_key(e):
            key_input.value = Fernet.generate_key().decode()
            page.update()

        def copy_click(e):
            if (
                result_output.value
                and not result_output.value.startswith("Warning")
                and not result_output.value.startswith("first")
            ):
                try:
                    page.set_clipboard(str(result_output.value))
                    snack_bar.open = True
                except Exception as err:
                    result_output.value = f"copy error: {err}"
                page.update()

        # Bileşenleri Ekrana Çiz
        page.add(
            ft.Row([
                key_input,
                ft.IconButton(icon="key", icon_color="greenAccent", on_click=generate_key),
            ]),
            message_input,
            ft.Row([
                ft.ElevatedButton("encrypt", bgcolor="greenAccent", color="black", on_click=encrypt_click),
                ft.OutlinedButton("decrypt", on_click=decrypt_click),
            ]),
            ft.Row([
                result_output,
                ft.IconButton(icon="copy", icon_color="greenAccent", tooltip="copy", on_click=copy_click),
            ]),
        )

    except Exception as e:
        # EĞER GİZLİ BİR HATA ÇIKARSA BEYAZ EKRAN YERİNE BURASI ÇALIŞACAK VE HATAYI YAZACAK
        err_str = traceback.format_exc()
        page.add(
            ft.Text("KRİTİK HATA OLUŞTU:", color="red", weight="bold", size=20),
            ft.Text(err_str, color="red", selectable=True)
        )

if __name__ == "__main__":
    ft.app(target=main) 
