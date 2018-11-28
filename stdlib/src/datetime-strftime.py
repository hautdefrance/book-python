from datetime import datetime


gagarin = datetime(1961, 4, 12)
formatted = gagarin.strftime('%Y-%m-%d %H:%M')


print(f'Gagarin launched on {formatted}')
# Gagarin launched on 1961-04-12 06:07
