from msilib.schema import Patch
import random 
from clases.Aleatorio import Aleatorio
from PIL import Image
import pathlib




def contarArchivos(carpetaBase, carpetaTipo):
    contador = 0
    for archivo in pathlib.Path("./{carpetaBase}/{carpetaTipo}".format(carpetaBase = carpetaBase, carpetaTipo = carpetaTipo)).iterdir():
        if archivo.is_file():
            contador += 1

    return contador


def construirRuta(carpeta, parteImagen, tipoArchivo):
    ruta = pathlib.Path("./{carpeta}/{parteImagen}/{parteImagen}".format(carpeta = carpeta, parteImagen = parteImagen)+
                        str(random.randint(1, contarArchivos(carpeta, parteImagen)))+"."+tipoArchivo)
    return  ruta


def calcularAncho(imagen1, imagen2):
    ancho = (imagen1.width - imagen2.width) // 2
    return ancho


def calcularAlto(imagen1, imagen2):
    alto =(imagen1.height - imagen2.height) // 2
    return alto

def crearCombinacion(numeroCombinaciones):
    
    for i in range(numeroCombinaciones):
        nombreProyecto = "OldSkull"
        rutaFondo = construirRuta(nombreProyecto, "fondo", "jpg")
        rutaBase = construirRuta(nombreProyecto, "base", "png")
        rutaCuerpo = construirRuta(nombreProyecto, "cuerpo", "png")
        rutaManos = construirRuta(nombreProyecto, "manos", "png")
        rutaCabeza = construirRuta(nombreProyecto, "cabeza", "png")
        rutaOjos = construirRuta(nombreProyecto, "ojos", "png")

        imagenFondo = Image.open(rutaFondo)
        imagenBase = Image.open(rutaBase)
        imagenCuerpo = Image.open(rutaCuerpo)
        imagenManos = Image.open(rutaManos)
        imagenCabeza = Image.open(rutaCabeza)
        imagenOjos = Image.open(rutaOjos)

        imagenFondo.paste(imagenBase, (calcularAncho(
            imagenBase, imagenFondo), calcularAlto(imagenBase, imagenFondo)), imagenBase)
        imagenFondo.paste(imagenCuerpo, (calcularAncho(
            imagenFondo, imagenCuerpo), calcularAlto(imagenFondo, imagenCuerpo)), imagenCuerpo)
        imagenFondo.paste(imagenManos, (calcularAncho(
            imagenFondo, imagenManos), calcularAlto(imagenFondo, imagenManos)), imagenManos)
        imagenFondo.paste(imagenCabeza, (calcularAncho(
            imagenFondo, imagenCabeza), calcularAlto(imagenFondo, imagenCabeza)), imagenCabeza)
        imagenFondo.paste(imagenOjos, (calcularAncho(
            imagenFondo, imagenOjos), calcularAlto(imagenFondo, imagenOjos)), imagenOjos)
        imagenFondo.convert('RGB').save(
            "OldSkull{contador}.png".format(contador=i+1), "PNG", optimize=True)
        

if __name__ == "__main__":
    numeroCombinaciones = int(input("numero de combinaciones: "))
    crearCombinacion(numeroCombinaciones)
    
