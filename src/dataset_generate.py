
from scipy.stats import poisson
from random import randint
import datetime
import sys


# features confiuration

count = 1000
def patient_name():
    global count
    pid = ''.join(['NYC',str(count)])
    count += 1
    return pid

try:
    start_month = int(sys.argv[3])
    end_month = int(sys.argv[4])
except:
    start_month = 1
    end_month = 2


def admission_date():
    mm, dd, yy = randint(start_month, end_month), randint(1, 28), randint(2015, 2015)
    d = datetime.datetime(yy, mm, dd)
    return d.date()


def leave_date(indate, stay):
    dout = indate + datetime.timedelta(days=stay)
    return dout


def rand_pois(mu=2):
    r = poisson.rvs(mu, size=1)[0] # random lenght based on an arbitrary mean
    return r


try:
    avg_stay = int(sys.argv[1])
except:
    avg_stay = 2
    
def patient_log():

    stay = rand_pois(mu=avg_stay) # an arbitrary mean of how long a patient stays at hospital
    ic = rand_pois(mu=0.1)        # approximately! assuming ~10% of patients go into IC rooms
    if ic > 0: ic_room = 'yes'
    else: ic_room = 'no'

    patient_id = patient_name()
    admit_day = admission_date()
    leave_day = leave_date(admit_day, stay)

    return [patient_id, admit_day, stay, leave_day, ic_room]


# generate feature samples and write them into a csv file

import csv

try:
    NUM_PATIENTS = int(sys.argv[2])
except:
    NUM_PATIENTS = 3000


def generate_patients_dataset():

    output_file = 'patients-data.csv'
    with open(output_file, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['PatientID', 'AdmitDay', 'DaysStay', 'LeaveDay', 'ICRoom'])
        for i in range(NUM_PATIENTS):
            spamwriter.writerow(patient_log())
    print('generated patients dataset and wrote output into: \n\t{}'.format('patients-data.csv'))


generate_patients_dataset()