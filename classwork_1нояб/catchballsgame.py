import pygame
from pygame.draw import circle, polygon
from random import randint

pygame.init()

FPS = 120
screen = pygame.display.set_mode((1200, 900))  # Создание игрового окна
clock = pygame.time.Clock()  # Создание часов
font_style = pygame.font.SysFont(None, 50)  # Создание стилей текста для вывода
font_style_start = pygame.font.SysFont(None, 100)  # надписей
font_style_finish = pygame.font.SysFont(None, 150)

RED = (255, 0, 0)  # Установка цветов
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]  # Создание массива цветов


def new_ball():
    '''
    Создаёт новый шарик
    Рандомно выбирает параметры x (координата по x), y (координата по y),
    r (радиус шарика), color (цвет шарика). Возращает список параметров
    '''
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 4)]
    circle(screen, color, (x, y), r)
    parameters = [x, y, r, color]
    return parameters


def new_triangle():
    '''
    Создаёт новый треугольник
    Рандомно выбирает параметры x (координата по x), y (координата по y),
    a (длина стороны треугольник вдоль оси x и его высота), color (цвет треугольника).
    Возращает список параметров
    '''
    x = randint(100, 700)
    y = randint(100, 500)
    a = randint(30, 50)
    color = COLORS[randint(0, 4)]
    polygon(screen, color, [[x, y], [x + a // 2, y - a],
                            [x + a, y]])
    parameters = [x, y, a, color]
    return parameters


def ball(parameters):
    '''
    Рисует шарик
    parameters[0] - координата шарика по оси x
    parameters[1] - координата шарика по оси y
    parameters[2] - радиус шарика
    parameters[3] - цвет шарика
    '''
    x = parameters[0]
    y = parameters[1]
    r = parameters[2]
    color = parameters[3]
    circle(screen, color, (x, y), r)


def triangle(parameters):
    ''''
    Рисует треугольник
    parameters[0] - координата треугольника по оси x
    parameters[1] - координата треугольника по оси y
    parameters[2] - высота
    parameters[3] - цвет треугольника
    '''
    x = parameters[0]
    y = parameters[1]
    a = parameters[2]
    color = parameters[3]
    polygon(screen, color, [[x, y], [x + a // 2, y - a],
                            [x + a, y]])


def speed():
    '''Генерирует проекции скорости на оси x и y'''
    x_speed = randint(-500, 500) / 100
    y_speed = randint(-500, 500) / 100
    return [x_speed, y_speed]


def score_message(msg, color):
    '''Выводит на экран счёт игрока'''
    mesg = font_style.render("Score: " + str(msg), True, color)
    screen.blit(mesg, [1000, 70])


def timer_message(timer, color):
    '''Выводит на экран оставшееся время игрока'''
    mesg = font_style.render("Time: " + str(timer), True, color)
    screen.blit(mesg, [1000, 120])


def win_message(color):
    '''Выводит на экран сообщение о победе'''
    mesg = font_style_finish.render("YOU WIN!", True, color)
    screen.blit(mesg, [300, 400])


def lose_message(color):
    '''Выводит на экран сообщение о проигрыше'''
    mesg = font_style_finish.render("YOU LOSE!", True, color)
    screen.blit(mesg, [300, 400])


def play_game(score_for_win, timer):
    '''
    Игра "Поймай шарик"
    '''
    finished = False
    pygame.display.update()
    clock = pygame.time.Clock()  # Установить часы
    num_of_balls = 3  # Количество шариков
    num_of_triangles = 3  # Количество треугольников
    score = 0  # Начальный счёт
    parameters_balls = []  # Список шариков
    parameters_triangles = []  # Список треугольников
    speed_list_balls = []  # Список скоростей шариков
    speed_list_triangles = []  # Список скоростей треугльков
    for _ in range(num_of_balls):  # Заполнить списки шариков и
        parameters_balls.append(new_ball())  # треугольнков и их скоростей
        speed_list_balls.append(speed())
    for _ in range(num_of_triangles):
        parameters_triangles.append(new_triangle())
        speed_list_triangles.append(speed())
    while not finished:
        clock.tick(FPS)
        screen.fill(BLACK)
        for num_of_ball in range(num_of_balls):
            parameters_balls[num_of_ball][0] += speed_list_balls[num_of_ball][0]
            parameters_balls[num_of_ball][1] += speed_list_balls[num_of_ball][1]
            if parameters_balls[num_of_ball][0] + parameters_balls[num_of_ball][2] >= 1200 or \
                    parameters_balls[num_of_ball][0] - parameters_balls[num_of_ball][2] <= 0:
                speed_list_balls[num_of_ball][0] = -speed_list_balls[num_of_ball][0]
            if parameters_balls[num_of_ball][1] + parameters_balls[num_of_ball][2] >= 900 or \
                    parameters_balls[num_of_ball][1] - parameters_balls[num_of_ball][2] <= 0:
                speed_list_balls[num_of_ball][1] = -speed_list_balls[num_of_ball][1]
        for num_of_triangle in range(num_of_triangles):
            parameters_triangles[num_of_triangle][0] += speed_list_triangles[num_of_triangle][0]
            parameters_triangles[num_of_triangle][1] += speed_list_triangles[num_of_triangle][1]
            if parameters_triangles[num_of_triangle][0] + parameters_triangles[num_of_triangle][2] >= 1200 or \
                    parameters_triangles[num_of_triangle][0] <= 0:
                speed_list_triangles[num_of_triangle][0] = -speed_list_triangles[num_of_triangle][0]
            if parameters_triangles[num_of_triangle][1] >= 900 or \
                    parameters_triangles[num_of_triangle][1] - parameters_triangles[num_of_triangle][2] <= 0:
                speed_list_triangles[num_of_triangle][1] = -speed_list_triangles[num_of_triangle][1]
        for num_of_ball in range(len(parameters_balls)):  # Отрисовать фигуры с новыми координатами
            ball(parameters_balls[num_of_ball])
        for num_of_triangle in range(len(parameters_triangles)):
            triangle(parameters_triangles[num_of_triangle])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Проверить, попал ли игрок в шарик
                for num_of_ball, position in enumerate(parameters_balls):
                    if (event.pos[0] - position[0]) ** 2 + (event.pos[1] - position[1]) ** 2 <= position[2] ** 2:
                        score += 1  # Если да,добавить очки и создать новый шарик
                        parameters_balls[num_of_ball] = new_ball()
                        speed_list_balls[num_of_ball] = speed()
                for num_of_triangle, position in enumerate(parameters_triangles):
                    x0, y0 = event.pos[0], event.pos[1]
                    x1, y1 = position[0], position[1]
                    x2, y2 = position[0] + position[2] // 2, position[1] - position[2]
                    x3, y3 = position[0] + position[2], position[1]
                    a = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
                    b = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
                    c = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
                    if (a >= 0 and b >= 0 and c >= 0) or (a <= 0 and b <= 0 and c <= 0):
                        score += 4  # Проверка, попал ли игрок в треугольник, если да, то + очки, создание нового
                        parameters_triangles[num_of_triangle] = new_triangle()
                        speed_list_triangles[num_of_triangle] = speed()
        timer -= 1 / 120  # уменьшить таймер
        score_message(str(score), MAGENTA)  # вывести счет
        timer_message(str(int(timer)), MAGENTA)  # выести оставшееся время
        pygame.display.update()  # вывести изменения на экран
        if score >= score_for_win and timer >= 0:  # если набрал нужное кол-во очков до конца времени, сообщение о победе
            win_message(RED)
            finished = True
        elif timer < 0:  #Если нет, сообщение о поражении
            lose_message(RED)
            finished = True
        pygame.display.update()
    pygame.time.wait(850)
    pygame.quit()  # выйти из игры


play_game(10, 50)
