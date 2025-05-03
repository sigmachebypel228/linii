import pygame

# Инициализация библиотеки PyGame
pygame.init()

# Размер окна
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Рисование прямых линий")

# Фоновый цвет (чёрный)
BACKGROUND = (0, 0, 0)
screen.fill(BACKGROUND)

# Цвет основной линии (белый)
LINE_COLOR = (255, 255, 255)

# Цвет линии предварительного просмотра (серый)
PREVIEW_COLOR = (192, 192, 192)

# Списки для хранения всех нарисованных линий
lines = []

# Хранение координат начала и конца текущей линии
start_point = None
end_point = None

# Частота кадров
FPS = 60
clock = pygame.time.Clock()

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Нажали левую кнопку мыши
                start_point = event.pos  # Начало новой линии
                end_point = event.pos  # Конец совпадает с началом
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Отпустили левую кнопку мыши
                if start_point is not None and end_point is not None:
                    lines.append((start_point, end_point))  # Фиксируем готовую линию
                start_point = None
                end_point = None
        elif event.type == pygame.MOUSEMOTION:
            if start_point is not None:  # Перетаскиваем конец линии вслед за движением мыши
                end_point = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            # Правая кнопка мыши создает новую линию и перезаписывает старую
            if start_point is not None and end_point is not None:
                lines.append((start_point, end_point))  # Фиксируем текущую линию
                start_point = end_point  # Новая линия начинается с предыдущего конца
                end_point = None  # Готовимся зафиксировать следующую точку

    # Очищаем экран
    screen.fill(BACKGROUND)

    # Отрисовываем готовые линии
    for s, e in lines:
        pygame.draw.line(screen, LINE_COLOR, s, e, 3)

    # Предпросмотр текущей линии
    if start_point is not None and end_point is not None:
        pygame.draw.line(screen, PREVIEW_COLOR, start_point, end_point, 3)

    # Обновляем экран
    pygame.display.flip()
    clock.tick(FPS)

# Выходим из PyGame
pygame.quit()