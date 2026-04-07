from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# ==============================
# DATABASE
# ==============================
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS alumni (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        nim TEXT,
        tahun_masuk TEXT,
        tanggal_lulus TEXT,
        fakultas TEXT,
        prodi TEXT
    )''')

    conn.commit()
    conn.close()

init_db()

# ==============================
# ROUTES
# ==============================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    name = request.args.get('name', '')
    nim = request.args.get('nim', '')
    tahun_masuk = request.args.get('tahun_masuk', '')
    tanggal_lulus = request.args.get('tanggal_lulus', '')
    fakultas = request.args.get('fakultas', '')
    prodi = request.args.get('prodi', '')

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    query = "SELECT * FROM alumni WHERE 1=1"
    params = []

    if name:
        query += " AND name LIKE ?"
        params.append(f"%{name}%")
    if nim:
        query += " AND nim LIKE ?"
        params.append(f"%{nim}%")
    if tahun_masuk:
        query += " AND tahun_masuk LIKE ?"
        params.append(f"%{tahun_masuk}%")
    if tanggal_lulus:
        query += " AND tanggal_lulus LIKE ?"
        params.append(f"%{tanggal_lulus}%")
    if fakultas:
        query += " AND fakultas LIKE ?"
        params.append(f"%{fakultas}%")
    if prodi:
        query += " AND prodi LIKE ?"
        params.append(f"%{prodi}%")

    c.execute(query, params)
    data = c.fetchall()
    conn.close()

    return jsonify(data)

# ==============================
# RUN
# ==============================
if __name__ == '__main__':
    app.run(debug=True)