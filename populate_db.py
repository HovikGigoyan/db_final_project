import requests
from faker import Faker
import random

BASE_URL = "http://127.0.0.1:8001"
faker = Faker()

NUM_FESTIVALS = 10
NUM_ROCKBANDS = 10
NUM_PERFORMANCES = 10

def populate_festivals(num_festivals):
    for _ in range(num_festivals):
        festival = {
            "name": faker.word().capitalize() + " Festival",
            "location": faker.city(),
            "date": faker.date_this_decade().isoformat(),
            "organizer": faker.company(),
            "format": random.choice(["Outdoor", "Indoor"])
        }
        response = requests.post(f"{BASE_URL}/festivals/", json=festival)
        if response.status_code == 200:
            print(f"Festival added: {response.json()}")
        else:
            print(f"Failed to add festival: {response.text}")


def populate_rockbands(num_rockbands):
    for _ in range(num_rockbands):
        rockband = {
            "name": faker.word().capitalize() + " Band",
            "year_founded": random.randint(1970, 2025),
            "genre": random.choice(["Rock", "Metal", "Jazz", "Pop"]),
            "producer": faker.name(),
            "members": ", ".join(faker.first_name() for _ in range(random.randint(3, 6)))
        }
        response = requests.post(f"{BASE_URL}/rockbands/", json=rockband)
        if response.status_code == 200:
            print(f"RockBand added: {response.json()}")
        else:
            print(f"Failed to add rock band: {response.text}")

def populate_performances(num_performances):
    for _ in range(num_performances):
        performance = {
            "festival_id": random.randint(1, NUM_FESTIVALS),
            "band_id": random.randint(1, NUM_ROCKBANDS),
            "performance_type": random.choice(["Main Stage", "Side Stage", "Acoustic"]),
            "number": random.randint(1, 10),
            "duration": round(random.uniform(30, 180), 2)
        }
        response = requests.post(f"{BASE_URL}/performances/", json=performance)
        if response.status_code == 200:
            print(f"Performance added: {response.json()}")
        else:
            print(f"Failed to add performance: {response.text}")

if __name__ == "__main__":
    print("Populating Festivals...")
    populate_festivals(NUM_FESTIVALS)
    print("Populating RockBands...")
    populate_rockbands(NUM_ROCKBANDS)
    print("Populating Performances...")
    populate_performances(NUM_PERFORMANCES)