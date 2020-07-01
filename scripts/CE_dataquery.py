#!/usr/bin/env python
import pandas as pd
import numpy as np
import os
import json


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    CYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


print('-' * 45)
print('|' + ' ' * 43 +'|')
print('|' + 'Cluster expanstion data collector'.center(43,' ') +'|')
print('|' + 'made by mjhong'.center(43,' ') +'|')
print('|' + ' ' * 43 +'|')
print('-' * 45)

fileList = os.listdir()

try:
    if 'eci.json' not in fileList:
        raise Exception(bcolors.WARNING + 'No eci.json file found. ' + bcolors.ENDC)
    
    fittedData = input('Enter the path of fitted data file(.json) : ')
    os.system('casm query -k corr -j --output corr.json')
    print('Correlation matrix wriiten to ' + bcolors.CYAN + 'corr.json' + bcolors.ENDC + '.')
    
    os.system("casm query -c CALCULATED -k 'comp formation_energy hull_dist(CALCULATED)' -j --output energyhull_calculated.json")
    print('Energy hull by DFT written to ' + bcolors.CYAN + 'energyhull_calculated.json' + bcolors.ENDC + '.')
    
    energyHull = pd.read_json('energyhull_calculated.json')
    energyHull['comp'] = [comp[0][0] for comp in energyHull['comp']]
    energyHull.columns = ['comp', 'configname', 'formationE_DFT(eV)', 'hull_dist', 'selected'] 
    energyHull = energyHull[['configname','comp',  'selected', 'formationE_DFT(eV)', ]]
    
    with open('eci.json') as file:
        eci_json = json.load(file)
        eci_index = np.array(eci_json['fit']['eci'])[:,0].astype('int64')
        eci_values = np.array(eci_json['fit']['eci'])[:,1]
    
    with open('corr.json') as file:
        corr_json = json.load(file)
    
    correlationMatrix = [np.array(c['corr'])[:,0][eci_index] for c in corr_json]
    energyHull['formationE_CE(eV)']  = list(np.dot(correlationMatrix, eci_values))
    energyHull.to_csv('energyHull.csv')
    print(bcolors.BOLD + bcolors.OKGREEN +  'Energy Hull calculation complete!' + bcolors.ENDC)
    print(energyHull)

except Exception:
    print(bcolors.WARNING + 'Job not complete : No eci.json file.' + bcolors.ENDC)





