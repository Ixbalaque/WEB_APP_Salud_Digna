# WEB_APP_Salud_Digna
App  que predice un enfermedad cardiovascular en base a maching learing 

1) Entorno virtual 
    
    Asumiendo que ya tienes Python instalado en tu sistema
  
    1.1) Instala virtualenv (si no lo tienes instalado): 
        sudo apt-get update 
        sudo apt-get install python3-venv
  
    1.2) Crea un nuevo directorio para tu proyecto y navega a él:
        mkdir mi_proyecto
        cd mi_proyecto
  
    1.3) Crea un entorno virtual
        python3 -m venv venv
   
    1.4) Activa el modo Virtual 
        source venv/bin/activate
   
    Nota: para desactivar el entorno virtual usa el comando: deactivate

2) Clona el repositorio de Github     
    
    2.1) Descargar GitHub en caso de no tenerlo descargado
         sudo apt-get update
         sudo apt-get install git
   2.2)Clonar el repositorio en su carpeta previamente creada
         git clone

3) Ejecucicion de la APP

   3.3) Instale el archivo requirements.txt
        pip install -r requirements.txt
   3.3) Ejecute la app
        python3 run.py
