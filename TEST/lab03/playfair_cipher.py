import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.playfair import Ui_MainWindow
import requests

class PlayfairApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url_matrix = "http://127.0.0.1:5000/api/playfair/creatematrix"
        url_encrypt = "http://127.0.0.1:5000/api/playfair/encrypt"
        key = self.ui.txt_key.text()
        plain_text = self.ui.txt_plain_text.toPlainText()

        if not key.isalpha():
            self.show_message("Key chỉ được chứa chữ cái (A-Z, a-z). Vui lòng nhập lại.")
            return

        try:
            # Gọi API tạo ma trận
            res_matrix = requests.post(url_matrix, json={"key": key})
            if res_matrix.status_code == 200:
                matrix = res_matrix.json()["playfair_matrix"]
                self.ui.txt_matrix.setText(self.format_matrix(matrix))

            # Gọi API mã hóa
            res_encrypt = requests.post(url_encrypt, json={"plain_text": plain_text, "key": key})
            if res_encrypt.status_code == 200:
                encrypted = res_encrypt.json()["encrypted_text"]
                self.ui.txt_cipher_text.setText(encrypted)
                self.show_message("Encrypted successfully.")

        except Exception as e:
            self.show_message(f"Error: {str(e)}")

    def call_api_decrypt(self):
        url_matrix = "http://127.0.0.1:5000/api/playfair/creatematrix"
        url_decrypt = "http://127.0.0.1:5000/api/playfair/decrypt"
        key = self.ui.txt_key.text()
        cipher_text = self.ui.txt_cipher_text.toPlainText()

        if not key.isalpha():
            self.show_message("Key chỉ được chứa chữ cái (A-Z, a-z). Vui lòng nhập lại.")
            return

        try:
            # Gọi API tạo ma trận
            res_matrix = requests.post(url_matrix, json={"key": key})
            if res_matrix.status_code == 200:
                matrix = res_matrix.json()["playfair_matrix"]
                self.ui.txt_matrix.setText(self.format_matrix(matrix))

            # Gọi API giải mã
            res_decrypt = requests.post(url_decrypt, json={"cipher_text": cipher_text, "key": key})
            if res_decrypt.status_code == 200:
                decrypted = res_decrypt.json()["decrypted_text"]
                self.ui.txt_plain_text.setText(decrypted)
                self.show_message("Decrypted successfully.")

        except Exception as e:
            self.show_message(f"Error: {str(e)}")

    def format_matrix(self, matrix):
        # Chuyển danh sách 2D thành chuỗi có định dạng lưới
        return "\n".join(["  ".join(row) for row in matrix])

    def show_message(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlayfairApp()
    window.show()
    sys.exit(app.exec_())
