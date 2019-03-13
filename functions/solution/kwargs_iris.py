def print_iris(sepal_length, sepal_width, *args, **kwargs):
    print(locals())


with open(r'../data/iris.csv') as file:
    for line in file:
        # 4.9,3.1,1.5,0.1,setosa
        # features = ['4.9', '3.1', '1.5', '0.1']
        # labels = 'setosa'
        *features, labels = line.strip().split(',')
        labels = {'species': labels}

        print_iris(*features, **labels)
