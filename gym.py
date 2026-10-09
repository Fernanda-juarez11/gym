mport mysql.connector


conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="gimnasio"
)


def Create():
    if conexion.is_connected():
        cursor = conexion.cursor()
        clientName = input("Enter client name: ")
        age = int(input("Enter client age: "))
        membershipType = input(
            "Enter membership type (Basic, Premium, VIP): "
        )
        months = int(input("Enter number of months: "))
        if membershipType == "Basic":
            finalPrice = 100 * months
        elif membershipType == "Premium":
            finalPrice = 175 * months
        elif membershipType == "VIP":
            finalPrice = 250 * months
        else:
            print("Invalid membership type.")
            return
        if months >= 6:
            status = "ActivePlus"
        else:
            status = "Active"

        query = """INSERT INTO inscripciones(clientName, age, membershipType, months,finalPrice, status)VALUES (%s, %s, %s, %s, %s, %s)"""
        values = (
            clientName, age, membershipType,
            months, finalPrice, status
        )
        cursor.execute(query, values)
        conexion.commit()
        print("Membership registered successfully.")
        print("Final price: Q", finalPrice)
        print("Status:", status)


def Read():
    if conexion.is_connected():
        cursor = conexion.cursor()
        query = "SELECT * FROM inscripciones"
        cursor.execute(query)
        results = cursor.fetchall()
        for client in results:
            print(client)


def Update():
    if conexion.is_connected():
        cursor = conexion.cursor()
        id = int(input("Enter client ID to update: "))
        clientName = input("Enter client name: ")
        age = int(input("Enter client age: "))
        membershipType = input(
            "Enter membership type (Basic, Premium, VIP): "
        )
        months = int(input("Enter number of months: "))
        if membershipType == "Basic":
            finalPrice = 100 * months
        elif membershipType == "Premium":
            finalPrice = 175 * months
        elif membershipType == "VIP":
            finalPrice = 250 * months
        else:
            print("Invalid membership type.")
            return
        if months >= 6:
            status = "ActivePlus"
        else:
            status = "Active"
        query = """
        UPDATE inscripciones
        SET clientName = %s,
            age = %s,
            membershipType = %s,
            months = %s,
            finalPrice = %s,
            status = %s
        WHERE id = %s
        """
        values = (
            clientName, age, membershipType,
            months, finalPrice, status, id
        )
        cursor.execute(query, values)
        conexion.commit()
        if cursor.rowcount > 0:
            print("Membership updated successfully.")
            print("Final price: Q", finalPrice)
            print("Status:", status)
        else:
            print("Client ID not found.")


def Delete():
    if conexion.is_connected():
        cursor = conexion.cursor()
        id = int(input("Enter client ID to delete: "))
        query = "DELETE FROM inscripciones WHERE id = %s"
        cursor.execute(query, (id,))
        conexion.commit()
        if cursor.rowcount > 0:
            print("Membership deleted successfully.")
        else:
            print("Client ID not found.")


def menu():
    while True:
        print("\n--- GYM MEMBERSHIP SYSTEM ---")
        print("1. Create Membership")
        print("2. Read Memberships")
        print("3. Update Membership")
        print("4. Delete Membership")
        try:
            option = int(input("Choose an option: "))
            if option == 1:
                Create()
            elif option == 2:
                Read()
            elif option == 3:
                Update()
            elif option == 4:
                Delete()
            else:
                print("Invalid option.")
        except ValueError:
            print("Please enter a valid number.")


menu()