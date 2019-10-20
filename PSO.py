import random
import cv2
import math

w = 10
c1 = 1
c2 = 2

class PSO(object):

    def __init__(self, c1=1, c2=1, W=1):
        self.gbest_position = [0, 0, 0, 0]
        self.gbest_value = float('inf')
        self.c1 = c1
        self.c2 = c2
        self.W = W


class Particle(object):

    def __init__(self, x, y, s, tau, c1=1, c2=1, W=1):

        #TODO  decorate: accepting only vaid values
        self.position = [x, y, s, tau*(math.pi/180)]
        self.velocity = [random.uniform(-1, 1) for i in range(0, 4)]
        self.pbest_position = self.position
        self.pbest_value = float('inf')

        self.c1 = c1
        self.c2 = c2
        self.W = W

    def count_difference_measure(self, ref_image, landscape_image, nbits=8):
        """
        Count difference between images in gray scale
        #TODO catch zero devision error
        """
        x = self.position[0]
        y = self.position[1]
        s = self.position[2]
        tau = self.position[3]
        Pinv = 0
        m, n = ref_image.shape
        err_sol = 0
        for i in range(0, m):
            for j in range(0, n):
                ddX = j - n/2
                ddY = i - m/2

                I = int(x + s*(ddX * math.cos(tau) - ddY * math.sin(tau)))
                J = int(y + s *(ddX * math.sin(tau) + ddY * math.cos(tau)))
                cv2.putText(landscape_image, ".", (I, J), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))
                try:
                    err_sol = err_sol + abs(int(ref_image[i, j])-int(landscape_image[I, J]))
                except IndexError:
                    #print(I, J)
                    #print(landscape_image.shape)
                    Pinv = Pinv+1

        err_max = (2 ** (nbits)) * ((m * n) - Pinv)
        eval_sol = (err_max-err_sol)/err_max
        cv2.imshow('image', landscape_image)
        cv2.waitKey(0)
        return eval_sol

    def compute_velocity(self, gbest_position):

        local_factor = [self.c1 * random.random()*(self.pbest_position[i] - self.position[i]) for i, _ in enumerate(self.position)]
        global_factor = [(random.random()*self.c2)*(gbest_position[i] - self.position[i]) for i, _ in enumerate(self.position)]

        self.velocity = [self.W * self.velocity[i] + local_factor[i] + global_factor[i] for i, _ in enumerate(local_factor)]
        self.move()

    def move(self):
        self.position = [self.position[i]+self.velocity[i] for i, _ in enumerate(self.position)]


'''
PSO = PSO(1, 1, 1)
p = Particle(55, 47, 1, 90)
p.compute_velocity([1, 2, 3, 4 ])
print(p.velocity)
print(p.position)

'''