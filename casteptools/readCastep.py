import re
import pandas as pd


def find_optimised_atoms(inpfile):
    atoms = []
    check = False
    atom = re.compile(r'[A-Z]([a-z])?\s*\d*\s*(-)?\d*\.\d*\s*(-)?\d*\.\d*\s*(-)?\d*\.\d*')
    with open(inpfile) as f:
        for line in f:
            if "type of calculation" in line and "geometry optimization" not in line:
                break
            if "Geometry optimization completed successfully" in line:
                check = True
            match = atom.search(line)
            if (match is not None) and (check is True):
                    atoms.append(match.group().split())
            if "Final Enthalpy" in line:
                check = False
    for i in range(len(atoms)):
        atoms[i][1] = str(str(atoms[i][0]) + str(atoms[i][1]))
        for j in range(2, 5):
            atoms[i][j] = float(atoms[i][j])
    if len(atoms) is 0:
        atoms = "This is not a geometry optimisation."
    else:
        atoms = pd.DataFrame(atoms, columns=['Label', 'ID', 'x', 'y', 'z'])
    return atoms


def find_optimised_params(inpfile):
    params = {'a': 0, 'b': 0, 'c': 0, 'alpha': 0, 'beta': 0, 'gamma': 0, 'volume': 0}
    check = False
    fixed_cell = False
    with open(inpfile) as f:
        for line in f:
            if ("alpha =" in line):
                params['a'] = float(line.split()[2])
                params['alpha'] = float(line.split()[5])
            if ("beta  =" in line):
                params['b'] = float(line.split()[2])
                params['beta'] = float(line.split()[5])
            if ("gamma" in line):
                params['c'] = float(line.split()[2])
                params['gamma'] = float(line.split()[5])
            if "cell volume" in line:
                if len(line.split()) is 5:
                    params['volume'] = float(line.split()[3][1:])
                if len(line.split()) is 6:
                    params['volume'] = float(line.split()[4])
            if "Number of cell constraints= 6" in line:
                fixed_cell = True
            if "Geometry optimization completed successfully" in line:
                check = True
            if ("alpha" in line) and (check is True) and (fixed_cell is False):
                params['a'] = float(line.split()[2])
                params['alpha'] = float(line.split()[5])
            if ("beta" in line) and (check is True) and (fixed_cell is False):
                params['b'] = float(line.split()[2])
                params['beta'] = float(line.split()[5])
            if ("gamma" in line) and (check is True) and (fixed_cell is False):
                params['c'] = float(line.split()[2])
                params['gamma'] = float(line.split()[5])
            if "cell volume" in line and (check is True) and (fixed_cell is False):
                print(len(line.split()))
                if len(line.split()) is 5:
                    params['volume'] = float(line.split()[3][1:])
                if len(line.split()) is 6:
                    params['volume'] = float(line.split()[4])
            if 'Cell Contents' in line:
                check = False
    return params


def get_total_energy(inpfile):
    with open(inpfile, 'r') as f:
        for line in f:
            print(line)
