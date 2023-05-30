import requests
from bs4 import BeautifulSoup
import json
import random
import sys


#Pour faire un nb de range aléatoire
random_range = int(random.choice('3456'))


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
cookie = response.cookies


html_content = response.text

# Utiliser BeautifulSoup pour analyser le contenu HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Trouver tous les éléments de formulaire
form_elements = soup.find_all('input')

#BULK card generator
card = [
	{
		"issuer": "VISA",
		"cardNumber": "4485350330958237",
		"expiryMonth": "05",
		"expiryYear": "2027",
		"exp": "05/2027",
		"cvv": 957,
		"name": "Cheyenne Aufderhar",
		"address": "888 Tessie Lakes",
		"country": "Venezuela",
		"zipcode": "70443"
	},
	{
		"issuer": "VISA",
		"cardNumber": "4485114972132893",
		"expiryMonth": "02",
		"expiryYear": "2027",
		"exp": "02/2027",
		"cvv": 902,
		"name": "Arlene Durgan",
		"address": "35802 Schmeler Branch",
		"country": "Isle of Man",
		"zipcode": "98641"
	},
	{
		"issuer": "VISA",
		"cardNumber": "4556037183150418",
		"expiryMonth": "07",
		"expiryYear": "2024",
		"exp": "07/2024",
		"cvv": 366,
		"name": "Judd Donnelly",
		"address": "9883 Lockman Port",
		"country": "Mauritius",
		"zipcode": "94392-1588"
	},
	{
		"issuer": "VISA",
		"cardNumber": "4444972751693116",
		"expiryMonth": "06",
		"expiryYear": "2025",
		"exp": "06/2025",
		"cvv": 537,
		"name": "Brandi Ullrich",
		"address": "898 Cartwright View",
		"country": "France",
		"zipcode": "52062"
	},
	{
		"issuer": "VISA",
		"cardNumber": "4539407219630646",
		"expiryMonth": "12",
		"expiryYear": "2026",
		"exp": "12/2026",
		"cvv": 371,
		"name": "Valentin Legros",
		"address": "117 Schinner Forges",
		"country": "Cote d'Ivoire",
		"zipcode": "78725-9357"
	},
	{
		"issuer": "VISA",
		"cardNumber": "4024007166396308",
		"expiryMonth": "03",
		"expiryYear": "2023",
		"exp": "03/2023",
		"cvv": 620,
		"name": "Archibald Orn",
		"address": "1232 Ratke Dale",
		"country": "South Africa",
		"zipcode": "32597"
	},
	{
		"issuer": "VISA",
		"cardNumber": "4485147678620589",
		"expiryMonth": "05",
		"expiryYear": "2026",
		"exp": "05/2026",
		"cvv": 173,
		"name": "Ambrose Howe",
		"address": "049 Golden Ferry",
		"country": "Syrian Arab Republic",
		"zipcode": "19970-3893"
	},
	{
		"issuer": "VISA",
		"cardNumber": "4532371480144553",
		"expiryMonth": "12",
		"expiryYear": "2023",
		"exp": "12/2023",
		"cvv": 962,
		"name": "Earnestine Runolfsson",
		"address": "946 Raynor Radial",
		"country": "Montserrat",
		"zipcode": "78754"
	},
	{
		"issuer": "VISA",
		"cardNumber": "4190542866445508",
		"expiryMonth": "01",
		"expiryYear": "2027",
		"exp": "01/2027",
		"cvv": 237,
		"name": "Hermina Greenfelder",
		"address": "43724 White Grove",
		"country": "Mexico",
		"zipcode": "58115"
	},
	{
		"issuer": "VISA",
		"cardNumber": "4084408522135579",
		"expiryMonth": "11",
		"expiryYear": "2028",
		"exp": "11/2028",
		"cvv": 725,
		"name": "Ciara Boyer",
		"address": "7540 Chance Summit",
		"country": "Uzbekistan",
		"zipcode": "76681-3304"
	},
	{
		"issuer": "VISA",
		"cardNumber": "4485619498744518",
		"expiryMonth": "04",
		"expiryYear": "2027",
		"exp": "04/2027",
		"cvv": 899,
		"name": "Monserrate Hermann",
		"address": "3463 Goodwin Cape",
		"country": "Anguilla",
		"zipcode": "12747-5147"
	},
	{
		"issuer": "VISA",
		"cardNumber": "4024007154431406",
		"expiryMonth": "02",
		"expiryYear": "2024",
		"exp": "02/2024",
		"cvv": 610,
		"name": "Moshe Kassulke",
		"address": "2324 Leffler Pass",
		"country": "Guinea",
		"zipcode": "86707"
	},
	{
		"issuer": "VISA",
		"cardNumber": "4024007133745546",
		"expiryMonth": "12",
		"expiryYear": "2027",
		"exp": "12/2027",
		"cvv": 942,
		"name": "Edwina Cummings",
		"address": "652 Jast Trail",
		"country": "French Southern Territories",
		"zipcode": "22410"
	},
	{
		"issuer": "MasterCard",
		"cardNumber": "5538734143800377",
		"expiryMonth": "10",
		"expiryYear": "2024",
		"exp": "10/2024",
		"cvv": 862,
		"name": "Buck Bode",
		"address": "85313 Bogisich Terrace",
		"country": "New Zealand",
		"zipcode": "41650-5705"
	},
	{
		"issuer": "MasterCard",
		"cardNumber": "5323081449257061",
		"expiryMonth": "04",
		"expiryYear": "2026",
		"exp": "04/2026",
		"cvv": 692,
		"name": "Clint Rodriguez",
		"address": "021 Rice Crescent",
		"country": "Slovakia (Slovak Republic)",
		"zipcode": "39236"
	},
	{
		"issuer": "MasterCard",
		"cardNumber": "5516007756450871",
		"expiryMonth": "10",
		"expiryYear": "2025",
		"exp": "10/2025",
		"cvv": 807,
		"name": "Merlin Bergnaum",
		"address": "21012 Lind Walks",
		"country": "Antigua and Barbuda",
		"zipcode": "68898"
	},
	{
		"issuer": "MasterCard",
		"cardNumber": "5326402203055417",
		"expiryMonth": "07",
		"expiryYear": "2028",
		"exp": "07/2028",
		"cvv": 740,
		"name": "Cyrus Crist",
		"address": "87274 Spencer Bridge",
		"country": "Pitcairn Islands",
		"zipcode": "42590"
	},
	{
		"issuer": "MasterCard",
		"cardNumber": "5327798211914431",
		"expiryMonth": "06",
		"expiryYear": "2026",
		"exp": "06/2026",
		"cvv": 757,
		"name": "Jayme Thiel",
		"address": "7737 Kiehn Club",
		"country": "Guinea-Bissau",
		"zipcode": "67156"
	},
	{
		"issuer": "MasterCard",
		"cardNumber": "5203517920711824",
		"expiryMonth": "09",
		"expiryYear": "2023",
		"exp": "09/2023",
		"cvv": 989,
		"name": "Modesta Schneider",
		"address": "31434 Reichert Ranch",
		"country": "Libyan Arab Jamahiriya",
		"zipcode": "75492"
	},
	{
		"issuer": "MasterCard",
		"cardNumber": "2221722425106448",
		"expiryMonth": "06",
		"expiryYear": "2025",
		"exp": "06/2025",
		"cvv": 724,
		"name": "Bertha Fahey",
		"address": "845 Bessie Glens",
		"country": "Liberia",
		"zipcode": "08304"
	}
]

def generate_random_data():
    global last_name, first_name, phone_number, address, zip_code, city, email, password, bd_day, bd_month, bd_year

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

    days = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

    month = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

    years = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]
    
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
    email = first_name + ''.join(random.choice('0123456789') for _ in range(random_range)) + '@gmail.com'

    #Généré le password
    password = ''.join(random.choice('abcdefghijklmnopqrstwxyz0123456789!?.;#@-/') for _ in range(8))

    bd_day = random.choice(days)
    bd_month = random.choice(month)
    bd_year = random.choice(years)

    #Carding shit
    global card, exp, CCV, total_name
    data = json.load(card)
    choice = random.choice(data)

    card = choice['cardNumber']
    exp = choice['exp']
    CCV = choice['cvv']
    total_name = first_name + last_name



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
    elif field_name == 'card.number':
        field_value == card
    elif field_name == 'card.cvv':
        field_value == CCV
    elif field_name == 'card.exp':
        field_value == exp
    elif field_name == 'bd_day':
        field_value == bd_day
    elif field_name == 'bd_month':
        field_value == bd_month
    elif field_name == 'bd_year':
        field_value == bd_year


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
    response = requests.post(url_test, data=data_dict, cookies=cookie)
