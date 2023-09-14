import os

def create_html(ruta_carpeta):
    with open(os.path.join(ruta_carpeta, "index.html"), "w") as f:
        f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Página</title>\n</head>\n<body>\n<h1>Mi Página</h1>\n</body>\n</html>")

def create_css(ruta_carpeta):
    with open(os.path.join(ruta_carpeta, "styles.css"), "w") as f:
        f.write("/* Estilos CSS aquí */")

def create_JS(ruta_carpeta):
    with open(os.path.join(ruta_carpeta, "main.js"), "w") as f:
        f.write("// Código JavaScript aquí")

def create_dir(ruta_base):
    for i in range(1,26):
        nombre_carpeta = input(f"Pon el nombre de la carpeta {i}: ")
        ruta_carpeta = os.path.join(ruta_base, nombre_carpeta)

        if not os.path.exists(ruta_carpeta):
            os.mkdir(ruta_carpeta)
        else:
            print(f"La carpeta {nombre_carpeta} ya existe.")

        create_html(ruta_carpeta)
        create_css(ruta_carpeta)
        create_JS(ruta_carpeta)

    print("Carpetas creadas exitosamente. Puedes iniciar tus proyectos.")

if __name__ == "__main__":
    ruta_base = "/Users/hp/Documents/primer_parcial-pages"
    create_dir(ruta_base)
