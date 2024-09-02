from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'user': 'root',
    'password': 'mila9970',  
    'host': 'localhost',
    'database': 'ehr_security'
}

# Connect to the database
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    return render_template('lessons.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/lessons', methods=['GET'])
def get_lessons():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT title, content FROM lessons")
    lessons = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify({'lessons': lessons})

if __name__ == '__main__':
    app.run(debug=True)
