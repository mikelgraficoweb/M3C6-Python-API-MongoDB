#Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y una contraseña. Crea un objeto usando la clase.

class Usuario:
  def __init__(self, nombre, contrasena):
    self.nombre = nombre
    self.contrasena = contrasena

PERSONA1 = Usuario("JUAN", "123LR412")


print(PERSONA1.nombre)
print(PERSONA1.contrasena)


