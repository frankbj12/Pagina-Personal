import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Definición de colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Tamaño de la pantalla y celdas del laberinto
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 40
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE

# Inicialización de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tomb of the Mask Clone")

# Generación del laberinto
laberinto = [[random.choice([1, 0]) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Posición inicial del jugador
jugador_x, jugador_y = 0, 0

# Cargar imágenes
jugador_image = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
pygame.draw.circle(jugador_image, RED, (CELL_SIZE // 2, CELL_SIZE // 2), CELL_SIZE // 2)

# Función para reiniciar el juego
def reiniciar_juego():
    global laberinto, jugador_x, jugador_y
    laberinto = [[random.choice([1, 0]) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    jugador_x, jugador_y = 0, 0

# Función para generar un laberinto más complejo
def generar_laberinto():
    for _ in range(GRID_HEIGHT * GRID_WIDTH // 3):
        x, y = random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)
        laberinto[y][x] = 0

# Generar el laberinto inicial
generar_laberinto()

# Función principal del juego
def juego():
    global jugador_x, jugador_y  # Declarar como variables globales

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # Mover al jugador de celda en celda
        if keys[pygame.K_UP] and jugador_y > 0 and laberinto[jugador_y - 1][jugador_x] != 0:
            jugador_y -= 1
        elif keys[pygame.K_DOWN] and jugador_y < GRID_HEIGHT - 1 and laberinto[jugador_y + 1][jugador_x] != 0:
            jugador_y += 1
        elif keys[pygame.K_LEFT] and jugador_x > 0 and laberinto[jugador_y][jugador_x - 1] != 0:
            jugador_x -= 1
        elif keys[pygame.K_RIGHT] and jugador_x < GRID_WIDTH - 1 and laberinto[jugador_y][jugador_x + 1] != 0:
            jugador_x += 1

        screen.fill(BLACK)

        # Dibujar el laberinto
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if laberinto[y][x] == 1:
                    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(screen, WHITE, rect)

        # Dibujar al jugador
        screen.blit(jugador_image, (jugador_x * CELL_SIZE, jugador_y * CELL_SIZE))

        pygame.display.flip()
        clock.tick(30)

# Iniciar el juego
juego()
