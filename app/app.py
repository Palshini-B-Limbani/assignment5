from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Read DB host from environment variable (Jenkins override)
    db_host = os.getenv("DB_HOST", "db")

    try:
        conn = mysql.connector.connect(
            host=db_host,
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
    
    except Exception as error:
        # For CI testing (no DB available)
        return f"DB Connection Failed on host: {db_host} — App is Running! ✅"
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
