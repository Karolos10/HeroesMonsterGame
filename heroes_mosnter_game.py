
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

class heroe(personaje):
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