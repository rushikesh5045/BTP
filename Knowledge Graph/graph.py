


import re
import networkx as nx
import matplotlib.pyplot as plt

def extract_symptoms_and_treatments(text):
    symptoms = re.findall(r'(?<=symptomatic )[\w\s-]+', text)
    treatments = re.findall(r'(?<=treated )[\w\s-]+', text)
    return symptoms, treatments


with open("output1.txt", 'r') as f:
    conversations = f.readlines()


patient_conversation = conversations[0]  
G = nx.Graph()


symptoms, treatments = extract_symptoms_and_treatments(patient_conversation)


patient_node = f"Patient_0"  
G.add_node(patient_node, label="Patient")

for symptom in symptoms:
    G.add_node(symptom, label="Symptom")
    G.add_edge(patient_node, symptom, relationship="HAS_SYMPTOMS")

for treatment in treatments:
    G.add_node(treatment, label="Treatment")
    G.add_edge(patient_node, treatment, relationship="HAS_TREATMENT") 
pos = nx.spring_layout(G, seed=42)  
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=2000, node_color='lightblue', font_size=10)
edge_labels = {(u, v): d["relationship"] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
