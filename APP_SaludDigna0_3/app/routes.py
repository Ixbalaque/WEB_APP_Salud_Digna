
from flask import Blueprint, render_template 
from flask import request 
from flask import session
from .models import db, Persona
import pandas as pd
import joblib
import os

# Especifica la ruta completa al archivo del modelo
modelo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'css', 'PMEC.joblib')

# Carga el modelo
loaded_model = joblib.load(modelo_path)


main = Blueprint('main',__name__)

@main.route('/')
def Login():
    return render_template('Login.html')

@main.route('/Login_NU')
def Login_NU():
    return render_template('Login_NU.html')

@main.route('/Salud_Digna')
def Salud_Digna():
    return render_template('Salud_Digna.html',data="")

@main.route('/submit_form_LoginNU', methods=['POST'])
def submit_form_NU():
    
    nombre=request.form.get('nombre')
    usuario=request.form.get('usuario')
    email=request.form.get('email')
    contrasena=request.form.get('contrasena')
    
    persona_existente = Persona.query.filter_by(email=email).first()
    
    ## Verificar que todos los campos estén llenos    

    if persona_existente is None:
        nueva_persona=Persona(nombre=nombre,
                            usuario=usuario,
                            email=email)
        nueva_persona.set_password(contrasena)
        db.session.add(nueva_persona)
        db.session.commit()

        session['user_id'] = nueva_persona.id
         
        return render_template('Salud_Digna.html', data=nueva_persona)
        
    else: 
        
        return render_template('Error_NU.html', data=persona_existente )  

@main.route('/submit_form_LoginIU', methods=['POST'])
def submit_form_IU():
    
    contrasena = request.form.get('contrasena')
    usuario    = request.form.get('usuario')

    usuario_existente = Persona.query.filter_by(usuario=usuario).first()
    
    # Verificar si el usuario existe y la contraseña es válida
    if usuario_existente and usuario_existente.check_password(contrasena):
        # El usuario y la contraseña son válidos
        return render_template('Salud_Digna.html', data=usuario_existente)  
    else:
        usuario_vacio = ""
        # El usuario no existe o la contraseña es incorrecta
        return render_template('Error_IU.html',  data=usuario_vacio)  


@main.route("/submit_form_Encuesta", methods=['POST'])
def submit_form_Encuesta():

    #df = pd.DataFrame()

    # Obtén los datos del formulario
    age                = int(request.form.get('edad'))
    gender             = int(request.form.get('Sexo')) 
    chestpain          = int(request.form.get('dolor'))
    fastingbloodsugar  = int(request.form.get('azucar'))
    restingrelectro    = int(request.form.get('Electrocardiograma')) 
    maxheartrate       = int(request.form.get('ritmoCardiaco'))  
    exerciseangia      = int(request.form.get('angina')) 
    oldpeak            = int(request.form.get('depresionST')) 
    slope              = int(request.form.get('pendienteST')) 
    noofmajorvessels   = int(request.form.get('vFlou')) 

    data = {
        'age': [age],
        'gender': [gender],
        'chestpain': [chestpain],
        'restingBP': [0],  # Puedes establecer un valor predeterminado si no está en el formulario
        'serumcholestrol': [0], # Puedes establecer un valor predeterminado si no está en el formulario
        'fastingbloodsugar': [fastingbloodsugar],
        'restingrelectro': [restingrelectro],
        'maxheartrate': [maxheartrate],
        'exerciseangia': [exerciseangia],
        'oldpeak': [oldpeak],
        'slope': [slope],
        'noofmajorvessels': [noofmajorvessels]
    }
    
    df = pd.DataFrame(data)
     
    # Realizar la predicción utilizando el modelo cargado
    prediction = loaded_model.predict(df)
    
    print("Predicción del modelo:", prediction[0])
    print(type(prediction[0]))
    resultados=""

    if prediction[0] == 1:

        return render_template('MalasNoticias.html', data=resultados)  

    else:
        return render_template('BuenasNoticias.html', data=resultados)  
    
    


@main.route('/enviar_NewDataUser', methods=['POST'])
def enviar_mensaje():
    
    key="hola"
    
    
    return {'mensaje': f'Datos del usuario {key} actualizados exitosamente.'}

""""

    # Obtener datos del formulario enviado
    nombre    = request.form.get('nombre_R')  # Asegúrate de tener el nombre del campo correcto
    usuario   = request.form.get('usuario_R')
    email     = request.form.get('email_R')
    contasena = request.form.get('contrasena_R')
   
    # Realizar la búsqueda en la base de datos
    persona = Persona.query.filter_by(usuarior=usr).first() 

    if usuario:

        mensaje = f'¡Hola, {persona.nombre}!'
    else :
        mensaje = 'Conteaseña Incorrecta.'

    # Devolver el mensaje como JSON
    return {'mensaje': mensaje}
"""
