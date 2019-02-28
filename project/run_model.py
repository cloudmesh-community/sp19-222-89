from joblib import dump, load
import model


#print(model.labels_testing)
svm_model = load('model.joblib')

anwser = {}
anwser=svm_model.predict(model.features_testing)

for i in range(len(model.labels_testing)):
   print("Prediction vs Answer: ", anwser[i], '|', model.labels_testing[i])