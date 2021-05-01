"""Flask app for Cupcakes"""
from flask import Flask,jsonify,request,render_template
from models import db,connect_db,Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config["SECRET_KEY"] = "oh_so_secret_key"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/cupcakes/<int:cake_id>")
def show_cupcake(cake_id):
    cupcake = Cupcake.query.get_or_404(cake_id)
    return render_template("index.html",show_cupcake=cupcake)


@app.route("/api/cupcakes")
def all_cupcake():
    cupcakes = Cupcake.query.all()
    json_cupcakes = [cupcake.serialize() for cupcake in cupcakes]
    return jsonify(cupcakes=json_cupcakes)


@app.route("/api/cupcakes/<int:id>")
def cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    json_cupcake = cupcake.serialize()
    return jsonify(cupcake=json_cupcake)

@app.route("/api/cupcakes",methods=["POST"])
def add_cupcake():
    cupcake = Cupcake(
        flavor=request.json.get("flavor"),
        size=request.json.get("size"),
        rating=request.json.get("rating"),
        image=request.json.get("image")
    )

    db.session.add(cupcake)
    db.session.commit()
    return (jsonify(cupcake=cupcake.serialize()),201)

@app.route("/api/cupcakes/<int:cake_id>",methods=["PATCH"])
def update_cupcake(cake_id):
    cupcake = Cupcake.query.get_or_404(cake_id)

    cupcake.flavor = request.json.get("flavor",cupcake.flavor)
    cupcake.size = request.json.get("size",cupcake.size)
    cupcake.rating = request.json.get("rating",cupcake.rating)
    cupcake.image = request.json.get("image",cupcake.image)

    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes/<int:cup_id>",methods=["DELETE"])
def delete_cup(cup_id):
    cupcake = Cupcake.query.get_or_404(cup_id)
    db.session.delete(cupcake)

    db.session.commit()

    return jsonify(deleted=cupcake.id)

