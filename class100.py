class Car(object):
    def __init__(self,model,colour,speedLimit,company):
             self.colour = colour
             self.company = company
             self.model = model
             self.speedlimit = speedLimit

    def start(self):
        print('started')

    def stop(stop):
        print('stoped')

    def accelerate(self):
        print('accelarated')

MJ = Car('Ac-0','black',200,'MJ') 
print(MJ.colour)
print(MJ.company)
print(MJ.model)
print(MJ.speedlimit)

MJ.start()
MJ.stop()
MJ.accelerate()