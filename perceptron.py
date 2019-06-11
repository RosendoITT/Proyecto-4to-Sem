'''
	Perceptron
	 = w + N * (d(k) - y) * x(k)

	p1 = -1
	p2 = 1
 w= El peso actual  une a la neurona i  de la capa de netrada y la nu j de la cap de salida
 n= constantes 0 1 aprende la la red
 d(k)= El estadod e la neurona de la capa de salida j
 y= El valor deseado para la neurona
x(k)= El estado de la neurona de la capa de entrada i 
	
'''
# Importamos la libreria random
import random

#creamos clase
class Perceptron:
    def __init__(self, sample, exit, learn_rate=0.01, epoch_number=1000, bias=-1):

#atributos de class
        self.sample = sample    #entrenamiento 
        self.exit = exit # Salida esperada para cada dato
        self.learn_rate = learn_rate # Que tanto aprendera la red
        self.epoch_number = epoch_number 
        self.bias = bias # Bias de la red
        self.number_sample = len(sample)  # Numero de ejemplos
        self.col_sample = len(sample[0])   # Columnas de los datos
        self.weight = []  # Lista de pesos

    def trannig(self): # Metodo de entrenamiento
        for sample in self.sample:  # Se recorren los datos de entrenamiento
            sample.insert(0, self.bias)# Se inserta el bias en la primera pocisión

        for i in range(self.col_sample):
           self.weight.append(random.random())  # Asignamos pesos aleatorios

        self.weight.insert(0, self.bias) # Insertamos el bias en los pesos

        epoch_count = 0

        while True:
            erro = False
            for i in range(self.number_sample):
                u = 0
                for j in range(self.col_sample + 1):  # Función de activación

                    u = u + self.weight[j] * self.sample[i][j]
                y = self.sign(u)  # Comprobar el valor
                if y != self.exit[i]:

                    for j in range(self.col_sample + 1):


# Función de entrenamiento
# w = w + N(d(k)-y) x(k)

                        

                        self.weight[j] = self.weight[j] + self.learn_rate * (self.exit[i] - y) * self.sample[i][j]
                    erro = True
            epoch_count = epoch_count + 1  # Se aumenta el numero de epoch
            if erro == False:
                print(('Inserta nuevos numeros =D ',epoch_count))  # Mostramos el valor de epoch
                print('---------------------------------------\n')
                break

    def sort(self, sample):


        #Se inserta el bias 
       # sera una neurona que siempre estara activada.



        
        sample.insert(0, self.bias)
        u = 0
        for i in range(self.col_sample + 1):

             # Función de activación
            u = u + self.weight[i] * sample[i]

        y = self.sign(u)  # Comprobamos el valor de la función de activación

        if  y == -1:   # Si y es igual a -1, la clasificación corresponde a P1
            print(('Ejemplo: ', sample))
            print('Categoria: P1')
        else:
            print(('Ejemplo: ', sample))
            print('Categoria: P2')

    def sign(self, u):
        return 1 if u >= 0 else -1  # Si y es igual a 1, la clasificación corresponde a P2


# Datos de entrenamiento
        
samples = [
    [1, 4],
    [5, 7],
    [1, 3],
    [6, 9],
    [1,2],
    [2,1],
    [8,4],
    [9,4],
    [6,8],
]

exit = [-1, 1, -1, 1, -1, -1, 1, 1, 1]  # Clasificación de los datos de entrenamiento (salidas que esperamos para cada conjunto de dato)


#Intancia de nuestra neurona
network = Perceptron(sample=samples, exit = exit, learn_rate=0.01, epoch_number=1000, bias=-1)


# Entrenamos a la neurona
network.trannig()

"""
Le pedimos datos para entrenar.
Luego mostramos el resultados
"""
while True:
    sample = []
    for i in range(2):
        sample.insert(i, float(input('Inserte un numero >:c :3 : ')))
    network.sort(sample) # Clasificacipon de nuevos
