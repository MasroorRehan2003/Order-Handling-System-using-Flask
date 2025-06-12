from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from models import Order, ActionLog

app = Flask(__name__)

orders = []  
logs = []    



@app.route('/')
def home():
    return render_template('orders.html', orders=orders)


@app.route('/add', methods=['POST'])



def add_order():
    
    new_order = Order.from_form(request.form)
    
    if any(o.order_id == new_order.order_id for o in orders):
        return "Error: Order ID already exists", 400
    
    orders.append(new_order)
    logs.append(ActionLog("Created", "Admin", datetime.now(), new_order.order_id))
    
    return redirect(url_for('home'))




@app.route('/edit/<order_id>', methods=['POST'])
def edit_order(order_id):
    for order in orders:
        
        if order.order_id == order_id:
            order.update(request.form)
            logs.append(ActionLog("Edited", "Admin", datetime.now(), order_id))
            
            break
    return redirect(url_for('home'))




@app.route('/delete/<order_id>')

def delete_order(order_id):
    
    global orders
    
    orders = [o for o in orders if o.order_id != order_id]
    
    logs.append(ActionLog("Deleted", "Admin", datetime.now(), order_id))
    
    return redirect(url_for('home'))




@app.route('/deliver/<order_id>')


def mark_delivered(order_id):
    for order in orders:
        if order.order_id == order_id:
            order.status = "Delivered"
            logs.append(ActionLog("Marked Delivered", "Admin", datetime.now(), order_id))
            
            break
    return redirect(url_for('home'))




@app.route('/logs')
def view_logs():
    return render_template('logs.html', logs=logs)




if __name__ == '__main__':
    app.run(debug=True)
