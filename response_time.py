

class ResponseTime(object):
    send = None
    received = None
    lost = None
    ping_list = []

    def __init__(self, file):
        self.file = file
        self.send = 0
        self.received = 0
        self.lost = 0

    def analizer(self):

        for x in range(0, len(self.file)):
            line = self.file[x]

            if 'Resposta' in line:
                self.send += 1
                self.received += 1
                string = ''
                i = 44

                while line[i] != 'm':
                    string += line[i]
                    i += 1

                self.ping_list.append(int(string))

            elif 'Esgotado' in line:
                self.send += 1
                self.lost += 1
                self.ping_list.append(3000)


        print('Pacotes: Enviados = {}, Recebidos = {}, Perdidos = {}'.format(self.send, self.received, self.lost))
        return self.ping_list