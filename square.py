import pygame
def squre_draw(dense, surface, sscreen_X, screen_Y,
               corner_1X, corner_1Y, 
               corner_2X, corner_2Y, 
               corner_3X, corner_3Y,  
               corner_4X, corner_4Y, 
               color):
    #screen = pygame.display.set_mode((screen_X, screen_Y))
    pygame.draw.line(surface, color ,
                     (corner_1X, corner_1Y), 
                     (corner_2X, corner_2Y))
    pygame.draw.line(surface, color ,
                      (corner_2X, corner_2Y), 
                      (corner_3X, corner_3Y))
    pygame.draw.line(surface, color ,
                      (corner_3X, corner_3Y), 
                      (corner_4X, corner_4Y))
    pygame.draw.line(surface, color ,
                      (corner_4X, corner_4Y), 
                      (corner_1X, corner_1Y))

    for dis_ in range(dense):

        dis = dis_/dense

        line_X_1 = (corner_1X - corner_2X) * dis
        line_Y_1 = (corner_1Y - corner_2Y) *dis
        line_X_2 = (corner_3X - corner_4X) *dis
        line_Y_2 = (corner_3Y - corner_4Y) *dis

        line_X_1=  line_X_1 /1
        line_X_2= line_X_2 /-1
        line_Y_1=  line_Y_1 /1
        line_Y_2= line_Y_2 /-1
    

        point1X = line_X_1 + corner_2X
        point1Y = line_Y_1 + corner_2Y
        point2X = line_X_2 + corner_3X
        point2Y = line_Y_2 + corner_3Y



        pygame.draw.line(surface, color ,
                          (point1X, point1Y), 
                          (point2X, point2Y))
        pygame.draw.line(surface, color ,
                                  (point1X, point1Y), 
                                  (point1X, point1Y),4)
        pygame.draw.line(surface, color ,
                                  (point2X, point2Y), 
                                  (point2X, point2Y),4)