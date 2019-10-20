import unittest
from PSO import Particle
import cv2


class Test_particle(unittest.TestCase):

    def setUp(self):
        #read image
        self.refimage = cv2.imread('data/ref.bmp')
        self.landscape = cv2.imread('data/landscape.jpg')

        #gray scale image
        self.refimage = cv2.cvtColor(self.refimage, cv2.COLOR_BGR2GRAY)
        self.landscape = cv2.cvtColor(self.landscape, cv2.COLOR_BGR2GRAY)


    def test_count_similarity(self):
        particle = Particle(55, 47, 1, 90)
        print(particle.count_difference_measure(self.refimage, self.landscape))

    def test_count_similarity_same_object(self):
        particle = Particle(0, 0, 0, 0)
        print(particle.count_difference_measure(self.refimage, self.refimage))

    def test_move(self):
        particle = Particle(0, 0, 0, 0)
        particle.velocity = [1, 1, 1, 1]
        particle.move()
        self.assertEqual([1, 1, 1, 1.0], particle.position)

    def test_count_velocity(self):
        particle = Particle(0, 0, 0, 0)
        particle.compute_velocity([1, 2, 3, 4])
        self.assertEqual(4, len(particle.velocity))


if __name__ == '__main__':
    unittest.main()