from time import sleep
from itertools import cycle

class TrafficLight:
    __color = ['  ', [7, 3, 5], ['\033[41m\033[1m', '\033[43m\033[1m', '\033[42m\033[1m']]
    def running(self):
        color_lst = ['', '']
        for n in cycle((0, 1, 2)):
            color_lst[1] = self.__color[2][n]
            print(f'\r({color_lst[int(n == 0)]}{self.__color[0]}\033[0m)'
                  f'({color_lst[int(n == 1)]}{self.__color[0]}\033[0m)'
                  f'({color_lst[int(n == 2)]}{self.__color[0]}\033[0m)', end='')
            sleep(self.__color[1][n])

traf_light = TrafficLight()
traf_light.running()
        