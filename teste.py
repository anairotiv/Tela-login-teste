import sqlite3
from flask_cors import CORS
from flask import Flask, request


app = Flask(__name__)
#CORS(app)

@app.route('/save_data', methods=['POST'])
def save_data_route():
    print("estou aqui")
    data = request.get_json()
    print(data)
    save_data(data['name'], data['email'], data['phone'])
    return 'Dados salvos com sucesso!'

def save_data(name, email, phone):
    conn = sqlite3.connect('cadastro.db')
    c = conn.cursor()
    c.execute("INSERT INTO usuario VALUES (?, ?, ?)", (name, email, phone))
    conn.commit()
    conn.close()
