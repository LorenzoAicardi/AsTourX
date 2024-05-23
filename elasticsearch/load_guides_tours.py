import numpy as np
from faker import Faker
from dotenv import load_dotenv
from datetime import datetime
from elasticsearch import Elasticsearch

client = Elasticsearch('http://localhost:9200', verify_certs=False)

client.ssl_context = False
import os
# load_dotenv();

faker = Faker(seed=666)
np.random.seed(666)

keywords = [
    'archeology',
    'museums',
    'music',
    'art',
    'cinema',
    'countryside',
    'tracking',
    'rafting',
    'history',
    'literature',
    'sport',
    'food',
    'wine',
    'beer'
]


def generate_guide():
    guide = {}
    guide['gender'] = np.random.choice(['male', 'female'], size=1).item()
    guide['name'] = (faker.first_name_male() if guide['gender'] == 'male' else faker.first_name_female()) + ' ' + faker.last_name()
    guide['birth_date'] = faker.date_of_birth()
    guide['now_available'] = bool(np.random.binomial(1, 0.3))
    guide['languages_spoken'] = list(np.random.choice(['english', 'italian', 'french', 'spanish', 'deutsche', 'dutch', 'bulgarian', 'chinese'], size=1+np.random.poisson(lam=1, size=1).item(), replace=False))
    guide['price'] = int(max(10, np.abs(np.random.normal(30, 5))))
    guide['education'] = np.random.choice(['elementary', 'high-school', 'bachelor', 'master', 'phd'], size=1).item()
    guide['biography'] = faker.profile()['job']
    guide['keywords'] = list(np.random.choice(keywords, size=np.random.poisson(2, size=1).item()))
    guide['current_location'] = {
        "lat": np.random.normal(40.3524, 0.01),
        "lon": np.random.normal(18.1732, 0.01)
    }

     # Generate previous tours
    guide['previous_tours'] = []
    for _ in range(np.random.poisson(lam=2, size=1).item()):
        tour = {
            "altitude": np.random.uniform(0, 3000),
            "distance": np.random.uniform(1, 50),
            "days": np.random.randint(1, 15),
            "tour_keywords": list(np.random.choice(keywords, size=np.random.poisson(lam=5, size=1).item())),
            "places": []
        }
        # Generate places for each tour
        for _ in range(np.random.poisson(lam=3, size=1).item()):
            place = {
                "name": faker.city(),
                "location": {
                    "lat": np.random.normal(40.3524, 0.01),
                    "lon": np.random.normal(18.1732, 0.01)
                }
            }
            tour['places'].append(place)
        guide['previous_tours'].append(tour)
    
    return guide


N = 200

for i in range(1, N):
    client.index(index='guides_tours', body=generate_guide())
    print(f"Generated {i}/{N} guides")