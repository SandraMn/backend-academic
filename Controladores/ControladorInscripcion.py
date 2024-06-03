from Repositorios.RepositorioInscripcion import RepositorioInscripcion
from Modelos.Inscripcion import Inscripcion


class ControladorInscripcion():
    def __init__(self):

        self.repositorioInscripcion = RepositorioInscripcion()

    def index(self):
        return self.repositorioInscripcion.findAll()

    def create(self, infoInscripcion):

        nuevainscripcion = Inscripcion(infoInscripcion)


        return self.repositorioInscripcion.save(nuevainscripcion)

    def show(self, id):

        laInscripcion = Inscripcion(self.repositorioInscripcion.findById(id))

        return laInscripcion._dict_

    def update(self, id, infoInscripcion):

        inscripcionActual = Inscripcion(self.repositorioInscripcion.findById(id))


        inscripcionActual.año = infoInscripcion["año"]
        inscripcionActual.semestre = infoInscripcion["semestre"]
        inscripcionActual.nota_final = infoInscripcion["nota_final"]


        return self.repositorioInscripcion.save(inscripcionActual)

    def delete(self, id):
        return self.repositorioInscripcion.delete(id)