import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='hackernews_st',
            user='hackernews_st',
            password='hackernews_st'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def init_db():
    connection = get_connection()
    if connection is None:
        print("Could not establish connection to the database")
        return False
    
    try:
        cursor = connection.cursor()
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS videos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title_art VARCHAR(255) NOT NULL,
            url VARCHAR(500) NOT NULL,
            title_yt VARCHAR(255),
            description_yt TEXT,
            script_yt TEXT,
            cinema_yt TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        
        cursor.execute(create_table_query)
        connection.commit()
        print("Table 'videos' created successfully")
        return True
        
    except Error as e:
        print(f"Error creating table: {e}")
        return False
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def article_exists(title_art):
    connection = get_connection()
    if connection is None:
        return False
    
    try:
        cursor = connection.cursor()
        
        query = "SELECT COUNT(*) FROM videos WHERE title_art = %s"
        cursor.execute(query, (title_art,))
        
        result = cursor.fetchone()
        return result[0] > 0
        
    except Error as e:
        print(f"Error verifying article: {e}")
        return False
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def insert_video(title_art, url, title_yt=None, description_yt=None, script_yt=None, cinema_yt=None):
    connection = get_connection()
    if connection is None:
        return False
    
    try:
        cursor = connection.cursor()
        
        insert_query = """
        INSERT INTO videos (title_art, url, title_yt, description_yt, script_yt, cinema_yt)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        
        cursor.execute(insert_query, (title_art, url, title_yt, description_yt, script_yt, cinema_yt))
        connection.commit()
        print(f"Video '{title_art}' inserted successfully")
        return True
        
    except Error as e:
        print(f"Error inserting video: {e}")
        return False
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    init_db()
