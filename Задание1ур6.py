from time import sleep


class TrafficLight:
    _states = {'красный': 7, 'желтый': 2, 'зеленый': 10}
    _color = ''

    def running(self):
        for color, time in self._states.items():
            self._color = color

            print(f"Светофор '{self._color}' "
                  f"на {time} секунд")

            sleep(time)



if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()
