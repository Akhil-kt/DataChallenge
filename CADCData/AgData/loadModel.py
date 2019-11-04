import cPickle as pickle


model = pickle.load(open('model.sav', 'rb'))

print(model.best_params_)