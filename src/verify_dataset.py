
import pandas as pd

data = pd.read_csv('patients-data.csv')

def icroom_percentage():
    n = len(data[data.ICRoom == 'yes'])
    percent = float(n) / len(data) * 100
    return percent

def avg_stay():
    avg = float(sum(data.DaysStay)) / len(data)
    return avg

def explore_patients_dataset():
    print("{} patients were admitted between March/April 2015".format(len(data)))
    print("{}% admitted into IC Rooms ({})".format(icroom_percentage(), len(data[data.ICRoom == 'yes'])))
    print("{} day(s) is the average stay of a patient".format(avg_stay()))
    return data

explore_patients_dataset()