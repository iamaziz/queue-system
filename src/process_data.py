
import pandas as pd
import matplotlib.pyplot as plt

in_file = 'per-patient-data.csv'

data = pd.DataFrame.from_csv(in_file, index_col=False)

# aggregate raw per-individual patients dataset

def daily_ticks():
    
    days = set( data.AdmitDay )
    total = 0
    icroom = 0
    day_total = {}
    
    for d in sorted(days):
        '''
        total patients per a day = admit + still - leave
        
        return:
            {'day_date': [n_admitted, n_leaving, n_admitted_to_ICU, n_leaving_ICU, total_in_ICU, total_in_hospital]}
        '''
        came = len( data[ data.AdmitDay == d ] )
        left = len( data[ data.LeaveDay == d ] )
        
        total += came
        total -= left

        inicu = len( data[ (data.AdmitDay == d) & (data.ICRoom == 'yes') ] )
        outicu = len( data[ (data.LeaveDay == d) & (data.ICRoom == 'yes') ] )
        
        icroom += inicu
        icroom -= outicu
        
        day_total[d] = [came, left, inicu, outicu, icroom, total]
    
    return day_total

# write the processed data into a csv file

import csv
out_file = 'per-day-data.csv' 
with open(out_file, 'w') as csvfile:
    a = csv.writer(csvfile, delimiter=',')
    a.writerow(['Date', 'InPatients', 'OutPatients', 'InICU', 'OutICU', 'ICUroomTotal', 'OverallTotal'])
    
    entries = daily_ticks()
    
    for k, v in sorted( entries.items() ):
        row = []
        row.append(k)
        
        pin, pout, icuin, icuout, picu, ptotal = v
        row.append(pin)
        row.append(pout)
        row.append(icuin)
        row.append(icuout)
        row.append(picu)
        row.append(ptotal)
        
        a.writerow(row)

print('processed the per-patient dataset:\n\t{}\nand generated the aggregated new dataset into:\n\t{}'.format(in_file, out_file))