from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('package_cars.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM package_cars")
    cars = c.fetchall()
    conn.close()
    return render_template('index.html', cars=cars)

@app.route('/add_car', methods=['POST'])
def add_car():
    car_number = request.form['car_number']
    weight = request.form['weight']
    location = request.form['location']
    action = request.form['action']

    conn = sqlite3.connect('package_cars.db')
    c = conn.cursor()
    if action == 'add':
        c.execute("INSERT INTO package_cars (car_number, weight, location, status, complete) VALUES (?, ?, ?, 'Not on site', 0)",
                  (car_number, weight, location))
    elif action == 'shift_start':
        c.execute("INSERT INTO package_cars (car_number, weight, location, status, complete) VALUES ('Shift Start', 'N/A', 'N/A', 'Shift Start', 0)")
    elif action == 'shift_end':
        c.execute("INSERT INTO package_cars (car_number, weight, location, status, complete) VALUES ('Shift End', 'N/A', 'N/A', 'Shift End', 0)")
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update_complete', methods=['POST'])
def update_complete():
    data = request.get_json()
    car_id = data['id']
    complete = data['complete']
    conn = sqlite3.connect('package_cars.db')
    c = conn.cursor()
    c.execute("UPDATE package_cars SET complete = ? WHERE id = ?", (complete, car_id))
    conn.commit()
    conn.close()
    return jsonify(success=True)

@app.route('/update_field', methods=['POST'])
def update_field():
    data = request.get_json()
    car_id = data['id']
    field = data['field']
    value = data['value']
    conn = sqlite3.connect('package_cars.db')
    c = conn.cursor()
    c.execute(f"UPDATE package_cars SET {field} = ? WHERE id = ?", (value, car_id))
    conn.commit()
    conn.close()
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
