from flask import Blueprint, render_template, request, jsonify,json
from models.contact import Contact
from utils.db import db
import requests
contacts = Blueprint('contacts',__name__)

@contacts.route('/')
def home():
    return render_template('index.html')

@contacts.route('/show',methods=["GET"])
def show_contact():
    contacts =Contact.query.all()
    object=[]
    for contac in contacts:
        contactobject={
            "id":str(contac.id).strip('\"'),
            "fullname":str(contac.fullname).strip('\"'),
            "email":str(contac.email).strip('\"'),
            "phone":str(contac.phone).strip('\"')
        }
        object.append(contactobject)
    return jsonify(object)

@contacts.route('/new', methods=["POST"])
def add_contact():
    datos=request.get_json()
    fullname=datos['fullname']
    email=datos['email']
    phone=datos['phone']
    new_contact=Contact(fullname, email, phone)
    db.session.add(new_contact)
    db.session.commit()  
    return 'Datos guardados con exito'

@contacts.route('/update',methods=["POST"])
def update_contact():
    datos=request.get_json()
    id=datos['id']
    contact =Contact.query.get(id)
    contact.fullname=datos['fullname']
    contact.email=datos['email']
    contact.phone=datos['phone']
    db.session.commit()  
    return 'Contacto actualizado'

@contacts.route('/delete')
def delete_contact():
    id=request.args.get('id')
    contact =Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()  
    return 'Contacto eliminiado'

@contacts.route('/pablito', methods=["GET"])
def requets_contact():
    id=request.args.get('id')
    r = requests.get('https://reqres.in/api/users/{}'.format(id))
    re=r.json()
    print(re)
    people=[]
    peo={
        "id":re['data']['id'],
        "email":re['data']['email'],
        "nombre":re['data']['first_name']+" "+re['data']['last_name']
        }
    people.append(peo)
    return jsonify(people)

@contacts.route('/pablito1', methods=["POST"])
def ingre_contact():
    datos=request.get_json()
    data1={
        "name":datos['name'],
        "job":datos['job']
    }
    r = requests.post('https://reqres.in/api/users',data=data1)
    re=r.json()
    print(re)
    people=[]
    peo={
        "id":re['id'],
        "job":re['job'],
        "nombre":re['name'],
        "fecha":re['createdAt']
        }
    people.append(peo)
    return jsonify(people)

@contacts.route('/pablito2', methods=["POST"])
def updt_contact():
    datos=request.get_json()
    id=datos['id']
    data1={
        "name":datos['name'],
        "job":datos['job']
    }
    r = requests.put('https://reqres.in/api/users/{}'.format(id),data=data1)
    re=r.json()
    print(re)
    people=[]
    peo={
        "job":re['job'],
        "nombre":re['name'],
        "fecha":re['updatedAt']
        }
    people.append(peo)
    return jsonify(people)

@contacts.route('/pablito3', methods=["GET"])
def borrar_contact():
    id=request.args.get('id')
    r = requests.delete('https://reqres.in/api/users/{}'.format(id))
    # re=r.text()
    print(r)
    return "Borrado con exito"