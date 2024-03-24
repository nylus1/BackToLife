def leer_disco(ruta):
    try:
        with open(ruta, 'rb') as f:
            while True:
                bloque = f.read(1024)
                if not bloque:
                    break
                for b in bloque:
                    print(f'{b:02x}', end=' ')
                print()
    except PermissionError:
        print("No tienes permisos suficientes para acceder a este disco.")

leer_disco('E:') 
