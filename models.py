from datetime import datetime

class Order:
    def __init__(self, order_id, items, delivery_date, sender, recipient, address):
        self.order_id = order_id
        self.items = int(items)
        self.delivery_date = delivery_date
        self.sender = sender
        self.recipient = recipient
        self.address = address
        self.status = "Ongoing"




    def update(self, form):
        self.items = int(form['items'])
        self.delivery_date = form['delivery_date']
        self.sender = form['sender']
        self.recipient = form['recipient']
        self.address = form['address']



    @staticmethod
    def from_form(form):
        return Order(
            form['order_id'],
            form['items'],
            form['delivery_date'],
            form['sender'],
            form['recipient'],
            form['address']
        )
        
        
        

class ActionLog:
    def __init__(self, action, performed_by, timestamp, order_id):
        self.action = action
        self.performed_by = performed_by
        self.timestamp = timestamp
        self.order_id = order_id
