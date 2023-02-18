import pygame

class Node:
    def __init__(self, body, x, y, width, nw=None, ne=None, sw=None, se=None):
        self.nw = nw
        self.ne = ne
        self.sw = sw
        self.se = se
        self.body = body
        self.mass = 0
        self.isLeaf = True
        self.x = x
        self.y = y 
        self.width = width
        self.massx = 0
        self.massy = 0

    
    def __str__(self):
        return f'[body:{self.body}, mass: {self.mass}, nw: {self.nw}\nne: {self.ne}\nsw: {self.sw}\nse: {self.se}\nx: {self.x}, y: {self.y}, width: {self.width}]'


    def draw(self, screen):
        # print(self.x, self.y, self.width)
        pygame.draw.rect(screen, [0, 255, 0], [int(self.x), int(self.y), self.width, self.width], 1)



    # def calculate_node_mass(self):
    #     if not self.root:
    #         return 0

    #     elif self.root.isLeaf:
    #         return 0
        
            
    #     elif self.root.body:
    #         self.root.mass = self.root.body.mass
    #         return self.root.body.mass
            
    #     else:
    #         m = 0
    #         m += self.root.nw.calculate_node_mass()
    #         m += self.root.ne.self.calculate_node_mass()
    #         m += self.root.sw.self.calculate_node_mass()
    #         m += self.root.se.calculate_node_mass()
    #         self.root.mass = m
    #         return m

        
    # def calculate_center_x(self):
    #     if not self.root or not self.root.mass:
    #         return 0
        
    #     if self.root.body:
    #         return self.root.body.x * self.root.body.mass

    #     m = 0
    #     m += self.root.nw.calculate_center_x()
    #     m += self.root.ne.calculate_center_x()
    #     m += self.root.sw.calculate_center_x()
    #     m += self.root.se.calculate_center_x()

    #     return m

    # def calculate_center_y(self):
    #     if not self.root or not self.root.mass:
    #         return 0
        
    #     if self.root.body:
    #         return self.root.body.y * self.root.body.mass

    #     m = 0
    #     m += self.root.nw.calculate_center_y()
    #     m += self.root.ne.calculate_center_y()
    #     m += self.root.sw.calculate_center_y()
    #     m += self.root.se.calculate_center_y()

    #     return m

    # def calculate_center_mass(self):
    #     if self.root:
    #         if self.root.mass:
    #             self.root.massx = self.calculate_center_x(self.root) / self.root.mass
    #             self.root.massy = self.calculate_center_y(self.root) / self.root.mass
    #         self.root.nw.calculate_center_mass()
    #         self.root.ne.calculate_center_mass()
    #         self.root.sw.calculate_center_mass()
    #         self.root.se.calculate_center_mass()


    # def calculate_net_force(self, body):
        
    #     if self.root:
    #         if self.root.body and self.root.body != body:
    #             d = math.sqrt((self.root.body.x - body.x)**2 + (self.root.body.y - body.y)**2)
    #             body.calculate_force(self.root.body.x, self.root.body.y, self.root.body.mass, d)
    #         elif not self.root.isLeaf:
    #             d = math.sqrt((self.root.massx - body.x)**2 + (self.root.massy - body.y)**2)
    #             if d > 0 and self.root.width / d < Config.THETA:
    #                 body.calculate_force(self.root.massx, self.root.massy, self.root.mass, d)
    #             else:
    #                 self.root.nw.calculate_net_force(body)
    #                 self.root.ne.calculate_net_force(body)
    #                 self.root.nw.calculate_net_force(body)
    #                 self.root.se.calculate_net_force(body)

    # def draw_bounds(self, screen):
    #     root = self.root
    #     if root:
    #         root.draw(screen)
    #         root.nw.draw_bounds(screen)
    #         root.ne.draw_bounds(screen)
    #         root.sw.draw_bounds(screen)
    #         root.se.draw_bounds(screen)


    # def insert_tree(self, root, body, bodies):

    #     if not root:
    #         return 

    #     if root.isLeaf:
    #         root.body = body
    #         body.region_width = root.width
    #         root.isLeaf = False
        
    #     elif root.body:
    #         if abs(root.body.x - body.x) <= 0.2 and abs(root.body.y - body.y) <= 0.2:
    #             if root.body.mass < body.mass:
    #                 root.body.r = body.r
    #                 root.body.x = body.x
    #                 root.body.y =body.y
    #                 root.body.vx = body.vx
    #                 root.body.vy = body.vy
    #             root.body.mass += body.mass
    #             bodies.remove(body)
    #         else:
    #             tmp = root.body
    #             root.body = None
    #             w = root.width / 2
    #             x = root.x
    #             y = root.y
    #             root.nw = Node(None, x, y, w)
    #             root.ne = Node(None, x + w, y, w)
    #             root.se = Node(None, x + w, y + w, w)
    #             root.sw = Node(None, x, y + w, w)

    #             self.insert_tree(root, tmp, bodies)
    #             self.insert_tree(root, body, bodies)
        
    #     else:
    #         x = root.x
    #         y = root.y
    #         width = root.width / 2
    #         next_check = None
    #         if body.x >= 0 and body.x <= 800 and body.y >= 0 and body.y <= 800:
    #             if body.x < x + width:
    #                 if body.y >= y and body.y < y + width:
    #                     next_check = root.nw
    #                 else:
    #                     next_check = root.sw
    #             else:
    #                 if body.y < y + width:
    #                     next_check = root.ne
    #                 else:
    #                     next_check = root.se

    #         self.insert_tree(next_check, body, bodies)

    #     return root

    # def insert(self, body, bodies):
    #     self.insert_tree(self.root, body, bodies)
        