class data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes 
        self.ano = ano

    def formatada(self):
        print("{}/{}/{}".format(self.dia,self.mes,self.ano))


d = data("29", "09", "2021")
d.formatada()
