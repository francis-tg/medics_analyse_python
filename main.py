import pandas as pd

# Charger les données depuis le fichier Excel
df = pd.read_excel("medecin.xlsx")

# Créer une fonction pour proposer les maladies associées à une liste de symptômes
def proposer_maladies(symptomes):
    maladies_proposees = df[df['Symptomes'].apply(lambda x: isinstance(x, str) and all(symptome in x.split(', ') for symptome in symptomes))]
    return maladies_proposees

# Liste de symptômes d'exemple
symptomes_exemple = ['frissons','fatigue']

# Obtenir les maladies associées à la liste de symptômes
maladies_associees = proposer_maladies(symptomes_exemple)
print("Maladies associées : ")
print(maladies_associees['Maladie'])

# Extraire les médecins intervenant pour ces maladies
medecins_intervenant = maladies_associees['Medecin'].unique()
print("Médecins intervenant : ")
print(medecins_intervenant)
