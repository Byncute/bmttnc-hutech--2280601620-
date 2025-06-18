from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence import RailFenceCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/encrypt_caesar", methods=['POST'])
def encrypt_caesar():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    cipher = CaesarCipher()
    encrypted = cipher.encrypt_text(text, key)
    return render_template('index.html', result_caesar=encrypted)

@app.route("/decrypt_caesar", methods=['POST'])
def decrypt_caesar():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    cipher = CaesarCipher()
    decrypted = cipher.decrypt_text(text, key)
    return render_template('index.html', result_caesar=decrypted)

@app.route("/encrypt_playfair", methods=['POST'])
def encrypt_playfair():
    text = request.form['inputPlainText']
    key = request.form['inputKey']
    cipher = PlayFairCipher()
    matrix = cipher.create_playfair_matrix(key)
    encrypted = cipher.playfair_encrypt(text, matrix)
    return render_template('index.html', result_playfair=encrypted)

@app.route("/decrypt_playfair", methods=['POST'])
def decrypt_playfair():
    text = request.form['inputCipherText']
    key = request.form['inputKey']
    cipher = PlayFairCipher()
    matrix = cipher.create_playfair_matrix(key)
    decrypted = cipher.playfair_decrypt(text, matrix)
    return render_template('index.html', result_playfair=decrypted)

@app.route("/encrypt_railfence", methods=['POST'])
def encrypt_railfence():
    text = request.form['inputPlainText']
    num_rails = int(request.form['inputNumRails'])
    cipher = RailFenceCipher()
    encrypted = cipher.rail_fence_encrypt(text, num_rails)
    return render_template('index.html', result_railfence=encrypted)

@app.route("/decrypt_railfence", methods=['POST'])
def decrypt_railfence():
    text = request.form['inputCipherText']
    num_rails = int(request.form['inputNumRails'])
    cipher = RailFenceCipher()
    decrypted = cipher.rail_fence_decrypt(text, num_rails)
    return render_template('index.html', result_railfence=decrypted)

@app.route("/encrypt_vigenere", methods=['POST'])
def encrypt_vigenere():
    text = request.form['inputPlainText']
    key = request.form['inputKey']
    cipher = VigenereCipher()
    encrypted = cipher.vigenere_encrypt(text, key)
    return render_template('index.html', result_vigenere=encrypted)

@app.route("/decrypt_vigenere", methods=['POST'])
def decrypt_vigenere():
    text = request.form['inputCipherText']
    key = request.form['inputKey']
    cipher = VigenereCipher()
    decrypted = cipher.vigenere_decrypt(text, key)
    return render_template('index.html', result_vigenere=decrypted)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
