import numpy as np
from faker import Faker
from dotenv import load_dotenv
from datetime import datetime
from elasticsearch import Elasticsearch
import os

load_dotenv()

client = Elasticsearch(os.getenv('HOST'), verify_certs=False)
client.ssl_context = False

# init elasticsearch index with this mapping
# {
#   "mappings": {
#     "properties": {
#       "name": { "type": "text" },
#       "birth_date": { "type": "date" },
#       "now_available": { "type": "boolean" },
#       "gender": { "type": "keyword" },
#       "languages_spoken": { "type": "keyword" },
#       "price": { 
#         "type": "scaled_float",
#         "scaling_factor": 100 
#       },    
#       "education": { "type": "keyword" },
#       "biography": { "type": "text" },
#       "keywords": { "type": "text" },
#       "current_location": { "type": "geo_point" },
#       "previous_tours": { 
#         "type": "nested", 
#         "properties": {
#           "altitude": { "type": "float" },
#           "distance": { "type": "float" },
#           "days": {"type": "short"},
#           "tour_keywords": { "type": "text" },
#           "places": {
#             "type": "nested",
#             "properties": {
#                 "name": { "type": "text"},
#                 "location": { "type": "geo_point"}
#             }
#           }
#         }
#       }
#     }
#   }
# }


client.indices.create(
    index='guides',
    body={
    "mappings": {
        "properties": {
            "name": { "type": "text" },
            "birth_date": { "type": "date" },
            "now_available": { "type": "boolean" },
            "gender": { "type": "keyword" },
            "languages_spoken": { "type": "keyword" },
            "price": { 
                "type": "scaled_float",
                "scaling_factor": 100 
            },    
            "education": { "type": "keyword" },
            "biography": { "type": "text" },
            "keywords": { "type": "text" },
            "current_location": { "type": "geo_point" },
            "previous_tours": { 
                "type": "nested", 
                "properties": {
                    "altitude": { "type": "float" },
                    "distance": { "type": "float" },
                    "days": {"type": "short"},
                    "tour_keywords": { "type": "text" },
                    "places": {
                        "type": "nested",
                        "properties": {
                            "name": { "type": "text"},
                            "location": { "type": "geo_point"}
                        }
                    }
                }
            }
        }
    }
 })
