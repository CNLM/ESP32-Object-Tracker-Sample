import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [12, 5]
#plt.rcParams["figure.autolayout"] = True
headers = ['Time', 'P_X', 'P_Y']
df = pd.read_csv('Data_csv\Position.csv', names=headers)
df = df.iloc[2: , :]
df.set_index('Time').plot()
plt.savefig("PNGs\Pos.png")
plt.figure(1)
headers = ['Time', 'V_X', 'V_Y']
df = pd.read_csv('Data_csv\Velocity.csv', names=headers)
df = df.iloc[2: , :]
df.set_index('Time').plot()
plt.ylim(-100,100)
plt.savefig("PNGs\Velo.png")
plt.figure(2)
headers = ['Time', 'A_X', 'A_Y']
df = pd.read_csv('Data_csv\Acceleration.csv', names=headers)
df = df.iloc[2: , :]
df.set_index('Time').plot()
plt.ylim(-20,20)

plt.savefig("PNGs\Accel.png")
plt.show()