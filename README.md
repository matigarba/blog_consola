Blog manejado por consola

Qué hace:

Blog manejado completamente desde consola. Permite listar, buscar, filtrar y validar posts almacenados en el archivo datos.py

Cómo ejecutarlo

Desde la carpeta del proyecto blog_consola, correr el comando 

python main.py

Estructura de archivos:

"main.py": En este archivo se corre el programa. Tiene el un while que muestra el menu y llama a las funciones.

"menu.py": En este archivo esta guardada la funcion de mostrar_menu() con sus opciones y un try-except para el manejo de inputs invalidos.

"datos.py": En este archivo se guarda la data del proyecto. perfil_autor(dic), estados_post(tup), etiquetas_blog(set), post(list).

"operacoines.py": Guarda las funciones de consultas. listar_posts(), buscar_por_titulo(), filtrar_por_tag().

"validaciones.py": Guarda la unica funcion, validar_post(), para validar la estructura de los posts.


Funcionalidades del menú

1. Ver todos los posts — Lista todos los posts con su título y autor.
2. Buscar por título — Busca posts cuyo título contenga el término ingresado.
3. Filtrar por tag — Busca posts que tengan el tag ingresado entre sus etiquetas.
4. Validar posts — Recorre todos los posts e informa si son válidos o qué errores tiene cada uno.
5. Salir — Finaliza el programa.
