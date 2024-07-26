## Intrucciones para configurar y ejecutar

### La aplicacion esta contenida en un entorno virtual de Python con venv, por lo que para la ejecucion de la misma es necesario realizar lo siguiente:
#### 1. Ubicarse en el directorio "webApp". 
#### 2. Una ves dentro ejecutamos el comando "source bin/activate", para activar el entorno virtual.
#### 3. Si no tienes instalado Django, puedes instalarlo dentro del entorno virtual con el gestion de librerias de python pip, como "pip install django".
#### 4. Luego navegas dentro del directorio de "vehiculo_seguro", debe verse asi:
	
![image](https://github.com/user-attachments/assets/22cae9c5-b725-4097-9e39-55f51b1a00ca)

#### 5. Ya para la ejecucion usamos el comando "python manage.py runserver <puerto>". Si funciona correctamente debes ver:
![image](https://github.com/user-attachments/assets/9f042d4b-341d-4cd0-ae1f-a61bee979bef)

#### 6. Cuando vamos al localhost con el puerto indicado "http://localhost:8001/", deberiamos ser redireccionados al login:
![image](https://github.com/user-attachments/assets/b584cf4c-983a-40d0-b305-befc04963502)

#### 7. Una vez iniciada seccion, pues podemos enviar las solicitudes y listarlas como usuarios:
![image](https://github.com/user-attachments/assets/7267fb55-57d8-4ed7-a847-c5d6772c1825)

#### 8. Luego de realizar una solicitud, en el listado de usuario (solo se pueden ver las solicitudes que a realizado dicho usuario en especifico, la de otros usuarios se le omiten) se deberia de ver de esta forma (En la columna donde dice "Respuesta", una vez recibida la informacion del Agente nos permitira observar los comentarios y demas.):

![image](https://github.com/user-attachments/assets/15d09e70-f61f-40e9-bda4-38e49c963a0c)

#### 9. Vista del Agente (pueden ver todas las solicitudes de diferentes usuarios y dicha ruta esta regulada para solo agentes):
![image](https://github.com/user-attachments/assets/adf7a834-2762-4239-9f4f-bbbbf19fdeef)

#### 10. Esta es la vista de la edicion del Agente:
![image](https://github.com/user-attachments/assets/737c8e55-9eb6-4424-9d70-6c5ed3007c2b)

#### 11. Esta es la vista de la respuesta por parte del usuario:
![image](https://github.com/user-attachments/assets/5f3d05f9-a2f6-4318-bb74-21ede87402bc)


## Estructura del codigo:

#### 1. Directorios :
![image](https://github.com/user-attachments/assets/b5d97425-34aa-4b07-bca4-fe2af0353246)

#### 2. El modelo de la base de datos donde se almacenan las solicitudes se llama "Solicitud" no "VehicleInsuranceRequest", este se gestiona en el archivo models.py.
#### 3. En el views.py es donde se gestiona las vistas como el user_login, editar_solicitud, is_agent, etc.
#### 4. En el urls.py es donde gestiono los path a las rutas y endpoints.
#### 5. En el forms.py es donde gestiono la estructura de los formularios y demas para mostrarlo en la vista.
#### 6. Utilizo un archivo decorators.py para el manejo de los agentes, verificando si pertenecen a este grupo.


