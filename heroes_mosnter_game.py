
import random

class personaje:
    def __init__(self, nombre, vida, fuerza):
        self.__nombre = nombre
        self.__vida = vida
        self.__fuerza = fuerza
    
    def get_nombre(self):
        return self.__nombre
    
    def get_vida(self):
        return self.__vida
    
    def get_fuerza(self):
        return self.__fuerza
    
    def recibir_danio(self, danio):
        self.__vida -= danio
        
        if self.__vida < 0:
            self.__vida = 0
            
    def esta_vivo(self):
        return self.__vida > 0

class Heroe(personaje):
    def __init__(self, nombre, vida, fuerza, magia):
        super().__init__(nombre, vida, fuerza)
        self.__magia = magia
    
    def get_magia(self):
        return f"{self.get_nombre()} usa magia de {self.__magia}"
    
    def atacar_monstruo(self, monstruo):
        danio = random.randint(1, self.get_fuerza())
        monstruo.recibir_danio(danio)
        print(f"{self.get_nombre()} ataca al monstruo con {danio} de danio")
        if not monstruo.esta_vivo():
            print(f"{monstruo.get_nombre()} ha sido derrotado")
    
class Monstruo(personaje):
    def __init__(self, nombre, vida, fuerza):
        super().__init__(nombre, vida, fuerza)
        
    def atacar_heroe(self, heroe):
        danio = random.randint(1, self.get_fuerza())
        heroe.recibir_danio(danio)
        print(f"{self.get_nombre()} ataca a {heroe.get_nombre()} con {danio} de danio")
        if not heroe.esta_vivo():
            print(f"{heroe.get_nombre()} ha sido derrotado")
    
def main():
    heroe1=Heroe("Gandalf", 100, 10, "fuego")
    monstruo1= Monstruo("Sauron", 100, 10)
        
    while heroe1.esta_vivo() and monstruo1.esta_vivo():
        heroe1.atacar_monstruo(monstruo1)
        if monstruo1.esta_vivo():
            monstruo1.atacar_heroe(heroe1)
    if heroe1.esta_vivo():
        print(f"{heroe1.get_nombre()} ha ganado")
    else:
        print(f"{monstruo1.get_nombre()} ha ganado")


if __name__ == "__main__":
    main()