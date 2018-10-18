from datetime import datetime
import matplotlib.pyplot as plt


def temp_plot(dates, mean_temps):
    year_start = datetime(2012, 1, 1)
    days = [(d - year_start).days + 1 for d in dates]

    fig = plt.figure()
    plt.title('Temperatures in Bloomington 2012')
    plt.ylabel('Mean Temperature (F)')
    plt.xlabel('Day of Year')

    plt.plot(days, mean_temps, marker='o')

    return fig


data = read_weather('data/weather.csv')

min_temps = data['min temp']
mean_temps = data['mean temp']
max_temps = data['max temp']
dates = [datetime.fromordinal(d) for d in data['timestamp']]
events = data['events']

if not os.path.exists('plots'):
    os.mkdir('plots')

fig = temp_plot(dates, mean_temps)
fig.savefig('plots/day_vs_temp.png')
