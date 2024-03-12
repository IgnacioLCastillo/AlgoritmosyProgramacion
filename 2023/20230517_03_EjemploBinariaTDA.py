import pickle
import datetime


class Alumno:
    def __init__(self, legajo, nombre, fecha_nac):
        self.legajo = legajo
        self.nombre = nombre
        self.fecha_de_nacimiento = fecha_nac

    def to_string(self):
        date_format = self.fecha_de_nacimiento.strftime(
            '%d/%m/%Y %H:%M:%S')
        return "Alumno: %i\n\t%s\n\t%s" % (self.legajo, self.nombre, date_format)


def de_a_uno():
    # Escribiendo y leyendo de a uno
    alumno = Alumno(1, "Lucas Frias", datetime.datetime(1994, 1, 29, 7, 15, 00))
    file_descriptor_for_write = open("misLibrerias/Alumnosbinfile.bin", "wb")
    pickle.dump(alumno, file_descriptor_for_write)
    file_descriptor_for_write.close()

    file_descriptor_for_read = open("misLibrerias/Alumnosbinfile.bin", "rb")
    print(pickle.load(file_descriptor_for_read).to_string())
    file_descriptor_for_read.close()


def de_a_muchos():
    # Escribiendo y leyendo de a muchos
    alumnos = [Alumno(1, "Lucas Frias", datetime.datetime(1994, 1, 29, 7, 15, 00)),
               Alumno(2, "Ignacio Castillo", datetime.datetime(1990, 11, 25, 7, 36, 00)),
               Alumno(3, "Alumno ejemplo", datetime.datetime(1980, 8, 23, 5, 48, 00)),
               Alumno(4, "Alumno ejemplo XX", datetime.datetime(1980, 8, 23, 5, 48, 00))]
    file_descriptor_for_write = open("binfile.bin", "wb")
    pickle.dump(alumnos, file_descriptor_for_write)
    file_descriptor_for_write.close()

    file_descriptor_for_read = open("binfile.bin", "rb")
    alumnos_leidos = pickle.load(file_descriptor_for_read)
    for alumno in alumnos_leidos:
        print(alumno.to_string())
    file_descriptor_for_read.close()


# Main
#de_a_uno()
de_a_muchos()