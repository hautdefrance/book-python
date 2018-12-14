import pickle


data = pickle.loads('filename.pkl')
print(f'Restored object: {data}')

jose = data[0]
print(f'My name... {jose.name}')
