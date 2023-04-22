import pickle
import numpy as np 


#load the model 
best_model = pickle.load(open('modelnn.pkl', 'rb'))

# # Make predictions on new data
#['WBC', 'RBC', 'HGB', 'Plat', 'ALT 12','ALT 24']
X_new = np.array([[]]) # assume X_new has shape (n_samples, n_features)
    
predictions = best_model.predict(X_new)

# Print the predicted labels
predicted_labels = np.argmax(predictions, axis=1)
print(predicted_labels)