# dS/dt = -BIS/N
# dI/dt = BIS/N - gI
# dR/dt = gI

# B is the average number of people an infectious person will infect
# g is the probability of converting from contagious to non-contagious
# average number of contagious days is 1/g
# R0 or the basic reproduction number is B/g

import math

import matplotlib.pyplot as plt

N = population = 10_000
B = 0.3  # contact rate (per day)
g = 0.1  # recovery rate (per day)  -> avg infectious period = 1/g = 10 days
# R0 = B/g = 3.0

# Let's define some other variables
# On average, 17.5% of people are vaccinated today
# OF THE VACCINATED, they can be revaccinated every 12 months
# probability per day of vaccination is 0.175*(1/365)
# We will assume that vaccination is drawn randomly from S, I, and R
v = 0.175 * (1 / 365)

# Immunity goes down asymptotically
# We will update immunity/recovered to be R(t) = e^(-lambda * t)
# S then needs to be updated to get the rate of people coming from recovered
# Immunity is 60% after 9 months
# 0.60 = e^(-lambda * 9 months*30 days/month)
_lambda = -1 * math.log(0.60) / 270

days = 1365

# Start with a population of 10_000 people, 1 of whom is infected
S, I, R = [population - 1], [1], [0]
S_t = S[0]
I_t = I[0]
R_t = R[0]

for day in range(days):
    # dS = -B * I_t * S_t / N
    # dI = B * I_t * S_t / N - g * I_t
    # dR = g * I_t

    # Including vaccination and loss of immunity
    # Vaccination term of R can be dropped-- it stays in R
    # Vaccination term of I can be dropped-- takes 2 weeks to become immune
    dS = -B * I_t * S_t / N - v * S_t + _lambda * R_t
    dI = B * I_t * S_t / N - g * I_t
    dR = g * I_t + v * S_t - _lambda * R_t

    # What happens if there's another jump from bats to humans on day 200?
    # if day == 1200:
    #     dS -= 1000
    #     dI += 1000

    S_t += dS
    I_t += dI
    R_t += dR
    S.append(S_t)
    I.append(I_t)
    R.append(R_t)

# Plot
t = range(days + 1)
plt.figure(figsize=(10, 5))
plt.plot(t, S, label="Susceptible")
plt.plot(t, I, label="Infected")
plt.plot(t, R, label="Recovered")
plt.xlabel("Days")
plt.ylabel("People")
plt.title(f"SIR Model  (N={N}, β={B}, γ={g}, R₀={B/g:.1f})")
plt.legend()
plt.tight_layout()
plt.show()
plt.show()
