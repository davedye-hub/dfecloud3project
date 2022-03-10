from application import app, db
from application.models import Items

@app.route('/create/item')
def create_item():
    new_item = Items(item="New Item")
    db.session.add(new_item)
    db.session.commit()
    return f"Item with id {new_item.id} added to database"