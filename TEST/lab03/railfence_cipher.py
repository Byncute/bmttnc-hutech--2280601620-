import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.railfence import Ui_MainWindow  # Đảm bảo đúng đường dẫn
import requests

class RailFenceApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key.text()
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                encrypted = response.json()["encrypted_text"]
                self.ui.txt_cipher_text.setText(encrypted)
                self.show_message("Encrypted successfully.")
            else:
                self.show_message("API error: " + str(response.status_code))
        except Exception as e:
            self.show_message(f"Request failed: {str(e)}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": self.ui.txt_key.text()
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                decrypted = response.json()["decrypted_text"]
                self.ui.txt_plain_text.setText(decrypted)
                self.show_message("Decrypted successfully.")
            else:
                self.show_message("API error: " + str(response.status_code))
        except Exception as e:
            self.show_message(f"Request failed: {str(e)}")

    def show_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RailFenceApp()
    window.show()
    sys.exit(app.exec_())
