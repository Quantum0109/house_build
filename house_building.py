import turtle as t

def build_house(base_x = -500, base_y = -500, base_width = 100, base_height = 10, base_fill = "#990000", walls_width = 0, walls_height = 0, walls_fill = "#000000", roof_width = 0, roof_height = 0, roof_fill = "#000000"):
    """
        base_x - x левого нижнего угла фундамента
        base_y - y левого нижнего угла фундамента

        base_width - ширина фундамента 
        base_height - высота фундамента 
        base_fill - цвет заливки фундамента

        walls_x - считаем автоматически
        walls_y - считаем автоматически
        walls_width - спрашиваем у заказчика
        walls_height - спрашиваем у заказчика
        walls_fill - спрашиваем у заказчика

        roof_x - считаем автоматически
        roof_y - считаем автоматически
        roof_width - считаем автоматически, 120% ширины крыши
        roof_height - спрашиваем у заказчика
        roof_fill - спрашиваем у заказчика
    """
    t.speed(0)

    #считаем автоматически величины
    walls_x = base_x
    walls_y = base_y + base_height
    walls_width = base_width
    roof_x = walls_x - (walls_width * 0.1)
    roof_y = base_height + walls_height
    roof_width = walls_width * 1.2

    def build_base(base_x, base_y, base_width, base_height, base_fill):
        t.penup()
        t.goto(base_x, base_y)
        t.setheading(0)
        t.fillcolor(base_fill)
        t.pendown()
        t.begin_fill()
        t.forward(base_width)
        t.left(90)
        t.forward(base_height)
        t.left(90)
        t.forward(base_width)
        t.left(90)
        t.forward(base_height)
        t.end_fill()

    def build_walls(walls_x, walls_y, walls_width, walls_height, walls_fill):
        t.penup()
        t.goto(walls_x, walls_y)
        t.setheading(0)
        t.pendown()
        t.fillcolor(walls_fill)
        t.begin_fill()
        t.forward(walls_width)
        t.left(90)
        t.forward(walls_height)
        t.left(90)
        t.forward(walls_width)
        t.left(90)
        t.forward(walls_height)
        t.left(90)
        t.end_fill()


    def build_roof(roof_x, roof_y, roof_width, roof_height, roof_fill):
        t.penup()
        t.goto(roof_x, roof_y)
        t.setheading(0)
        t.pendown()
        t.fillcolor(roof_fill)
        t.begin_fill()
        t.forward(roof_width)
        t.goto(walls_width / 2, base_height + walls_height + roof_height)
        t.goto(roof_x, roof_y)
        t.end_fill()


    build_base(base_x, base_y, base_width, base_height, base_fill)
    build_walls(walls_x, walls_y, walls_width, walls_height, walls_fill)
    build_roof(roof_x, roof_y, roof_width, roof_height, roof_fill)

build_house(base_x = 0, base_y = 0, base_width = 200, base_height = 10, base_fill = "#660000", walls_height = 150, walls_fill = "#00FF00", roof_height = 100, roof_fill = "#FFFF00")
t.done()
