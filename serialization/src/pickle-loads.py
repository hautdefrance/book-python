import pickle

FILENAME = 'filename.pkl'

data = pickle.loads(FILENAME)
print(f'Restored object: {data}')

jose = data[0]
print(f'My name... {jose.name}')
