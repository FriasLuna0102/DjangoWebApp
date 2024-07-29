# Prueba de Homework: Desarrollo de una WebApp de Solicitud de Seguro de Vehículo

## Descripción del Proyecto

Desarrollar una aplicación web en Django que permita a los usuarios solicitar seguro de vehículo. La aplicación debe permitir a los usuarios ingresar la matrícula del vehículo, número de chasis o número de VIN, y sus datos personales. Además, deben poder cargar archivos de soporte como copia de la matrícula y copia de la licencia de conducir del solicitante. Las solicitudes deben ser gestionadas por un personal de backoffice que también tendrá acceso a la aplicación como usuario agente.

## Requisitos Funcionales

### 1. Funcionalidad de Usuario

**Registro y Autenticación:**
- Los usuarios deben poder registrarse y autenticarse en la aplicación.
- Los datos requeridos para el registro incluyen nombre, correo electrónico y contraseña.

**Solicitud de Seguro:**
- Los usuarios deben poder ingresar la matrícula del vehículo, número de chasis (VIN), marca, modelo, año y sus datos personales (nombre, dirección, teléfono).
- Los usuarios deben poder cargar archivos de soporte (copia de la matrícula y copia de la licencia de conducir).
- Los usuarios deben poder ver el estado de sus solicitudes de seguro.

### 2. Funcionalidad de Agente

**Gestión de Solicitudes:**
- Los agentes deben poder ver todas las solicitudes de seguro.
- Los agentes deben poder cambiar el estado de las solicitudes (por ejemplo, en proceso, aprobado, rechazado).
- Los agentes deben poder agregar comentarios a las solicitudes.
- Los agentes deben poder agregar el número de póliza, la fecha de emisión y de expiración, y cargar la imagen del carnet de seguro.
- Los agentes tendrán acceso al admin de Django, limitado a la gestión de solicitudes de seguro y la creación de usuarios.

## Requisitos Técnicos

**Modelos:**
- **User:** Utilizar el modelo de usuario de Django para los usuarios y agentes.
- **VehicleInsuranceRequest:** Modelo para almacenar las solicitudes de seguro con campos para matrícula, número de chasis, marca, modelo, año, datos personales del solicitante, archivos de soporte (matrícula y licencia), estado de la solicitud, comentarios del agente, número de póliza, fecha de emisión, fecha de expiración, y carnet de seguro.

**Vistas y Templates:**
- Crear vistas para registro, inicio de sesión y gestión de solicitudes.
- Crear templates HTML para las páginas mencionadas, asegurando un diseño limpio y funcional.

**Autorización:**
- Implementar permisos para asegurar que solo los agentes puedan acceder a la gestión de solicitudes.
- Configurar el admin de Django para permitir a los agentes gestionar las solicitudes de seguro y crear usuarios, limitando su acceso a estas funcionalidades.

## Puntos Adicionales

**Validaciones:**
- Validar que los campos de matrícula y número de chasis sean únicos.
- Validar los datos personales del usuario.
- Validar el formato y tamaño de los archivos cargados.

**Diseño Responsivo:**
- Asegurar que la aplicación sea accesible y funcional en dispositivos móviles.

**Documentación:**
- Incluir un archivo README con instrucciones para configurar y ejecutar la aplicación.
- Proveer documentación de las principales funcionalidades y estructura del código.

**Fecha de entrega: lunes 29 de Julio a las 10:00 a.m.**