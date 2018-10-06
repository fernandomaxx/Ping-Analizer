from response_time import ResponseTime
from plot import Plot

if __name__ == '__main__':
    ref_file = open("arquivo.txt", 'r')
    file = ref_file.readlines()
    Plot(ResponseTime(file).analizer())

