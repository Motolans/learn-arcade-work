'''
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
'''

import arcade

#create window
arcade.open_window(600, 600, "Drawing Example")

#set background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
#note, alpha channel in arcade is 0 - 255, not 0 - 1
#arcade.set_background_color((189, 55, 180, 170))

#get ready to draw
arcade.start_render()

#drawing code goes here

#"grass"
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

#"tree trunk"
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

#"tree top"
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

#ellipses and relationship to rectangles
#arcade.draw_rectangle_outline(300, 300, 250, 200, arcade.csscolor.BLACK, 3)
#arcade.draw_ellipse_outline(300, 300, 250, 200, arcade.csscolor.RED, 3)

#another tree, ellipse top
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)

#yet another tree, arc top
#arc is centered at (300, 340) with a width of 60 and height of 100
#The starting angle is 0, and ending angle is 180
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

#still more tree, triangle top
#Triangle requires three points:
# ie, (400, 400), (370, 320), (430, 320)
arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)

#polygonal tree
#polygons use a sequence of x points
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500,400), (480, 360), (470, 320), (530, 320), (520, 360)), arcade.csscolor.DARK_GREEN)

#sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

#rays to the left, right, up, and down
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)

#diagonal rays
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

#Draw text at (150, 230) with a font of 24 pts)
arcade.draw_text("Arbor Day - Plant a Tree!", 150, 230, arcade.color.BLACK, 24)

#finish drawing
arcade.finish_render()

#keep window open
arcade.run
