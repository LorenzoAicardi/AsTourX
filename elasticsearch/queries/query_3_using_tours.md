## The idea
The idea is to use the `previous_tours` attribute to find guides that have experience with certain keywords or locations. The script score will be used to calculate the score based on the age, price, education, and distance between the user and the guide.
We have used as the base query the one from the [query 1](query_1_script_score_approach.md) file.
As in the query 1, we can modify the weights of the scores to adjust the importance of each attribute.
The script score will be calculated as follows:
- Age scorer: The score will be calculated based on the age of the guide. The closer the age to the target age, the higher the score.
- Price scorer: The score will be calculated based on the price of the guide. The lower the price, the higher the score.
- Education scorer: The score will be calculated based on the education of the guide. The higher the education, the higher the score.
- Distance scorer: The score will be calculated based on the distance between the user and the guide. The closer the guide, the higher the score.
- The final score will be calculated as a weighted sum of the scores and the default score.

### The default score

The default score is the score calculated by Elasticsearch based on the query and the document.
This score take account of the tour keywords, the tour places, and the distance between the places and my target logation (the user's current location or the location of a POI that the user is interested in).

### Query

```elasticsearch
{
  "query": {
    "function_score": {
      "query": {
        "bool": {
          "must": [
            {
              "terms": {
                "languages_spoken": ["bulgarian"]
              }
            },
            {
              "term": {
                "now_available": True
              }
            }
          ],
          "should": [
            {
              "nested": {
                "path": "previous_tours",
                "query": {
                  "bool": {
                    "should": [
                      {
                        "match": {
                          "previous_tours.tour_keywords": {
                            "query": "wine museums",
                            "operator": "or"
                          }
                        }
                      },
                      {
                        "nested": {
                          "path": "previous_tours.places",
                          "query": {
                            "bool": {
                              "should": [
                                {
                                  "match": {
                                    "previous_tours.places.name": {
                                      "query": "colosseum",
                                      "operator": "or"
                                    }
                                  }
                                },
                                {
                                  "geo_distance": {
                                    "distance": "10km",
                                    "previous_tours.places.location": {
                                      "lat": 41.8902,
                                      "lon": 18.160
                                    }
                                  }
                                }
                              ]
                            }
                          },
                        }
                      }
                    ]
                  }
                },
              }
            }
          ]
        }
      },
      "script_score": {
        "script": {
          "source": 
          """
            // Age scorer
            def target_age = params.target_age;
            Instant instant = Instant.ofEpochMilli(new Date().getTime());
            ZonedDateTime birth = doc['birth_date'].value;
            ZonedDateTime now = ZonedDateTime.ofInstant(instant, ZoneId.of('Z'));
            def doc_age = ChronoUnit.YEARS.between(birth, now);
            def age_score = Math.exp(-Math.pow(target_age - doc_age, 2) / 150);
            
            // Price scorer
            def price_score = Math.pow(2, -doc['price'].value / params.avg_price);
            
            // Education scorer
            def user_education = params.user_education;
            def education_scores_map = [
              "elementary": 0,
              "high-school": 0.2,
              "bachelor": 0.5,
              "master": 0.9,
              "phd": 1
            ];
            def guide_education = doc['education'].value;
            def education_score = education_scores_map[guide_education];
            def education_diff = education_scores_map[user_education] - education_score;
            def adjusted_education_score = Math.max(0, education_score + education_diff);
            
            // Distance scorer
            double target_lat = params.target_lat;
            double target_lon = params.target_lon;
            double targetLatRad = Math.toRadians(target_lat);
            double targetLonRad = Math.toRadians(target_lon);
            double docLat = doc['current_location'].lat;
            double docLon = doc['current_location'].lon;
            double docLatRad = Math.toRadians(docLat);
            double docLonRad = Math.toRadians(docLon);
            double earthRadius = 6371.0;
            double dLat = docLatRad - targetLatRad;
            double dLon = docLonRad - targetLonRad;
            double a = Math.sin(dLat / 2.0) * Math.sin(dLat / 2.0) +
                       Math.cos(targetLatRad) * Math.cos(docLatRad) *
                       Math.sin(dLon / 2.0) * Math.sin(dLon / 2.0);
            double c = 2.0 * Math.atan2(Math.sqrt(a), Math.sqrt(1.0 - a));
            double distance = earthRadius * c;
            double distance_score = 1 / (1 + distance);
            
            return 0.1 * age_score
                   + 0.3 * price_score
                   + 0.1 * adjusted_education_score
                   + 0.3 * distance_score
                   + 2 * _score;
          """,
          "params": {
            "target_age": 17,
            "avg_price": 31,
            "target_lat": 41.462,
            "target_lon": 18.161,
            "user_education": "phd"
          },
        },
      },
    }
  }
}
```