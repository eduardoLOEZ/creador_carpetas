import os

#------CREAR HTML------
def create_html(ruta_carpeta):
    with open(os.path.join(ruta_carpeta, "index.html"), "w") as f:
        f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Página</title>\n</head>\n<body>\n<h1>Mi Página</h1>\n</body>\n</html>")


#------CREAR CSS------
def create_css(ruta_carpeta):
    with open(os.path.join(ruta_carpeta, "styles.css"), "w") as f:
        f.write("/* Estilos CSS aquí */")


#------CREAR JS------
def create_JS(ruta_carpeta):
   with open(os.path.join(ruta_carpeta, "main.js"), "w") as f:
        f.write("// Código JavaScript aquí")



#------FUNCION PRINCIPAL------
def create_dir(ruta):

    #numero de carpetas a crear
    for i in range(1,26):
        #nombre de la carpeta
        nombre_carpeta = f"pagina{i}"

        #donde se guardara
        ruta_carpeta = os.path.join(ruta, nombre_carpeta)

        if not os.path.exists(ruta_carpeta):
            os.mkdir(ruta_carpeta)
        else:
            print(f"La carpeta {nombre_carpeta} ya existe.")

        #cada carpeta tendra html,css y JS por si acaso(si no lo quieren, 
        #borren la funcion create_JS())
        create_html(ruta_carpeta)
        create_css(ruta_carpeta)
        create_JS(ruta_carpeta)

    print("carpetas creadas exitosamente con sus archivos, ya puedes iniciar tus proyectos")


if __name__== "__main__":
    #cambien la ruta dependiendo donde quieren guardar sus 25 carpetas
    ruta_base= "/Users/hp/Documents/primer_parcial-pages"
    create_dir(ruta_base)