import requests
import psycopg2

# Mock database connection details
DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'mydatabase'
DB_USER = 'myuser'
DB_PASSWORD = 'mypassword'

def fetch_data_from_api():
    response = requests.get('https://api.example.com/data')
    data = response.json()
    return data

def transform_data(data):
    # Perform data transformation logic
    transformed_data = []
    for item in data:
        transformed_item = {
            'id': item['id'],
            'name': item['name'],
            # Add additional transformations as needed
        }
        transformed_data.append(transformed_item)
    return transformed_data

def load_data_to_database(data):
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()
    
    # Insert the transformed data into the table
    for item in data:
        insert_query = """
            INSERT INTO mytable (name)
            VALUES (%s)
        """
        cursor.execute(insert_query, (item['name'],))
    
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    # ETL process
    data = fetch_data_from_api()
    transformed_data = transform_data(data)
    load_data_to_database(transformed_data)
