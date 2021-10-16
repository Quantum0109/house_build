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
        roof_y - - считаем автоматически
        roof_width - спрашиваем у заказчика
        roof_height - спрашиваем у заказчика
        roof_fill - спрашиваем у заказчика
    """
    t.speed(1)

    def draw_rectangle(x, y, width = 0, height = 0, fill = "#000000"):
        t.penup()
        t.goto(x, y)
        t.setheading(0)
        t.pendown()
        t.fillcolor(fill)
        t.begin_fill()
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.end_fill()


    def build_base(base_x, base_y, base_width, base_height, base_fill):
        draw_rectangle(base_x, base_y,base_width,base_height, base_fill)
    
    def build_walls(walls_width, walls_height, walls_fill):
        walls_x = 10
        walls_y = 10
        draw_rectangle(walls_x, walls_y, walls_width, walls_height, walls_fill)
    

    def build_roof():
        print("Приехала бригада крыш")



    build_base(base_x, base_y, base_width, base_height, base_fill)
    build_walls(walls_width, walls_height, walls_fill)
    build_roof()

build_house(base_x = 0, base_y = 0, base_width = 200, base_height = 10, base_fill = "#000066")
t.done()
