from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  
from datetime import datetime
from flask_bootstrap import Bootstrap

#Creacion y configuracion de la app 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:admin@localhost:3311/flask-shopy-2687365'
app.config["SECRET_KEY"]="jefersonesmarica❤️"
bootstrap = Bootstrap(app)

#Crear los objetos de SQLalchemy y migrate 
db = SQLAlchemy(app)
migrate = Migrate(app ,
                  db )
# Creacion de Modelos 
class Cliente(db.Model):
    __tablename__= "clientes"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100) , unique = True )
    email = db.Column(db.String(120) , unique = True) 
    password = db.Column(db.String(128))

class Producto(db.Model):
    __tablename__= "productos"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    precio = db.Column(db.Numeric(precision = 10 , scale = 2))
    imagen = db.Column(db.String(100))
    
class Venta(db.Model):
    __tablename__= "ventas"
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime , default = datetime.utcnow)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    
class Detalle(db.Model):
    __tablename__= "detalles"
    id = db.Column(db.Integer, primary_key = True)
    cantidad = db.Column(db.Numeric(precision = 10 , scale = 2))
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    venta_id = db.Column(db.Integer, db.ForeignKey('ventas.id'))
    
# Denifir el formulario de registro de productos

class NuevoProductoForm(FlaskForm):
    nombre = StringField("Nombre de producto")
    precio = StringField("Precio del producto")
    submit = SubmitField("Registrar")
        
    
@app.route("/registrar_producto", methods=['GET','POST'])
def registrar():
    form= NuevoProductoForm()
    p= Producto()
    if form.validate_on_submit():
        #Registrar el producto en Base de Datos
        form.populate_obj(p)
        db.session.add(p)
        db.session.commit()
        return "Producto Registrado"
    return render_template("registrar.html",form=form)




    
                        
    