import numpy as np
import matplotlib.pyplot as plt

class Plot(object):

    def __init__(self, ping_list):
        self.ping_list = ping_list
        self.len = len(ping_list)
        self.good = 0
        self.moderate = 0
        self.bad = 0
        self.terrible = 0
        self.show()
        self.show_bar()

    def show(self):
        x = 10*np.array(range(self.len))

        plt.plot( x, self.ping_list) # green bolinha
        plt.plot( x, self.ping_list, color='orange') # linha pontilha orange

        #plt.plot( x, data2, 'r^') # red triangulo
        #plt.plot( x, data2, 'k--', color='blue')  # linha tracejada azul

        plt.axis([0, self.len, 0, 3500])
        plt.title("Gráfico de tempo")

        plt.grid(True)
        plt.xlabel("time (s)")
        plt.ylabel("response time (ms)")
        plt.show()

    def show_bar(self):
        self.rate_time()
        plt.rcdefaults()
        fig, ax = plt.subplots()
        data = ('Good (100ms)', 'Moderate (200ms)', 'Bad (300ms)', 'Terrible (300ms+)')
        y_pos = np.arange(len(data))
        ax.barh(y_pos, [self.good/self.len,self.moderate/self.len,self.bad/self.len,self.terrible/self.len], align='center',
                color='red', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(data)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Percentage')
        ax.set_title('Response time rate!')
        plt.show()

    def rate_time(self):
        for x in range(0, self.len):
            if self.ping_list[x] <= 100:
                self.good +=1
            elif self.ping_list[x] <= 200:
                self.moderate +=1
            elif self.ping_list[x] <= 300:
                self.bad +=1
            else:
                self.terrible +=1






