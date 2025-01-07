import psycopg2
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

DB_NAME = "rock_festival_db"
DB_USER = "postgres"
DB_PASSWORD = "my_secure_password"
DB_HOST = "localhost"
DB_PORT = "5433"

CREATE_FESTIVALS_TABLE = """
CREATE TABLE IF NOT EXISTS Festivals (
    FestivalID SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Location VARCHAR(100) NOT NULL,
    Date DATE NOT NULL,
    Organizer VARCHAR(100),
    Format VARCHAR(50)
);
"""

CREATE_ROCKBANDS_TABLE = """
CREATE TABLE IF NOT EXISTS RockBands (
    BandID SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    YearFounded INT,
    Genre VARCHAR(50),
    Producer VARCHAR(100),
    Members VARCHAR(250)
);
"""

CREATE_PERFORMANCES_TABLE = """
CREATE TABLE IF NOT EXISTS Performances (
    PerformanceID SERIAL PRIMARY KEY,
    FestivalID INT NOT NULL,
    BandID INT NOT NULL,
    PerformanceType VARCHAR(100),
    Number INT,
    Duration FLOAT,
    FOREIGN KEY (FestivalID) REFERENCES Festivals(FestivalID) ON DELETE CASCADE,
    FOREIGN KEY (BandID) REFERENCES RockBands(BandID) ON DELETE CASCADE
);
"""

def terminate_connections():
    """Terminate all active connections to the database."""
    conn = psycopg2.connect(
        dbname="postgres",
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    conn.autocommit = True
    cur = conn.cursor()
    try:
        cur.execute(f"""
            SELECT pg_terminate_backend(pg_stat_activity.pid)
            FROM pg_stat_activity
            WHERE pg_stat_activity.datname = '{DB_NAME}'
              AND pid <> pg_backend_pid();
        """)
        logging.info(f"Terminated active connections to database '{DB_NAME}'.")
    except psycopg2.Error as e:
        logging.error(f"Error terminating connections: {e}")
        raise
    finally:
        cur.close()
        conn.close()

def init_db():
    try:
        terminate_connections()

        conn = psycopg2.connect(
            dbname="postgres",
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(f"DROP DATABASE IF EXISTS {DB_NAME};")
        logging.info(f"Database '{DB_NAME}' dropped (if existed).")

        cur.execute(f"CREATE DATABASE {DB_NAME} OWNER {DB_USER};")
        logging.info(f"Database '{DB_NAME}' created with owner '{DB_USER}'.")

        cur.close()
        conn.close()

        conn2 = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn2.autocommit = True
        cur2 = conn2.cursor()

        cur2.execute(CREATE_FESTIVALS_TABLE)
        cur2.execute(CREATE_ROCKBANDS_TABLE)
        cur2.execute(CREATE_PERFORMANCES_TABLE)
        logging.info("Tables created: Festivals, RockBands, Performances.")

        cur2.close()
        conn2.close()

        logging.info("Database initialization completed successfully.")

    except psycopg2.Error as e:
        logging.error(f"Error during database initialization: {e}")
        raise

if __name__ == "__main__":
    init_db()