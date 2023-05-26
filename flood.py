import requests
from bs4 import BeautifulSoup
import json
import random
import sys


# Vérifier s'il y a au moins un argument
if len(sys.argv) == 1:
    print("[-] Fait comme ça gros bouffon : script.py URL NB_DE_ROUND") 
    exit()
else:
    # Récupérer le premier argument
    url_tmp = sys.argv[1]
    url_tmp = url_tmp.replace('http://', '')
    url_tmp = url_tmp.replace('https://', '')
    url = str('http://' + url_tmp)
    round = int(sys.argv[2])
    
    #url = "http://c.bonification.fr"


    # Afficher la valeur des arguments
    print("[+] URL :", url)
    print(f"[+] Pour {round} rounds")

# Envoyer une requête GET pour récupérer le contenu HTML de la page
response = requests.get(url)
html_content = response.text

# Utiliser BeautifulSoup pour analyser le contenu HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Trouver tous les éléments de formulaire
form_elements = soup.find_all('input')

def generate_random_data():
    global last_name, first_name, phone_number, address, zip_code, city, email, password
    # Liste de noms réalistes
    last_names = [
    'Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor',
    'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson',]

    # Liste de prénoms réalistes
    first_names = [
    'Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia',
    'Harper', 'Evelyn', 'Abigail', 'Emily', 'Elizabeth', 'Mila', 'Ella', 'Avery', 'Sofia', 'Camila',]

    # Liste de villes réalistes
    addresses = [
    '123 Main Street', '456 Elm Avenue', '789 Oak Lane', '10 Pine Court', '234 Maple Drive',
    '567 Cedar Road', '890 Birch Street', '111 Willow Avenue', '222 Spruce Lane', '333 Cherry Court', '129 rue du scam']

# Liste de noms de villes
    cities = [
    'New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Phoenix', 'San Antonio', 'San Diego',
    'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'San Francisco', 'Indianapolis', 'Seattle', 'Denver',
    'Washington', 'Boston', 'Nashville', 'Baltimore', 'Scamville']
    
    # Générer un nom aléatoire
    last_name = random.choice(last_names)

    # Générer un prénom aléatoire
    first_name = random.choice(first_names)

    # Générer un numéro de téléphone aléatoire
    phone_number = ''.join(random.choice('0123456789') for _ in range(10))

    # Générer une adresse aléatoire
    address = random.choice(addresses)

    # Générer un code postal aléatoire
    zip_code = ''.join(random.choice('0123456789') for _ in range(5))

    # Générer une ville aléatoire
    city = random.choice(cities)

    #Générer les emails
    email = first_name + ''.join(random.choice('0123456789azjdieyrgvxlpm') for _ in range(3)) + '@gmail.com'

    #Généré le password
    password = ''.join(random.choice('abcdefghijklmnopqrstwxyz0123456789!?.;#@-/') for _ in range(8))



# Créer un dictionnaire pour stocker les données des champs


def value_gen(field_name):
    global field_value
    if field_name == 'firstname':
        field_value = first_name
    elif field_name == 'lastname':
        field_value = last_name
    elif field_name == 'address':
        field_value = address
    elif field_name == 'zip':
        field_value = zip_code
    elif field_name == 'city':
        field_value = city
    elif field_name == 'email':
        field_value = email
    elif field_name == 'phone':
        field_value = phone_number
    elif field_name == 'acceptterms':
        field_value = '1'
    elif field_name == 'password':
        field_value = password

    else:
        field_value = 'NOTHING'

def generator():
    global data_dict
    data_dict = {}
    # Parcourir les éléments de formulaire et remplir le dictionnaire
    for element in form_elements:
        if 'type' in element.attrs and element['type'] == 'text':
            field_name = element.get('name')

            #Génération des valeurs
            generate_random_data()
            value_gen(field_name)

            data_dict[field_name] = field_value
    data_dict["acceptterms"] = 1



#Envoie de la réponse sur un URL de test
url_test = 'https://eoe0axeop0p9u2n.m.pipedream.net'

#envoie des infos
print(f'[+] Website : {url}')
for _ in range(round):
    generator()

    print(f'[+] Data : {data_dict}\n\n')
    print('[+] Envoi en cours ...')
    response = requests.post(url_test, data=data_dict)
