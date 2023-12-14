Nombre del Proyecto

AppFutbol (es una aplicación desarrollada para una academia deportiva para niños y adolescentes y tiene la única función de mostrar  quienes son sus docentes y que materias se dictan en ella. La app cuenta con una seccion en la que se puede publicar noticias de eventos u otras actividades relacionadas con la institución(las mismas pueden ser comentadas por los usuarios registrados).

_Tabla de Contenidos.

1-Instalación

2-Uso

3-Licencia




1- Instalación

Para instalar la App será necesario contar con un terminal Bash para clonar el siguente link https://github.com/mvann15/Entrega_Final_Vanni.git. En el terminal Bash ejecutar el comando 'cd' para moverse a la ruta donde se guardará la App. Una vez elegida la ruta ejecutar 'git clone ', esto descargará la App para ser instalada.
Ya descargada será necesario contar con un ID como Pycharm, ya en el ID seleccionar Open dentro del menú y moverse hasta la ruta donde fue descargada la App. Hacer click en Ok. Una vez abierto es recomendable agregar un nuevo entorno virtual. Si este es el caso se deberá instalar Django en dicho entorno ('pip install django'), así como también la biblioteca Pillow ('pip install Pillow' en el terminal) para esto, en el terminal del Id ejecutar el comando 'pip install django', y ejecutar las migraciones con los comandos 'python manage.py makemigrations y 'python manage.py migrate'  . A continuación cofigurar manage (seleccionar la opción módulo-runserver) y generar un usuario para acceder al panel admin de la App ejecutando el comando 'python manage.py createsuperuser'. Ya es posible ejecutar la App desde manage (cuando lo hagas, haz click en la url que aparecerá en el terminal, para que la App abra en tu navegador).

2- Uso

La app es funcional desde el comienzo  y podrás recorrer la página aún sin ser usuario registrado, en ella podrás ver las materias que se dictan en la academia, quienes las dictan y las noticias. (Solo los usuarios registrados pueden comentar las noticias). No imaginé un crud dentro de la app , no existe información sensible y pensé mas en la experiencia del usuario . Yo solo pensé en que pueda servir para promocionar. Todos los botones son funcionales, excepto el que  permite seleccionar la imagen del avatar, para poder modificarla se podrá acceder a través del link https:127.0.0.1:8000/accounts/avatar, sin embargo es necesario ser usuario registrado para poder crearlo.(el motivo del enlace es que no quería ver el botón crear avatar en la página de inicio)

3-Licencia

La App no se encuentra registrada y puedes hacer uso indiscriminado de ella hasta que me de cuenta. Enjoy.

