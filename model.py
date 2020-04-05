"""
CO370
Group 37 Project
model.py
"""

from collections import defaultdict
import csv
import gurobipy as gp
from gurobipy import GRB

m = gp.Model("laserables")

# Defining the model
with open("patterns.csv", mode="r") as f:
    f_reader = csv.DictReader(f)
    keys = f_reader.fieldnames
    objective = []

    for row in f_reader:
        # TODO(Chloe): figure out how to translate the
        # written model into code
        print("A row was read")

    m.setObjective(sum(objective), GRB.MINIMIZE)
    m.optimize()


# Write to solution file
with open("solution.csv", mode="w") as sol_f:
    f_writer = csv.writer(sol_f)
    # f_writer.writerow(["u", "v"])
    for v in m.getVars():
        print("A variable was read")
        # TODO(Chloe): figure out the format of how the solution will
        # be written

        # f_writer.writerow(v.varName.split(","))

print('Obj: %g' % m.objVal)