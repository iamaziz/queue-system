
# coding: utf-8

# ### Generate imaginary patients dataset

# In[1]:

get_ipython().magic(u'autosave 30')


# In[2]:

from scipy.stats import poisson
from random import randint
from datetime import datetime
from faker import Factory
fake = Factory.create()

def patient_name():
    return fake.name()


def admission_date():
    mm, dd, yy = randint(3, 4), randint(1, 28), randint(2015, 2015)
    d = datetime(yy, mm, dd)
    return d.date()


def stay_length():
    mu = 2                         # an arbitrary mean of how long a patient stay at hospital
    r = poisson.rvs(mu, size=1)[0] # random lenght(stay) based on the arbitrary mean
    return r


def is_icroom():
    mu = 0.1                      # approximately! assuming ~10% of patients go into IC rooms
    r = poisson.rvs(mu, size=1)[0]
    if r > 0:
        return 'yes'
    return 'no'


def is_admitted(duration):
    return 1


def patient_log():

    name = patient_name()
    admit_date = admission_date()
    stay = stay_length()
    ic_room = is_icroom()

    return [name, admit_date, stay, ic_room]


[type(f) for f in patient_log()]


# ### write patients data into csv

# In[3]:

import pandas as pd
import csv

def data_report():

    NUM_PATIENTS = 2000

    with open('patients-data.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Name', 'AdmitDay', 'DaysStay', 'ICRoom'])
        for i in range(NUM_PATIENTS):
            spamwriter.writerow(patient_log())


    def icroom_percentage():
        n = len(data[data.ICRoom == 'yes'])
        percent = float(n) / NUM_PATIENTS * 100
        return percent

    def avg_stay():
        avg = sum(data.DaysStay) / NUM_PATIENTS
        return avg


    # validate dataset consistency
    data = pd.read_csv('patients-data.csv') # or: pd.DataFrame.from_csv
    print("{} patients".format(NUM_PATIENTS))
    print("{}% admitted into IC Room".format(icroom_percentage()))
    print("{} day(s) is the average stay of a patient".format(avg_stay()))
    return data

data_report()


# ### plotting patients dataset

# In[4]:

data = pd.read_csv('patients-data.csv')


# **Aggregate patients' admissions per date into a dictionary**
#
# key: the date, value: number of admission

# In[5]:

days = list(set(data.AdmitDay))
day_admit = {}
for day in days:
    num_admit = len(data[data.AdmitDay == day])
    day_admit[day] = num_admit


# In[6]:

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt


# plotting with ordered dates

# In[7]:

plt.figure(figsize=(12,4))
ordered_admits = []
for k, v in sorted(day_admit.items()):
    ordered_admits.append(v)
plt.plot(ordered_admits, '-o')
plt.title('Number of admitted patients $y$ on a day $x$')
plt.xticks(range(len(day_admit)), sorted(day_admit.keys()), rotation = 90)
plt.show()


# In[8]:

days = data.DaysStay
plt.hist(days, bins=max(days))
plt.title("Total number of patients $y$ that stay $x$ days");plt.show()
plt.hist(days, bins=max(days), normed=True)
plt.title("The prob. density $y$ that a patient stays $x$ days");plt.show()

print("notice the mean of the distribution is approximately = 2, which was originally used in poisson.rvs(mu=2, size=1) to generate the random length of stay in the dataset.")


# **example**

# In[14]:

l = len(data[data.DaysStay == 1])
print('{} patients stayed for 1 day during the time interval March through April of 2015.'.format(l))


# ### Poisson Distribution

# In[20]:

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import matplotlib as mtlp


# In[34]:

set(days)


# In[39]:

day


# In[65]:

n, bins, patches, = plt.hist(days);plt.show()


# In[66]:




# In[68]:

plt.figure(figsize=(8,4))

day = np.arange(len(set(days)))
len_stay = list(set(days))[:7]

colors = matplotlib.rcParams['axes.color_cycle']
for i, lambda_ in enumerate(len_stay):

    ppmf = poisson.pmf(day, lambda_)
    l = "stay {} day(s)".format(lambda_)

    plt.plot(day, ppmf, '-o', label=l, color=colors[i])
    plt.fill_between(day, ppmf, color=colors[i], alpha=0.5)
    plt.legend()

plt.title("Poisson distribution of the patients dataset");plt.ylabel("pmf at $k$");plt.xlabel("$k$")
plt.legend(bbox_to_anchor = (1.5, 1));plt.show();


# In[47]:

n


# In[35]:

plt.figure(figsize=(8,4))

day = np.arange(15)
len_stay = list(days[:5])

colors = matplotlib.rcParams['axes.color_cycle']

for i, lambda_ in enumerate(len_stay):

    ppmf = poisson.pmf(day, lambda_)
    l = "stay {} day(s)".format(lambda_)

    plt.plot(day, ppmf, '-o', label=l, color=colors[i])
    plt.fill_between(day, ppmf, color=colors[i], alpha=0.5)
    plt.legend()

plt.title("Poisson distribution");plt.ylabel("pmf at $k$");plt.xlabel("Number of stay days $k$")
plt.legend(bbox_to_anchor = (1.5, 1));plt.show();


# In[32]:

day = np.arange(15)

len_stay = [10, 4, 6, 12]

