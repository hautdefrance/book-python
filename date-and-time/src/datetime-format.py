from datetime import datetime


gagarin = datetime(1961, 4, 12, 6, 7)


print(f'Gagarin launched on {gagarin:%Y-%m-%d %H:%M}')
# Gagarin launched on 1961-04-12 06:07
