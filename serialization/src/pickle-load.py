import pickle


with open('filename.pkl', mode='rb') as file:
    data = pickle.load(file)

print(f'Restored object: {data}')
