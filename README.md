# Skywalker 

### UV SaaS Project


## How to setup development enviroment




2. Creando entorno virtual

	2.1 Se crea un entorno llamado env-www con python 3.4 [virtualenv -p /usr/bin/python3.4 env-www] 

	2.2 Se activa el entorno [source env-www/bin/activate] 

	2.3 Se verifica la version de python dentro del entorno [python -V] debe ser python3.4
	

3. Clonar el mugroso repositorio

	3.1  Estando dentro de la carpeta env-www ejecutar [git clone https://github.com/andresfaq/repo-www.git]


4. Instalando dependencias en el entorno virtual

	4.1 Activar el entorno virtual (Punto 2.2)
	
	4.2 Ejecutar el comando [pip install -r requerimientos.txt] 
	
	#NOTA: el archivo requerimientos.txt se encuentra dentro de la carpeta repo-www


5. Base de datos

	5.1 (Opcional) Instalar administrador grafico [sudo apt-get install pgadmin3]

	5.2 Crear una base de datos llamada 'concesionario'
	



6. Instalando Proyecto

	6.1 Activar y entrar a la carpeta del entorno
	
	6.2 Copiar el archivo settings.py desde repo-www hasta la carpeta repo-www/concesionario/concesionario y cambiarle en la seccion DATABASES los datos necesarios para que funcione con su base de datos (la contraseña y el usuario... o el puerto si es que lo han cambiado)

	6.3 Regresar al directorio  [/repo-www/concesionario] 
	
	6.4 Realizar proceso de migracion de los modelos a la BD
		[python manage.py migrate auth]
		[python manage.py makemigrations] 
		[python manage.py migrate]
		[python manage.py syncdb] # Tastypie
		
	6.5 Poblar la BD
		[python manage.py shell < administracion/seeders.py]

	6.6 Correr servidor [python manage.py runserver]
	
	6.7 Abrir navegador e ingresar a la direccion 127.0.0.1:8000 o localhost:8000 

#### NOTAS ####

[Problema cuando se ejecuta el comando 'git pull']
--> Si aparece algun error con archivos *.pyc cuando se realiza un pull del proyecto
    hay que ingresar por medio de la consola a la carpeta repo-www y ejecutar el siguiente comando
    [find . -name "*.pyc" -exec git rm -f {} \;] Luego hay que realizar un commit con los cambios 
    y por ultimo realizar de nuevo el pull del proyecto.   

[Solucionando problema de usuario postgres]
--> Si a la hora de configurar el servidor postgres aparece el siguiente error 
    "Error connecting to the server: FATAL:  password authentication failed for user "postgres"
    se puede solucionar con los siguientes comandos. 
    [sudo su postgres] luego [psql] y una vez dentro de la consola de postgres se escribe el siguiente comando 
    [alter user postgres with password 'MiNuevoPassword';]
