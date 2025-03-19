import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

"""
Model epidemiologiczny SIR z implementacją metod solve_ivp.
Cel: Wykres liczby zakażonych I(t) w czasie.
"""

# Początkowe warunki
n_0 = 10**6             
i_0 = 10               
s_0 = 10**5                            
r_0 = n_0 - i_0 - s_0     

# Stałe
B = 5.2e-4                
g = 52                
a = 1/80                  
b = a                    

# Parametry czasowe
T = 20  # lat               
dt = 0.001                  
time = np.arange(0, T, dt) 

# model SIR
def function_I(state, t, a, b, B, g):
    s_t, i_t, r_t = state 

    dS = b * n_0 - B * s_t * i_t - a * s_t   # Zmiana liczby podatnych
    dI = B * s_t * i_t - g * i_t - a * i_t   # Zmiana liczby zakażonych
    dR = g * i_t - a * r_t                   # Zmiana liczby osób z odpornością
    
    return [dS, dI, dR]

delta = 0.2
# Parametry systemu
p = (a, b, B, g)  # stałe
p_1=(a, b*(1-delta), B, g) # track if it is a or b changed
p_2=(a, b*(1+delta), B, g) # track if it is a or b changed
p_3=(a, b, B*(1-delta), g)
p_4=(a, b, B*(1+delta), g)
p_5=(a, b, B, g*(1-delta))
p_6=(a, b, B, g*(1+delta))
y0 = [s_0, i_0, r_0]  # Warunki początkowe

# Rozwiązanie za pomocą solve_ivp
t_span = (0.0, T)
result_solve_ivp = solve_ivp(
    lambda t, y: function_I(y, t, *p), t_span, y0, t_eval=time
)
result_solve_ivp_1 = solve_ivp(
    lambda t, y: function_I(y, t, *p_1), t_span, y0, t_eval=time
)
result_solve_ivp_2 = solve_ivp(
    lambda t, y: function_I(y, t, *p_2), t_span, y0, t_eval=time
)
result_solve_ivp_3 = solve_ivp(
    lambda t, y: function_I(y, t, *p_3), t_span, y0, t_eval=time
)
result_solve_ivp_4 = solve_ivp(
    lambda t, y: function_I(y, t, *p_4), t_span, y0, t_eval=time
)
result_solve_ivp_5 = solve_ivp(
    lambda t, y: function_I(y, t, *p_5), t_span, y0, t_eval=time
)
result_solve_ivp_6 = solve_ivp(
    lambda t, y: function_I(y, t, *p_6), t_span, y0, t_eval=time
)

I_solve_ivp = result_solve_ivp.y[1]      # niezmienione parametry
# delta = 0.2
I_solve_ivp_1 = result_solve_ivp_1.y[1]  # zmieniony parametr b*(1-delta)
I_solve_ivp_2 = result_solve_ivp_2.y[1]  # zmieniony parametr b*(1+delta)
I_solve_ivp_3 = result_solve_ivp_3.y[1]  # zmieniony parametr B*(1-delta)
I_solve_ivp_4 = result_solve_ivp_4.y[1]  # zmieniony parametr B*(1+delta)
I_solve_ivp_5 = result_solve_ivp_5.y[1]  # zmieniony parametr g*(1-delta)
I_solve_ivp_6 = result_solve_ivp_6.y[1]  # zmieniony parametr g*(1+delta)

def prints_plot():
    plt.figure(figsize=(10, 6))
    plt.title("Liczba zakażonych w czasie: I(t)")
    plt.xlabel("Czas (lata)")
    plt.ylabel("Liczba osób")
    plt.legend()
    plt.grid()
    

""" 
W zależności od oczekiwanego wykresu, należy odkomentować odpowiednią linijkę kreującą odpowiedni wykres.
"""
prints_plot()

# 80% i 120% wartości danego parametru odnoszą się do orginalnej jego wielkości
plt.plot(time, I_solve_ivp_1, label=r"80% b (solve_ivp)", linestyle='solid')
plt.plot(time, I_solve_ivp_2, label=r"120% b (solve_ivp)", linestyle='solid')
plt.show()
prints_plot()
plt.plot(time, I_solve_ivp_3, label=r"80% beta (solve_ivp)", linestyle='solid')
plt.plot(time, I_solve_ivp_4, label=r"120% beta (solve_ivp)", linestyle='solid')
plt.show()
prints_plot()
plt.plot(time, I_solve_ivp_5, label=r"80% gamma (solve_ivp)", linestyle='solid')
plt.plot(time, I_solve_ivp_6, label=r"120% gamma (solve_ivp)", linestyle='solid')
plt.show()
