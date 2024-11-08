import sqlite3

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect("vehicle_database.db")
cursor = conn.cursor()
def convert_to_binary(filename):
    with open(filename, 'rb') as file:
        return file.read()
# Create the `registered_vehicles` table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS registered_vehicles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT,
        user_cnic TEXT,
        user_pic BLOB,
        car_number TEXT,
        car_name TEXT
    )
''')

# Optional: Insert some sample data
data = [
    ('Michael Johnson', '34567-8901234-5', convert_to_binary("sahil.jpeg"), 'LMN-2345', 'Ford Focus'),
    ('Emily Davis', '45678-9012345-6', convert_to_binary("Harris.jpeg"), 'JKL-6789', 'Chevrolet Malibu'),
    ('David Brown', '56789-0123456-7', convert_to_binary("sahil.jpeg"), 'OPQ-3456', 'Nissan Altima'),
    ('Sarah Wilson', '67890-1234567-8', convert_to_binary("Harris.jpeg"), 'RST-7890', 'Hyundai Elantra'),
    ('Chris Miller', '78901-2345678-9', convert_to_binary("sahil.jpeg"), 'UVW-4567', 'Kia Optima'),
    ('Amanda Taylor', '89012-3456789-0', convert_to_binary("Harris.jpeg"), 'XYZ-0123', 'Mazda 3'),
    ('James Anderson', '90123-4567890-1', convert_to_binary("sahil.jpeg"), 'DEF-6789', 'Tesla Model 3'),
    ('Emma Thomas', '01234-5678901-2', convert_to_binary("Harris.jpeg"), 'GHI-3456', 'Volkswagen Jetta'),  # Added car number
    ('Olivia Martinez', '23456-7890123-3', convert_to_binary("sahil.jpeg"), 'JKL-1234', 'BMW 3 Series'),
    ('William Lee', '34567-8901234-4', convert_to_binary("Harris.jpeg"), 'MNO-5678', 'Mercedes-Benz C-Class')
]

cursor.executemany('''
    INSERT INTO registered_vehicles (user_name, user_cnic, user_pic, car_number, car_name)
    VALUES (?, ?, ?, ?, ?)
''', data)



# Commit changes and close the connection
conn.commit()
conn.close()
