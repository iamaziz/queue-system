
# coding: utf-8

# **generate fake data**

# In[1]:

get_ipython().magic(u'lsmagic')


# In[3]:

from faker import Factory
fake = Factory.create()


# In[4]:

from random import randint
def response_time():
    """return """
    seconds = randint(60, 1200)
    return seconds / 60

def is_hospitalized(duration):
    # estimated threshold for hospitalizing a patients
    threshold = 43200 # seconds = 12 hours
    
    if duration.total_seconds() >= threshold:
        return '1'
    else:
        return '0'
        
def patient_log():
    name = fake.name()
    dob = fake.year()
    age = 2015 - int(dob)
    checkin = fake.date_time_this_month()
    checkout = fake.date_time_between(checkin, 'now')
    stay = checkout - checkin
    stay_hours = stay.total_seconds() / 60 / 60
    hospitalized = is_hospitalized(stay)
    response = response_time()
    return [name, age, str(checkin), str(checkout), response, stay.days, "{0:.1f}".format(stay_hours), hospitalized]
# patient_log()


# In[5]:

# write patients data to csv
NUM_PATIENTS = 10

import csv
with open('patients-data.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['name', 'age', 'check-in', 'check-out', 'response-time-mins', 'stay-days', 'stay-hours', 'hospitalized?'])
    for i in range(NUM_PATIENTS):
        spamwriter.writerow(patient_log())


# In[6]:

# validate data consistency
import pandas as pd
data = pd.read_csv('patients-data.csv')
data


# In[61]:

import matplotlib.pyplot as plt
import datetime
import calendar


# In[64]:

get_ipython().magic(u'pinfo plt.yticks')


# In[63]:

datetime.time


# In[40]:

[hrs,mins,secs = 0,x[0],0
datetime.time(hrs,mins,secs)


# In[62]:

get_ipython().magic(u'matplotlib notebook')
response = [randint(1,20) for _ in range(len(data))]

fig, ax = plt.subplots()

# ax.plot_date(patients, response)
# ax.set_xlim([datetime.date(2014, 1, 26), datetime.date(2014, 2, 1)])
plt.yticks( range(12), calendar.month_name[1:13], rotation=45 )
plt.xlabel('arrival date');plt.ylabel('response time')
plt.show()


# > http://stackoverflow.com/questions/21423158/how-do-i-change-the-range-of-the-x-axis-with-datetimes-in-matplotlib

# In[47]:

import datetime
import matplotlib.pyplot as plt

x = [datetime.date(2014, 1, 29), datetime.date(2014, 1, 29), datetime.date(2014, 1, 29)] 
y = [2, 4, 1]

fig, ax = plt.subplots()
ax.plot_date(x, y, markerfacecolor='CornflowerBlue', markeredgecolor='white')
fig.autofmt_xdate()
ax.set_xlim([datetime.date(2014, 1, 26), datetime.date(2014, 2, 1)])
ax.set_ylim([datetime.time(7,0,0), datetime.time(23,0,0)])


# ### Patients queue and response time

# 1. Create a queue for patients (can be multiple queues).
# 2. Randomly create patients (say requests) and put them in queue
# 3. Set a response time/serve time for every patient.
# 4. If there are high number of requests, response time is less and vice-versa.
# 5. The program must display requests and response time/serve time with randomized rate of increase and decrease of requests (patients).

# In[ ]:




# ## Experimentation lab

# In[12]:

# generate service time interval, check-in check-out
checkin = fake.date_time_this_month()
checkout =fake.date_time_between(checkin, 'now')
duration = checkout - checkin
stay_hours = duration.seconds / 60 / 60

print checkin
print checkout
print duration.days, "{0:.2f}".format(stay_hours)#, duration


# <hr>

# ### Reference

# faker 
# http://www.joke2k.net/faker/
# 
# time series analysis http://nbviewer.ipython.org/github/changhiskhan/talks/blob/master/pydata2012/pandas_timeseries.ipynb
# 
# time series analysis with statsmodel 
# http://conference.scipy.org/scipy2011/slides/mckinney_time_series.pdf
