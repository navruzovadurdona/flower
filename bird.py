import pygame
import random

# Инициализация
pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐦 Flappy Bird")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 191, 255)
GREEN = (0, 200, 0)

# Птица
bird_x = 100
bird_y = HEIGHT // 2
bird_radius = 20
gravity = 0.5
jump = -8
velocity = 0

# Трубы
pipe_width = 60
pipe_gap = 150
pipe_x = WIDTH
pipe_height = random.randint(100, 400)
speed = 3

# Шрифт
font = pygame.font.SysFont(None, 36)
score = 0

# Игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLUE)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            velocity = jump

    # Движение птицы
    velocity += gravity
    bird_y += velocity

    # Движение трубы
    pipe_x -= speed
    if pipe_x + pipe_width < 0:
        pipe_x = WIDTH
        pipe_height = random.randint(100, 400)
        score += 1

    # Проверка столкновений
    if (
        bird_y - bird_radius < 0 or
        bird_y + bird_radius > HEIGHT or
        (pipe_x < bird_x + bird_radius < pipe_x + pipe_width and
         (bird_y - bird_radius < pipe_height or bird_y + bird_radius > pipe_height + pipe_gap))
    ):
        running = False  # Столкновение — конец игры

    # Отрисовка трубы
    pygame.draw.rect(screen, GREEN, (pipe_x, 0, pipe_width, pipe_height))
    pygame.draw.rect(screen, GREEN, (pipe_x, pipe_height + pipe_gap, pipe_width, HEIGHT))

    # Отрисовка птицы
    pygame.draw.circle(screen, WHITE, (bird_x, int(bird_y)), bird_radius)

    # Отображение счёта
    score_text = font.render(f"Очки: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

# Завершение
pygame.quit()
