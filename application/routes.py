from application import app, db
from application.models import Items

@app.route('/create/item')
def create_item():
    new_item = Items(description="New Item")
    db.session.add(new_item)
    db.session.commit()
    return f"Item with id {new_item.id} added to database"

@app.route('/read/allItems')
def read_items():
    all_items = Items.query.all()
    items_dict = {"items":[]}
    for item in all_items:
        items_dict["items"].append(
            {
                "item": item.id,
                "description": item.description,
                "chemical": item.chemical
            }
        )
    return items_dict

@app.route('/update/item/<int:id>/<new_description>')
def update_item(id, new_description):
    item = Items.query.get(id)
    item.description = new_description
    db.session.commit()
    return f"Item {id} updated to {new_description}"

@app.route('/alterstatus/item/<int:id>')
def alterstatus_item(id):
    item = Items.query.get(id)
    item.chemical = True
    db.session.commit()
    return f"Item {id} status altered to chemical"