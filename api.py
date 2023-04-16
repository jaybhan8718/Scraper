from flask import Flask, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # enable CORS for all routes

@app.route('/get_data', methods=['GET'])
def get_data():
    conn = sqlite3.connect('hector_project.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Scraped_Data ORDER BY Percentage DESC")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
