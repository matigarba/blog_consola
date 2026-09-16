def mostrar_menu():
    while True:
        print("\n--- MENU DEL BLOG ---")
        print("1. Ver todos los posts")
        print("2. Buscar por titulo")
        print("3. Filtrar por tag")
        print("4. Validar posts")
        print("5. Salir")

        opcion = input("Elegí una opción: ").strip()

        try:
            opcion_menu = int(opcion)
        except ValueError:
            print("Opción inválida. Ingresa un numero.")
            continue

        if opcion_menu in [1, 2, 3, 4, 5]:
            return opcion_menu
        else:
            print("Opcion invalida! Elegi un numero del 1 al 5")