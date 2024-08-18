import simple_draw as sd

sd.resolution = (1300, 1300)

point_start = sd.Point(50, 50)

sd.background_color = (0, 255, 0)

square_size = 50
for y_num in range(0, 8):
    for x_num in range(0, 8):
        # if ((x_num + y_num) % 2) == 0:
        #     color = sd.COLOR_BLACK
        # else:
        #     color = sd.COLOR_WHITE

        color = (x_num * 20, x_num * 20, x_num * 20)

        sd.square(
            left_bottom=sd.Point(point_start.x + x_num * square_size, point_start.y + y_num * square_size),
            side=square_size,
            color=color,
            width=0)
        sd.sleep(0.2)


sd.pause()
