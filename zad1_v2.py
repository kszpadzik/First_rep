import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history
import numpy as np
import math
import matplotlib.pyplot as plt

# a) Rzucimy okiem na tutorial o podstawowej optymalizacji: 
options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2, options=options)
best_cost, best_pos = optimizer.optimize(fx.sphere, iters=1000)
print(f"Best cost: {best_cost}, Best position: {best_pos}\n")


# b) Spróbujmy teraz dodać ograniczenia dla dziedziny (obszaru), w którym szukamy minimum. Trzeba 
# ustalić ograniczenie górne i dolne dla wszystkich zmiennych, weźmy minimum 1, maksimum 2 – dla 
# wszystkich zmiennych. 
# I oczywiście ograniczenia trzeba przekazać jako parametr do optimizera poprzez argument: 
x_min = [1, 1]
x_max = [2, 2]
bounds = (x_min, x_max)
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2, options=options, bounds=bounds)
best_cost, best_pos = optimizer.optimize(fx.sphere, iters=1000)
print(f"Best cost: {best_cost}, Best position: {best_pos}\n")

# Zmieńmy teraz ten kod tak, by rozwiązywał problem inżynieryjny. Po pierwsze trzeba zmienić 
#limity: min 0, max 1 dla wszystkich sześciu zmiennych. Oczywiście dimensions trzeba ustawić na 6.  
# Uwaga, zamiast wypisywać długie wektory limitów ręcznie, można użyć numpy: np.zeros(6), np.ones(6). 
x_min = np.zeros(6)
x_max = np.ones(6)
bounds = (x_min, x_max)

# Define the endurance function
def endurance(particles):
    return np.array([
        math.exp(-2 * (y - math.sin(x))**2) + math.sin(z * u) + math.cos(v * w)
        for x, y, z, u, v, w in particles
    ])

# Popraw funkcję endurance, by pobierała tablicę sześciu argumentów, a nie sześć oddzielnych argumentów 
# • Dopisz funkcję f, która przebiegnie po całym roju uruchamiając dla każdej cząstki endurance. 
# • Wrzuć f do optymalizatora. 
optimizer = ps.single.GlobalBestPSO(n_particles=50, dimensions=6, options=options, bounds=bounds)
best_cost, best_pos = optimizer.optimize(lambda x: -endurance(x), iters=1000)  # Add a minus to maximize
# print(f"Best cost (negative endurance): {best_cost}, Best position: {best_pos}\n")

#  Powyższy wynik jest oczywiście zły, bo funkcja szuka minimum zamiast maximum. Czy można to 
# zmienić w prosty sposób w optimizerze? Ja niestety nie znalazłem takiej opcji        Trzeba więc 
# zrobić sztuczkę, taką jak przy algorytmie genetycznym i dopisać minus do funkcji endurance. 
# Teraz wynik jest już dobry (podobny do tego z algorytmu genetycznego), ale oczywiście z minusem:
print("e) dobry wynik:")
true_best_cost = -best_cost  # Convert negative cost to positive endurance
print(f"Best cost (endurance): {true_best_cost}, Best position: {best_pos}\n")

# Wyświetlmy jeszcze wykres kosztu zgodnie ze wskazówkami z:  https://pyswarms.readthedocs.io/en/latest/api/pyswarms.utils.plotters.html  
plot_cost_history(optimizer.cost_history)
plt.title("Cost History")
plt.xlabel("Iteration")
plt.ylabel("Cost")
plt.show()