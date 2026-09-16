def listar_posts(lista):
    for index, post in enumerate(lista, start= 1):
        titulo = post.get("titulo", "Sin título")
        nombre_autor = post.get("autor", {}).get("nombre", "Autor desconocido")
    
        print(f"{index}: {titulo} - Autor: {nombre_autor}")

def buscar_por_titulo(lista, termino):
    termino = termino.lower()
    posts_encontrados = []
    
    print(f"Posts encontrados con {termino}:")
    for post in lista:
        if termino in post["titulo"].lower():
            posts_encontrados.append(post["titulo"])

    return posts_encontrados

def filtrar_por_tag(lista, tag):
    tag_encontrado = []

    print(f"Posts encontrados con el tag {tag}:")
    for post in lista:
        tags_lower = [tag.lower() for tag in post["tags"]]

        if tag in tags_lower:
            tag_encontrado.append(post["titulo"])

    return tag_encontrado