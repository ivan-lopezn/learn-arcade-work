import arcade
arcade.open_window(800,600,"Avión")
arcade.set_background_color(arcade.color.BLUEBONNET)
arcade.start_render()
#Cola
arcade.draw_triangle_filled(650,55,500,300,750,250,arcade.color.AUROMETALSAURUS)
arcade.draw_ellipse_filled(645,300,150,235,arcade.color.BLUEBONNET,110)
#Sol
arcade.draw_triangle_filled(600,600,650,550,500,575,arcade.color.FLUORESCENT_ORANGE)
arcade.draw_triangle_filled(610,560,700,500,525,512,arcade.color.FLUORESCENT_ORANGE)
arcade.draw_triangle_filled(620,520,750,475,550,450,arcade.color.FLUORESCENT_ORANGE)
arcade.draw_triangle_filled(630,480,760,450,600,400,arcade.color.FLUORESCENT_ORANGE)
arcade.draw_triangle_filled(690,450,770,425,650,360,arcade.color.FLUORESCENT_ORANGE)
arcade.draw_triangle_filled(720,420,790,410,720,325,arcade.color.FLUORESCENT_ORANGE)
arcade.draw_triangle_filled(770,410,820,410,770,310,arcade.color.FLUORESCENT_ORANGE)
arcade.draw_circle_filled(800,600,200,arcade.color.CHROME_YELLOW)
#Nube arriba
arcade.draw_ellipse_filled(500,550,150,100,arcade.color.FLORAL_WHITE)
arcade.draw_ellipse_filled(500,500,150,100,arcade.color.FLORAL_WHITE)
arcade.draw_ellipse_filled(575,525,150,100,arcade.color.FLORAL_WHITE)
arcade.draw_ellipse_filled(425,525,150,100,arcade.color.FLORAL_WHITE)
#Nube abajo
arcade.draw_ellipse_filled(250,150,150,100,arcade.color.FLORAL_WHITE)
arcade.draw_ellipse_filled(250,100,150,100,arcade.color.FLORAL_WHITE)
arcade.draw_ellipse_filled(325,125,150,100,arcade.color.FLORAL_WHITE)
arcade.draw_ellipse_filled(175,125,150,100,arcade.color.FLORAL_WHITE)
#Nube izquierda
arcade.draw_ellipse_filled(200,450,150,100,arcade.color.FLORAL_WHITE)
arcade.draw_ellipse_filled(200,400,150,100,arcade.color.FLORAL_WHITE)
arcade.draw_ellipse_filled(275,425,150,100,arcade.color.FLORAL_WHITE)
arcade.draw_ellipse_filled(125,425,150,100,arcade.color.FLORAL_WHITE)
#Nube derecha
arcade.draw_ellipse_filled(700,300,150,100,arcade.color.FLORAL_WHITE)
arcade.draw_ellipse_filled(700,250,150,100,arcade.color.FLORAL_WHITE)
arcade.draw_ellipse_filled(775,275,150,100,arcade.color.FLORAL_WHITE)
arcade.draw_ellipse_filled(625,275,150,100,arcade.color.FLORAL_WHITE)
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
#Final
arcade.finish_render()
arcade.run()