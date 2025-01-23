import mysql.connector

# Connexion à la base de données MySQL
db = mysql.connector.connect(
    host="localhost",
    user="vegeta",        
    password="azerty",    
    database="resto"     
)

cursor = db.cursor()

# Suppression des données dans les tables
def delete_data():
    # Supprimer d'abord les clés étrangères
    cursor.execute("DELETE FROM COMPREND_MENU")
    cursor.execute("DELETE FROM CONTIENT_BOISSON")
    cursor.execute("DELETE FROM CONTIENT_PLAT")
    cursor.execute("DELETE FROM AVIS")
    
    cursor.execute("DELETE FROM COMMANDE")
    cursor.execute("DELETE FROM MENU")
    cursor.execute("DELETE FROM PLAT")
    cursor.execute("DELETE FROM BOISSON")
    cursor.execute("DELETE FROM CLIENT")
    
    db.commit()
    print("Les données ont été supprimées de toutes les tables.")

# Exécution de la suppression des données
delete_data()

# Fermeture de la connexion
cursor.close()
db.close()
