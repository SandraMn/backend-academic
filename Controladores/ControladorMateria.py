from Repositorios.RepositorioMateria import RepositorioMateria
from Repositorios.RepositorioDepartamento import RepositorioDepartamento
from Modelos.Materia import Materia


class ControladorMateria():
    def __init__(self):
        self.repositorioMateria = RepositorioMateria()
        self.repositorioDepartamento = RepositorioDepartamento()

    def index(self):
        return self.repositorioMateria.findAll()

    def create(self, infoMateria):
        nuevoMateria = Materia(infoMateria)
        return self.repositorioMateria.save(nuevoMateria)

    def show(self, id):
        elMateria = Materia(self.repositorioMateria.findById(id))
        return elMateria.__dict__

    def update(self, id, infoMateria):
        materiaActual = Materia(self.repositorioMateria.findById(id))
        materiaActual.nombre = infoMateria["nombre"]
        materiaActual.creditos = infoMateria["creditos"]
        return self.repositorioMateria.save(materiaActual)

    def delete(self, id):
        return self.repositorioMateria.delete(id)
