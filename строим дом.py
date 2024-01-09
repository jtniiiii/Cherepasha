import turtle
from random import randint

''' 
Код не запускается, начал это делать после добавления цветов
Просчитать отступы между домами
'''

def draw_house(
    x=0,
    y=0,
    base_w=150,
    base_h=20,
    bace_color='grey',
    walls_w=150,
    walls_h=60,
    walls_color='blue',
    door_w=50,
    door_h=50,
    door_color='brown',
    roof_w=170,
    roof_h=60,
    roof_color='red'
):
    
    '''
    вызывает функцию рисования фундамента
    вызывает функцию рисования стен
    вызывает функцию рисования крыши

    x - левый нижний угол фундамента
    y - левый нижний угол фундамента

    base_w - ширина фундамента
    base_h - высота фундамента
    bace_color - цвет фундамента

    walls_w - ширина стен
    walls_h - высота стен
    walls_color - цвет стен

    roof_w - ширина крыши
    roof_h - высота крыши
    roof_color - цвет крыши
    '''
  
    walls_x = x + (base_w - walls_w) // 2

    draw_base(x, y, base_w, base_h, bace_color)
    draw_walls(walls_x, y, walls_w, walls_h, walls_color, base_h)
    draw_door(walls_x, y, door_w, door_h, door_color, base_h, walls_w)
    draw_roof(walls_x, y, roof_w, roof_h, roof_color, base_h, walls_h, walls_w)


def draw_base(x, y, width, height, color):
    ''' рисуем фундамент'''
    turtle.penup() 
    turtle.goto(x, y)
    turtle.pendown()
    draw_rectangel(width, height, color)

def draw_walls(x, y, width, height, color, base_h):
    '''рисуем стены'''
    turtle.penup()
    turtle.goto(x, y + base_h)
    turtle.pendown()
    draw_rectangel(width, height, color)

def draw_door(x, y, width, height, color, base_h, walls_w):
    '''рисуем дверь'''
    turtle.penup()
    door_x = x + (walls_w - width) // 2
    turtle.goto(door_x, y + base_h)
    turtle.pendown()
    draw_rectangel(width, height, color)

def draw_roof(x, y, width, height, color, base_h, walls_h, walls_w):
    '''рисуем крышу'''
    turtle.penup()
    roof_x = x - (width - walls_w) // 2
    roof_y = y + base_h + walls_h
    turtle.goto(roof_x, roof_y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    top_x = roof_x + width // 2
    top_y = roof_y + height
    turtle.goto(top_x, top_y)
    turtle.goto(roof_x + width, roof_y)
    turtle.goto(roof_x, roof_y)
    turtle.end_fill()


def draw_rectangel(width, height, color):
    '''рисуем прямоугольник'''
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.end_fill()


def draw_street(x, y, houses):
    counter = 0
    while counter <= houses:
        base_w = randint(20, 200)
        base_h = randint(5, 50)
        base_color = (randint(0, 255), randint(0, 255), randint(0, 255))

        walls_w = randint(15, base_w)
        walls_h = randint(10, 300)
        walls_color = (randint(0, 255), randint(0, 255), randint(0, 255))

        door_w = randint(10, walls_w)
        door_h = randint(15, walls_h)
        door_color = (randint(0, 255), randint(0, 255), randint(0, 255))

        roof_w = randint(walls_w, 300)
        roof_h = randint(10, 150)
        roof_color = (randint(0, 255), randint(0, 255), randint(0, 255))

        draw_house( '''где-то тут ошибка'''
            x,
            y,
            base_w=base_w,
            base_h=base_h,
            base_color=base_color,
            walls_w=walls_w,
            walls_h=walls_h,
            walls_color=walls_color,
            door_w=door_w,
            door_h=door_h,
            door_color=door_color,
            roof_w=roof_w,
            roof_h=roof_h,
            roof_color=roof_color
        )

        counter += 1
        x += 300   ''' считает отступы между домами '''


draw_street(x=-300, y=-300, houses=8)

turtle.done()