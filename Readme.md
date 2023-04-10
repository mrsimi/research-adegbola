Setup 
1. Ensure you have python installed. If not download and install
2. Install pickle and numpy using this code `pip3 install pickle numpy` or `pip install pickle numpy`


Running Modelone.py
Edit the values in the sample data variable here 
```
if __name__ == "__main__":
    #['DAYS', 'CREATININE', 'UREA', 'ALT', 'AST', 'GGT', 'BW', 'LWR', 'KWR']
    sample_data = [[1.80000000e+02, 6.51205160e+01, 1.50274062e+01, 2.17060620e+02, 7.42701200e+01, 4.86187118e+01, 1.02710000e+02, 1.74241280e-02, 6.09756098e-03]]
    prediction = predict(sample_data)

    print(prediction) 
                    
```
Then type 
```
python3 modelone.py in the commond prompt/terminal 
```
with the data as label. The result comes out like this 

```
[45.59723077]
```

The result is the prediction of the sample data. The higher the value the more likely they are diseased. 