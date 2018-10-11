import pickle

FILENAME = 'filename.pkl'


with open(FILENAME, 'rb') as file:
    data = pickle.load(file)

print(f'Restored object: {data}')
