import arcade

my_window = arcade.open_window(1000,900, "Our First Window Demo")
arcade.set_background_color(arcade.color.PURPLE_NAVY)
arcade.start_render()

arcade.draw_circle_filled(500, 500, 250, arcade.color.ALLOY_ORANGE)
arcade.draw_triangle_filled(425,375, 500, 475, 575, 375, arcade.color.YELLOW)
arcade.draw_arc_outline(500, 370, 300, 100, arcade.color.YELLOW, -180, 0, 7)
arcade.draw_xywh_rectangle_filled(220, 740, 560, 20, arcade.color.BLACK)
arcade.draw_xywh_rectangle_filled(320, 760, 350, 100, arcade.color.BLACK)
arcade.draw_arc_filled(380,490, 100, 220, arcade.color.YELLOW, 0, 180,)
arcade.draw_arc_filled(580,490, 100, 220, arcade.color.YELLOW, 0, 180,)
arcade.finish_render()
arcade.run()