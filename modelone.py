import pickle
import numpy as np 


#['DAYS', 'CREATININE', 'UREA', 'ALT', 'AST', 'GGT', 'BW', 'LWR', 'KWR']
#sample data = 1.80000000e+02, 6.51205160e+01, 1.50274062e+01, 2.17060620e+02, 7.42701200e+01, 4.86187118e+01, 1.02710000e+02, 1.74241280e-02, 6.09756098e-03

def predict(data):
    #load model 
    pickled_model = pickle.load(open('modelone.pkl', 'rb'))

    arr = []
    for el in data: 
        arr.append([el[0], el[1], el[2], el[3], el[4], el[5],el[6], el[7],el[8]])
    
    x_test = np.array(arr)
    predictions = pickled_model.predict(x_test)
    return predictions


if __name__ == "__main__":
    #['DAYS', 'CREATININE', 'UREA', 'ALT', 'AST', 'GGT', 'BW', 'LWR', 'KWR']
    sample_data = [[1.80000000e+02, 6.51205160e+01, 1.50274062e+01, 2.17060620e+02, 7.42701200e+01, 4.86187118e+01, 1.02710000e+02, 1.74241280e-02, 6.09756098e-03]]
    prediction = predict(sample_data)

    print(prediction) 
                    