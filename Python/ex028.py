import random
import time
n = int(input("Advinhe o numero de 0 a 5 que pensei"))
x = [0,1,2,3,4,5]
y = random.choice(x)
time.sleep(0.5)
print('Processando...')
if n == y:
    print("Acertou pensei no numero {}".format(n))
else:
    print("Errou, pensei em {}".format(y))
