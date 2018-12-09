# shiny-broccoli
Proyecto De Teoria De Base De Datos II B
Crear un sistema que integre las operaciones/datos de una base de datos origen (SQL Server) a una
base de datos destino (MySQL).
El sistema debe hacer lo siguiente:
Copiar los datos de las tablas seleccionadas en la base de datos origen a la base de datos destino:
1. Creación de triggers para las operaciones de las tablas seleccionadas (insertar, actualizar y
eliminar) en la base de datos (valor 3 puntos oro).
2. Creación de bitácora (tabla) que almacene las operaciones de las tablas seleccionadas en la
base de datos que serán replicadas (valor 2 puntos oro).
3. Creación de job de replicación para que lea la bitácora y replique las operaciones de la base
de datos origen a la de destino y su respectiva interfaz: una ventana con el botón del job y
una etiqueta que indique cuando fue la última vez que se ejecutó (valor 5 puntos oro).
Requisitos:
1. Se debe almacenar la cadena de conexión de la base de datos origen y destino.
2. La interfaz deberá mostrar las tablas de la base de datos origen que deberán ser
seleccionadas para que puedan ser replicados sus datos, además de un botón que ejecute
el job.
3. Las bases de datos deben existir en ambos motores de bases de datos, por lo tanto, deben
tener la misma estructura, los mismos nombres de objetos y sus tipos de datos deben ser
coincidentes.
Explicación de interfaz:
En la imagen 1 se muestra cómo debe guardar todos los parámetros relacionados a la cadena de
conexión (instancia, base de datos, puerto, usuario, contraseña), además de probar si se puede
establecer la conexión en ambas bases de datos. Si no hay problemas de conexión, se deben guardar
las configuraciones en ambas bases de datos.
En la figura 2 se muestran los controles necesarios para poder hacer la replicación:
• Un control que muestre las tablas que existen en la base de datos origen y que puedan ser
seleccionadas para su replicación.
• Un control que muestre las tablas que serán replicadas en la base de datos destino.
• Un botón que agregue las tablas a replicar a la base de datos destino.
• Un botón que elimine las tablas que se están replicando de la base de datos destino para
detener su replicación.
• Un botón que guarde los cambios.
• Un botón de cancelación de cambios.
