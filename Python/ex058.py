import random
l = [0,1,2,3,4,5,6,7,8,9,10]
r = random.choice(l)
a = int(input("Advinhe o numero de 0 a 10 que pensei"))
t = 1
while not a == r:
    t += 1
    r = random.choice(l)
    int(input("Errou, pensei no {}, tente novamente".format(r)))
if a == r:
    print(" {} Acertou com {} tentativas, parabens".format(r,t))
# ou
# c = random.randint(0,10)
#acertou = False
#while not acertou:
#   a = int(input("Advinhe o numero de 0 a 10 que pensei"))
#   if a == c
#       acertou = True
#   else:
#   if a < c
        #print("Mais, tente de novo")
#   elif a > c
#       print("Menos, tente de novo")
#print("Acertou com {} tentativas.".format(t))
