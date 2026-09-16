from blog.datos import estados_post

def validar_post(post):

    if not isinstance(post, dict):
        return False, ["El post debe ser un diccionario"]

    errores = []

    claves_obligatorias = ["id", "titulo", "autor", "contenido", "estado"]
    for clave in claves_obligatorias:
        if clave not in post:
            errores.append(f'Falta la clave "{clave}"')

    titulo = post.get("titulo")
    if titulo == "" or titulo == None:
        errores.append("El título no puede estar vacío")

    contenido = post.get("contenido")
    if contenido == "" or contenido == None:
        errores.append("El contenido no puede estar vacío")

    tags = post.get("tags")
    if tags is not None and not isinstance(tags, list):
        errores.append("Los tags deben ser una lista")

    autor = post.get("autor")
    if autor is not None:
        if not isinstance(autor, dict):
            errores.append("El autor debe ser un diccionario")
        elif "nombre" not in autor:
            errores.append('El autor debe tener la clave "nombre"')

    estado = post.get("estado")
    if estado is not None and estado not in estados_post:
        errores.append(f"El estado debe ser uno de: {estados_post}")

    if errores:
        return False, errores

    return True, ["Válido"]
