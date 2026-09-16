perfil_autor = {
    "nombre": "Martín Suárez",
    "bio": "Ingeniero de software y divulgador de temas de programación.",
    "especialidad": "JavaScript y React",
    "redes_sociales": ["@martin_dev", "@martin_js"]
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {"JavaScript", "React", "Frontend", "APIs", "JavaScript"}

posts = [
    {
        "id": 1,
        "titulo": "Introducción a JavaScript",
        "autor": perfil_autor,
        "tags": ["JavaScript", "Principiantes"],
        "estado": "publicado",
        "contenido": None
    },
    {
        "id": 2,
        "titulo": "Programando con react",
        "autor": perfil_autor,
        "tags": ["JavaScript", "React", "Frontend"],
        "estado": "borrador",
        "contenido": "React es una biblioteca de JavaScript que se utiliza para crear interfaces de usuario interactivas y dinámicas en aplicaciones web y móviles"
    },
    {
        "id": 3,
        "titulo": "Consumiendo APIs con fetch",
        "autor": perfil_autor,
        "tags": ["JavaScript", "APIs"],
        "estado": "archivado",
        "contenido": "La API Fetch proporciona una interfaz JavaScript para acceder y manipular partes del canal HTTP"
    },
    {
        "id": 4,
        "titulo": "",
        "autor": perfil_autor,
        "tags": ["JavaScript", "APIs"],
        "estado": "archivado",
        "contenido": "La API Fetch proporciona una interfaz JavaScript para acceder y manipular partes del canal HTTP"
    },
    {
        "id": 5,
        "titulo": "Error post",
        "autor": perfil_autor,
        "tags": "JavaScript y APIs",
        "estado": "Nuevo",
        "contenido": "Probar post con mas de un error"
    }
]