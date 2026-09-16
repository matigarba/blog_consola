from blog.menu import mostrar_menu
from blog.operaciones import listar_posts
from blog.operaciones import buscar_por_titulo
from blog.operaciones import filtrar_por_tag
from blog.validaciones import validar_post
from blog.datos import posts

def blog():
    while True:

        opcion = mostrar_menu()

        if opcion == 1:
            print("\nListado de posts:")
            listar_posts(posts)

        elif opcion == 2:
            busqueda = input("Escribe el titulo que estas buscando:").strip().lower()
            resultados = buscar_por_titulo(posts, busqueda)

            if not resultados:
                print("No se encontro el titulo buscado")
            else:
                for titulo in resultados:
                    print(titulo)
       

        elif opcion == 3:
            tag_buscado = input("Escribe el tag que estas buscando:").strip().lower()
            resultados = filtrar_por_tag(posts, tag_buscado)

            if not resultados:
                print("No se encontraron post con el tag buscado")
            else:
                for tag in resultados:
                    print(tag)

        elif opcion == 4:
            print("Validando posts...")

            for index, post in enumerate(posts, start=1):
                es_valido, mensaje = validar_post(post)

                if es_valido:
                    print(f"Post {index}: {mensaje[0]}")
                else:
                    print(f"Post {index}: errores - {' | '.join(mensaje)}")


        elif opcion == 5:
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break


if __name__ == "__main__":
    blog()