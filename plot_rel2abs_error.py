import matplotlib.pyplot as plt
import pandas as pd 
import argparse
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser(description='Plot error graphs for Rel2Abs controller from debug csv file')

parser.add_argument('file',help='relative path to debug file, should be named LogData.csv')
args = parser.parse_args()

dir_path = f"{dir_path}{os.path.sep}"
file_path = f"{dir_path}{args.file}"

pf = pd.read_csv(file_path)

#Or use absolute path i.e:
#pf = pd.read_csv('C:/git/esmini/pyoscx_scenarios/LogData.csv')

plt.figure(1)
plt.plot(pf['Time'], pf['Error'], label ="positional error")
plt.plot(pf['Time'], pf['V_error'], label ="speed error")
plt.title('Prediction Error values over time')
plt.xlabel('Time [s]')
plt.ylabel('State Prediction Error [m or m/s]')
plt.legend()

plt.figure(2)
plt.plot(pf['Pred_Time'], pf['X_pred'], label="Predicted State")
plt.plot(pf['Time'], pf['X_act'], label = "Actual State")
plt.title('Predicted X-States vs Actual X-States')
plt.xlabel('Time [s]')
plt.ylabel('X-position [m]')
plt.legend()

plt.figure(3)
plt.plot(pf['Pred_Time'], pf['V_pred'], label="Predicted State")
plt.plot(pf['Time'], pf['V_act'], label = "Actual State")
plt.title('Predicted Speeds vs Actual Speeds')
plt.xlabel('Time [s]')
plt.ylabel('Speed [m/s]')
plt.legend()

plt.show()