import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Zombies vs Plantas")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Clases
class Planta(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.x -= self.speed

# Grupos de Sprites
plantas = pygame.sprite.Group()
zombies = pygame.sprite.Group()
todos_sprites = pygame.sprite.Group()

# Función principal del juego
def main():
    reloj = pygame.time.Clock()
    corriendo = True

    # Crear plantas y zombies iniciales
    for i in range(5):
        planta = Planta(100, i * 100 + 50)
        plantas.add(planta)
        todos_sprites.add(planta)

    for i in range(5):
        zombie = Zombie(ANCHO - 100, i * 100 + 50)
        zombies.add(zombie)
        todos_sprites.add(zombie)

    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False

        # Actualizar sprites
        todos_sprites.update()

        # Comprobar colisiones
        colisiones = pygame.sprite.groupcollide(zombies, plantas, True, False)

        # Dibujar todo
        pantalla.fill(BLANCO)
        todos_sprites.draw(pantalla)
        pygame.display.flip()

        # Controlar la velocidad del juego
        reloj.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
