import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Connexion à la base de données MySQL
db = mysql.connector.connect(
    host="localhost",
    user="vegeta",         # Remplacez par votre nom d'utilisateur MySQL
    password="azerty",     # Remplacez par votre mot de passe MySQL
    database="resto"       # Remplacez par le nom de votre base de données
)

cursor = db.cursor()

@app.route('/')
def index():
    # Récupérer les clients, avis, menus, plats et boissons depuis la base de données
    cursor.execute("SELECT * FROM CLIENT")
    clients = cursor.fetchall()

    cursor.execute("SELECT * FROM AVIS")
    avis = cursor.fetchall()

    cursor.execute("SELECT * FROM MENU")
    menus = cursor.fetchall()

    cursor.execute("SELECT * FROM PLAT")
    plats = cursor.fetchall()

    cursor.execute("SELECT * FROM BOISSON")
    boissons = cursor.fetchall()
    
    cursor.execute("SELECT * FROM COMMANDE")
    commandes = cursor.fetchall()

    return render_template('index.html', clients=clients, avis=avis, menus=menus, plats=plats, boissons=boissons, commandes=commandes)




@app.route('/add_clients', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        nom = request.form['nom']
        adresse = request.form['adresse']
        email = request.form['email']
        reservation = 'reservation' in request.form  # Checkbox

        cursor.execute("""
            INSERT INTO CLIENT (Nom, Adresse, Email, Reservation)
            VALUES (%s, %s, %s, %s)
        """, (nom, adresse, email, reservation))
        db.commit()

        return redirect(url_for('index'))

    return render_template('add_clients.html')

@app.route('/add_commande', methods=['GET', 'POST'])
def add_commande():
    if request.method == 'POST':
        id_client = request.form['id_client']
        date_commande = request.form['date_commande']
        prix = request.form['prix']
        mode_paiement = request.form['mode_paiement']

        cursor.execute("""
            INSERT INTO COMMANDE (ID_Client, Date_Commande, Prix, Mode_Paiement)
            VALUES (%s, %s, %s, %s)
        """, (id_client, date_commande, prix, mode_paiement))
        db.commit()

        return redirect(url_for('index'))

    cursor.execute("SELECT * FROM CLIENT")
    clients = cursor.fetchall()

    return render_template('add_commande.html', clients=clients)




# Route pour ajouter un avis
@app.route('/add_avis', methods=['GET', 'POST'])
def add_avis():
    if request.method == 'POST':
        id_client = request.form['id_client']
        note = request.form['note']
        commentaire = request.form['commentaire']
        date = request.form['date']

        cursor.execute("""
            INSERT INTO AVIS (ID_Client, Note, Commentaire, Date)
            VALUES (%s, %s, %s, %s)
        """, (id_client, note, commentaire, date))
        db.commit()

        return redirect(url_for('index'))

    # Charger les clients pour le choix
    cursor.execute("SELECT * FROM CLIENT")
    clients = cursor.fetchall()

    return render_template('add_avis.html', clients=clients)



# Route pour ajouter un menu
@app.route('/add_menu', methods=['GET', 'POST'])
def add_menu():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom_menu = request.form['nom_menu']
        prix = request.form['prix']
        description = request.form['description']

        # Insérer les données dans la table MENU
        cursor.execute("""
            INSERT INTO MENU (Nom_Menu, Prix, Description)
            VALUES (%s, %s, %s)
        """, (nom_menu, prix, description))
        db.commit()  # Valider les changements

        # Redirection vers la page d'accueil après ajout
        return redirect(url_for('index'))

    # Affichage de la page HTML pour ajouter un menu
    return render_template('add_menu.html')


# Route pour ajouter un plat
@app.route('/add_plat', methods=['GET', 'POST'])
def add_plat():
    if request.method == 'POST':
        nom_plat = request.form['nom_plat']
        prix = request.form['prix']
        Type = request.form['Type']  # récupération du type
        calories = request.form['calories']

        # Insérer les valeurs dans la table PLAT
        cursor.execute("""
            INSERT INTO PLAT (Nom_Plat, Prix, Type, Calories)
            VALUES (%s, %s, %s, %s)
        """, (nom_plat, prix, Type, calories))
        db.commit()

        return redirect(url_for('index'))

    return render_template('add_plat.html')


# Route pour ajouter une boisson
@app.route('/add_boisson', methods=['GET', 'POST'])
def add_boisson():
    if request.method == 'POST':
        nom_boisson = request.form['nom_boisson']
        prix = request.form['prix']
        Type = request.form['Type']  # récupération du type
        calories = request.form['calories']

        # Insérer les valeurs dans la table BOISSON
        cursor.execute("""
            INSERT INTO BOISSON (Nom_Boisson, Prix, Type, Calories)
            VALUES (%s, %s, %s, %s)
        """, (nom_boisson, prix, Type, calories))
        db.commit()

        return redirect(url_for('index'))

    return render_template('add_boisson.html')




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
