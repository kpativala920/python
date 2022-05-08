import subprocess
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('covid.csv')
print(df)
df.plot(x='Country', y='Confirmed')
df.plot(x='Country', y='Deaths')
plt.figure(figsize=(15, 5))
df = pd.read_csv('covid.csv')
plt.plot(df.Country, df.Confirmed.values)
plt.figure(figsize=(30, 5))
plt.xticks(rotation=90)

df = pd.read_csv('covid.csv')
plt.plot(df.Country, df.Confirmed.values)
plt.plot(df.Country, df.Deaths.values)
plt.figure(figsize=(15, 5))
plt.xticks(rotation=90)
plt.plot(df.Country, df.Confirmed.values, label='Confirmed')
plt.plot(df.Country, df.Deaths.values, label='Deaths')
plt.legend()
plt.xlabel('Country')
plt.ylabel('Confirmed-Death')
plt.title('Confirmed-Deaths CountryWise')

# normal diagram
plt.figure(figsize=(15, 5))
plt.xticks(rotation=90)
plt.plot(df.Country, df.Confirmed.values, label='Confirmed')
plt.plot(df.Country, df.Deaths.values, label='Deaths')
plt.legend()
plt.xlabel('Country')
plt.ylabel('Confirmed-Death')
plt.title('Confirmed-Deaths CountryWise')
plt.ioff()
plt.savefig('img1.png', format='png')

# grid layout diagram
plt.figure(figsize=(15, 5))
plt.xticks(rotation=90)
plt.plot(df.Country, df.Confirmed.values, label='Confirmed')
plt.plot(df.Country, df.Deaths.values, label='Deaths')
plt.legend()
plt.xlabel('Country')
plt.ylabel('Confirmed-Death')
plt.title('Confirmed-Deaths CountryWise')
plt.ioff()
plt.grid()
plt.savefig('img2.png', format='png')

# pattern diagram
plt.figure(figsize=(15, 5))
plt.xticks(rotation=90)
plt.plot(df.Country, df.Confirmed.values, '*--', label='Confirmed', c='r')
plt.plot(df.Country, df.Deaths.values, 'v:', label='Deaths', c='b')
plt.legend()
plt.xlabel('Country')
plt.ylabel('Confirmed-Death')
plt.title('Confirmed-Deaths CountryWise')
plt.ioff()
plt.grid()
plt.savefig('img3.png', format='png')

# death Count
plt.figure(figsize=(15, 5))
plt.xticks(rotation=90)
plt.plot(df.Country, df.Confirmed.values, '--', label='Confirmed', c='g')
plt.plot(df.Country, df.Deaths.values, ':', label='Deaths', c='m')
plt.legend()
plt.xlabel('Country')
plt.ylabel('Confirmed-Death')
plt.title('Confirmed-Deaths CountryWise')
plt.ioff()
plt.grid()
plt.savefig('img4.png', format='png')


subprocess.call("scroll.py", shell=True)