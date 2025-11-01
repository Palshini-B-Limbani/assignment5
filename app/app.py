from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    conn = mysql.connector.connect(
        host="db",
        user="root",
        password="rootpass",
        database="testdb"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS visits(id INT AUTO_INCREMENT PRIMARY KEY)")
    cursor.execute("INSERT INTO visits VALUES()")
    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM visits")
    count = cursor.fetchone()[0]
    return f"Total visits: {count}"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
