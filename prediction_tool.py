import pickle
from sklearn.neighbors import KNeighborsClassifier

filename='model.sk'
model=loaded_model = pickle.load(open(filename, 'rb'))
classes={
    0: "Alpha",
    1: "Gamma",
    2: "Beta",
}

#problem features config
problem_features = {
    "network_size": 3,   # <=10 ports: 1 | 11-40 ports: 2 | more than 40 ports: 3
    "network_topology": 1, # simple: 1 | butterfly: 2 | complex: 3
    "objectives": 1, #clear and consistent: 1 | conflicting: 2 
    "constraints": 1, #few & rigid constraints: 1 | many constraints with multiple interdepencies: 2
    "fleet_composition":1, #single type of vessel: 1 | multiple types of vessels: 2
    "degree_of_uncertainty": 0, #None: 0 | Moderate: 1 | high: 2
    "approximability": 1, # Exact: 1 | Faily Approximable: 2 | Poorly approximable: 3
    "service_level_requirements": 0 #None: 0 | Time-transit deadlines: 1
}

#pre-processing the data 
for key in problem_features:
    problem_features[key] =  problem_features[key]+1

params=[[problem_features["network_size"], problem_features["network_topology"], problem_features["objectives"], problem_features["constraints"], problem_features["fleet_composition"], problem_features["degree_of_uncertainty"], problem_features["approximability"], problem_features["service_level_requirements"]]]

#prediction
prediction=model.predict(params)[0]
print(f"Prediction: {classes[prediction]}")