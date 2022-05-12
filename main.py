# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from mdutils import MdUtils

def main():
    md = MdUtils("solución.md")
    print("Sistema de colas abierto")
    print("=========================")
    print("Frecuencia de llegada de trabajos al sistema:")
    frecuencia = int(input(">> "))
    print("Inserta nombre de dispositivos: (separados por coma)")
    dispositivos = input(">> ").split(",")
    print("Inserta razón de visitas: (separados por coma)")
    visitas = input(">> ").split(",")
    print("Inserta tiempos de servicio en s: (separados por coma)")
    tiempos = input(">> ").split(",")
    print("=========================")
    md.new_header("Solución",1)
    md.insert_code("\lamda = " + str(frecuencia),language="latex")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


