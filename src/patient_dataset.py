
import pandas as pd
data = pd.read_csv('patients-data.csv')
days = list(set(data.AdmitDay))

# aggregate admit per day
day_admit = {}


def __aggregate():
    for day in days:
        num_admit = len(data[data.AdmitDay == day])
        day_admit[day] = num_admit

__aggregate()
        
# plotting

import matplotlib.pyplot as plt


def plot_admit_per_day():
    plt.figure(figsize=(12,4))
    ordered_admits = []
    for k, v in sorted(day_admit.items()):
        ordered_admits.append(v)
    plt.plot(ordered_admits, '-*')
    plt.title('Number of admitted patients $y$ on a day $x$')
    plt.xticks(range(len(day_admit)), sorted(day_admit.keys()), rotation = 90)
    plt.grid();plt.show()
    

def plot_stay_density():
    days = data.DaysStay
    plt.hist(days, bins=max(days))
    plt.title("Total number of patients $y$ that stay $x$ days");plt.show()
    plt.hist(days, bins=max(days), normed=True)
    plt.title("The prob. density $y$ that a patient stays $x$ days");plt.show()
    print("notice the mean of the distribution is approximately = 2, which was originally used in poisson.rvs(mu=2, size=1) to generate the random length of stay in the dataset.")