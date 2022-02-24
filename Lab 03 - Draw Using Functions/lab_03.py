import arcade
arcade.open_window(800, 600, "Avión")
def main():
    arcade.set_background_color(arcade.color.BLUEBONNET)
    arcade.start_render()
    avión()
    sol()
    nube(500,525)
    nube(250, 125)
    nube(200, 425)
    nube(700, 275)
    #Final
    arcade.finish_render()
    arcade.run()
def sol():
    arcade.draw_triangle_filled(600, 600, 650, 550, 500, 575, arcade.color.FLUORESCENT_ORANGE)
    arcade.draw_triangle_filled(610, 560, 700, 500, 525, 512, arcade.color.FLUORESCENT_ORANGE)
    arcade.draw_triangle_filled(620, 520, 750, 475, 550, 450, arcade.color.FLUORESCENT_ORANGE)
    arcade.draw_triangle_filled(630, 480, 760, 450, 600, 400, arcade.color.FLUORESCENT_ORANGE)
    arcade.draw_triangle_filled(690, 450, 770, 425, 650, 360, arcade.color.FLUORESCENT_ORANGE)
    arcade.draw_triangle_filled(720, 420, 790, 410, 720, 325, arcade.color.FLUORESCENT_ORANGE)
    arcade.draw_triangle_filled(770, 410, 820, 410, 770, 310, arcade.color.FLUORESCENT_ORANGE)
    arcade.draw_circle_filled(800, 600, 200, arcade.color.CHROME_YELLOW)
def avión():
    #Cola
    arcade.draw_triangle_filled(650,55,500,300,750,250,arcade.color.AUROMETALSAURUS)
    arcade.draw_ellipse_filled(645,300,150,235,arcade.color.BLUEBONNET,110)
    #Estructura del avión
    arcade.draw_ellipse_filled(400,300,700,200,arcade.color.AUROMETALSAURUS,45)
    #Alas
    arcade.draw_triangle_outline(435,402,520,319,700,500,arcade.color.BLACK,2)   #Contorno derecha
    arcade.draw_triangle_filled(380,380,450,250,700,500,arcade.color.AUROMETALSAURUS)   #Relleno derecha
    arcade.draw_triangle_outline(350,350,450,250,100,50,arcade.color.BLACK,2)   #Contorno izquierda
    arcade.draw_triangle_filled(355,355,455,255,100,50,arcade.color.AUROMETALSAURUS)    #Relleno izquierda
    #Ventanas
    arcade.draw_rectangle_filled(275,450,25,25,arcade.color.BLIZZARD_BLUE,45)
    arcade.draw_rectangle_filled(325,400,25,25,arcade.color.BLIZZARD_BLUE,45)
    arcade.draw_rectangle_filled(375,350,25,25,arcade.color.BLIZZARD_BLUE,45)
    arcade.draw_rectangle_filled(425,300,25,25,arcade.color.BLIZZARD_BLUE,45)
    arcade.draw_rectangle_filled(475,250,25,25,arcade.color.BLIZZARD_BLUE,45)
    arcade.draw_rectangle_filled(525,200,25,25,arcade.color.BLIZZARD_BLUE,45)
    arcade.draw_rectangle_filled(575,150,25,25,arcade.color.BLIZZARD_BLUE,45)
    #Cabina
    arcade.draw_triangle_filled(142,520,220,450,280,520,arcade.color.BLIZZARD_BLUE)
    arcade.draw_circle_filled(170,530,30,arcade.color.BLIZZARD_BLUE)
    arcade.draw_circle_filled(180,530,30,arcade.color.BLIZZARD_BLUE)
    arcade.draw_circle_filled(190,528,30,arcade.color.BLIZZARD_BLUE)
    arcade.draw_circle_filled(200,526,30,arcade.color.BLIZZARD_BLUE)
    arcade.draw_circle_filled(210,525,30,arcade.color.BLIZZARD_BLUE)
    arcade.draw_circle_filled(220,522,30,arcade.color.BLIZZARD_BLUE)
    arcade.draw_circle_filled(230,519,30,arcade.color.BLIZZARD_BLUE)
    arcade.draw_circle_filled(240,515,30,arcade.color.BLIZZARD_BLUE)
    arcade.draw_circle_filled(265,525,10,arcade.color.BLIZZARD_BLUE)
    arcade.draw_circle_filled(270,525,10,arcade.color.BLIZZARD_BLUE)
    #Piloto
    arcade.draw_circle_outline(200,500,20,arcade.color.BLACK,2)
    arcade.draw_circle_filled(200,500,19,arcade.color.INDIAN_RED)
    arcade.draw_circle_filled(200,510,2,arcade.color.BLACK)
    arcade.draw_rectangle_filled(190,500,20,2,arcade.color.BLACK,35)
def dibujar_nube(x,y):
    arcade.draw_ellipse_filled(x,y+25,150,100,arcade.color.FLORAL_WHITE)
    arcade.draw_ellipse_filled(x,y-25,150,100,arcade.color.FLORAL_WHITE)
    arcade.draw_ellipse_filled(x+75,y,150,100,arcade.color.FLORAL_WHITE)
    arcade.draw_ellipse_filled(x-75,y,150,100,arcade.color.FLORAL_WHITE)
main()