colors = matplotlib.rcParams['axes.color_cycle']

for i, lambda_ in enumerate(len_stay):
    ppmf = poisson.pmf(day, lambda_)

    plt.plot(day, ppmf, '-o', label=lambda_, color=colors[i])
    plt.fill_between(day, ppmf, color=colors[i], alpha=0.5)
    plt.legend()

plt.title("Poisson distribution");plt.ylabel("pmf at $k$");plt.xlabel("Number of patients $k$");plt.show();# plt.figure(figsize=(8,4))


# In[14]:

k = np.arange(20)
colors = matplotlib.rcParams['axes.color_cycle']
plt.figure(figsize=(12,8))
for i, lambda_ in enumerate([1, 4, 6, 12]):
    plt.bar(k, poisson.pmf(k, lambda_), label=lambda_, color=colors[i], alpha=0.4, edgecolor=colors[i], lw=3)
    plt.legend()
plt.title("Poisson distribution")
plt.xlabel("$k$")
plt.ylabel("PDF at k")
plt.show()


# In[10]:

# http://nbviewer.ipython.org/urls/gist.github.com/mattions/6113437/raw/c5468ea930d6960225d83e112d7f3d00d9c13398/Exploring+different+distribution.ipynb
k = np.arange(20)
plt.figure(figsize=(8,4))
for i, lambda_ in enumerate([1, 4, 6, 12]):
    plt.bar(k, poisson.pmf(k, lambda_), label=lambda_, color=colors[i], alpha=0.4, edgecolor=colors[i], lw=3)
    plt.legend()

plt.title("Poisson distribution");plt.xlabel("$k$");plt.ylabel("PDF at k")


# In[ ]:




# In[11]:

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import matplotlib as mtlp


# In[134]:

dates = data.AdmitDay
print(dates[0])
data.AdmitDay


# In[142]:

# http://nbviewer.ipython.org/urls/gist.github.com/mattions/6113437/raw/c5468ea930d6960225d83e112d7f3d00d9c13398/Exploring+different+distribution.ipynb
import matplotlib
k = np.arange(20)
colors = matplotlib.rcParams['axes.color_cycle']
plt.figure(figsize=(12,8))
for i, lambda_ in enumerate([1, 4, 6, 12]):
    plt.bar(k, poisson.pmf(k, lambda_), label=lambda_, color=colors[i], alpha=0.4, edgecolor=colors[i], lw=3)
    plt.legend()
plt.title("Poisson distribution")
plt.xlabel("$k$")
plt.ylabel("PDF at k")


# > http://stackoverflow.com/questions/21423158/how-do-i-change-the-range-of-the-x-axis-with-datetimes-in-matplotlib

# ### Patients queue and response time

# 1. Create a queue for patients (can be multiple queues).
# 2. Randomly create patients (say requests) and put them in queue
# 3. Set a response time/serve time for every patient.
# 4. If there are high number of requests, response time is less and vice-versa.
# 5. The program must display requests and response time/serve time with randomized rate of increase and decrease of requests (patients).

# In[ ]:




# ## Experimentation lab

# In[101]:

mm, dd, yy = fake.month(), fake.day_of_month(), 2015
admit_date = "-".join([str(i) for i in [mm, dd, yy]])
stay = length_stay()
print admit_date


# In[ ]:

print fake.date


# In[12]:

# generate service time interval, check-in check-out
checkin = fake.date_time_this_month()
checkout =fake.date_time_between(checkin, 'now')
duration = checkout - checkin
stay_hours = duration.seconds / 60 / 60

print checkin
print checkout
print duration.days, "{0:.2f}".format(stay_hours)#, duration


# In[84]:

# http://www.daveoncode.com/2013/05/20/generate-random-dates-in-python-using-datetime-and-random-modules/
from datetime import datetime
import random

mm, dd, yy = random.randint(1, 12), random.randint(1, 28),  random.randint(2014, 2015)
d = datetime(yy, mm, dd)
print d.date()


# <hr>

# ### Poisson Distribution (process)

# In[207]:

# src: http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html#scipy-stats-poisson
from scipy.stats import poisson
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

mu = 0.6
mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')

x = np.arange(poisson.ppf(0.01, mu),
              poisson.ppf(0.99, mu))
ax.plot(x, poisson.pmf(x, mu), 'bo', ms=8, label='poisson pmf')
ax.vlines(x, 0, poisson.pmf(x, mu), colors='b', lw=5, alpha=0.5)

rv = poisson(mu)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,
        label='frozen pmf')
ax.legend(loc='best', frameon=False)
plt.show()


# In[255]:

# generate random lenghts of stay based on the mean
mu = 0.1
poisson.rvs(mu, size=100)


# ### Reference

# faker
# http://www.joke2k.net/faker/
#
# paper (uses poisson distribution): Simple Queuing Theory Tools You Can Use in Healthcare
# http://www.iienet.org/uploadedFiles/SHS_Community/Resources/Simple%20Queuing%20Theory%20Tools%20You%20Can%20Use%20In%20Healthcare.pdf
#
# time series analysis http://nbviewer.ipython.org/github/changhiskhan/talks/blob/master/pydata2012/pandas_timeseries.ipynb
#
# time series analysis with statsmodel
# http://conference.scipy.org/scipy2011/slides/mckinney_time_series.pdf
