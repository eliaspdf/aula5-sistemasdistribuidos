import threading
import time

saldo = 1000

def sacar(valor):
    global saldo
    
    saldo.atual = saldo
    time.sleep(0.01)
    saldo = saldo.atual - valor
    
threads = []

for i in range(10):
    t = threading.Thread(target=sacar, args=(50,))
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()
    
print("saldo esperado: 500")
print("saldo obtido:", saldo)

RESULTADO

saldo esperado: 500
saldo obtido: 1000
