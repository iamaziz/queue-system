
import pandas as pd

data = pd.read_csv('per-patient-data.csv')

def icroom_percentage():
    n = len(data[data.ICRoom == 'yes'])
    percent = float(n) / len(data) * 100
    return percent

def avg_stay():
    avg = float(sum(data.DaysStay)) / len(data)
    return avg

def explore_patients_dataset():
    print("{} patients were admitted.".format(len(data)))
    print("{:.2f}% admitted into IC Rooms (total {})".format(icroom_percentage(), len(data[data.ICRoom == 'yes'])))
    print("{:.2f} day(s) is the average stay of a patient.".format(avg_stay()))

explore_patients_dataset()