from casteptools.readCastep import *

testfile = "/home/csunix/cp14tejh/PhD/Data/CalculationOutputs/S22/FullData/MBD/85.castep"

opt_atoms = find_optimised_atoms(testfile)
opt_params = find_optimised_params(testfile)
print(opt_atoms)
print(opt_params)

Output()