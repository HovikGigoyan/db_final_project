from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random

DB_NAME = "rock_festival_db"
DB_USER = "postgres"
DB_PASSWORD = "my_secure_password"
DB_HOST = "localhost"
DB_PORT = "5433"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

faker = Faker()

NUM_FESTIVALS = 100
NUM_ROCKBANDS = 100
NUM_PERFORMANCES = 100

def populate_festivals(session):
    for _ in range(NUM_FESTIVALS):
        query = text("""
        INSERT INTO Festivals (Name, Location, Date, Organizer, Format)
        VALUES (:name, :location, :date, :organizer, :format)
        """)
        session.execute(
            query,
            {
                "name": f"{faker.word().capitalize()} Festival",
                "location": faker.city(),
                "date": faker.date_this_decade(),
                "organizer": faker.company(),
                "format": random.choice(["Outdoor", "Indoor"]),
            },
        )
    session.commit()
    print(f"{NUM_FESTIVALS} festivals added successfully!")

def populate_rockbands(session):
    for _ in range(NUM_ROCKBANDS):
        query = text("""
        INSERT INTO RockBands (Name, YearFounded, Genre, Producer, Members)
        VALUES (:name, :year_founded, :genre, :producer, :members)
        """)
        session.execute(
            query,
            {
                "name": f"{faker.word().capitalize()} Band",
                "year_founded": random.randint(1970, 2025),
                "genre": random.choice(["Rock", "Metal", "Jazz", "Pop"]),
                "producer": faker.name(),
                "members": ", ".join(faker.first_name() for _ in range(random.randint(3, 6))),
            },
        )
    session.commit()
    print(f"{NUM_ROCKBANDS} rock bands added successfully!")

def populate_performances(session):
    for _ in range(NUM_PERFORMANCES):
        query = text("""
        INSERT INTO Performances (FestivalID, BandID, PerformanceType, Number, Duration)
        VALUES (:festival_id, :band_id, :performance_type, :number, :duration)
        """)
        session.execute(
            query,
            {
                "festival_id": random.randint(1, NUM_FESTIVALS),
                "band_id": random.randint(1, NUM_ROCKBANDS),
                "performance_type": random.choice(["Main Stage", "Side Stage", "Acoustic"]),
                "number": random.randint(1, 10),
                "duration": round(random.uniform(30, 180), 2),
            },
        )
    session.commit()
    print(f"{NUM_PERFORMANCES} performances added successfully!")

def main():
    session = SessionLocal()

    try:
        print("Populating Festivals...")
        populate_festivals(session)

        print("Populating Rock Bands...")
        populate_rockbands(session)

        print("Populating Performances...")
        populate_performances(session)
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    main()