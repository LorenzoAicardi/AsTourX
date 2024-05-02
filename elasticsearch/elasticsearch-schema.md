## Mappings
```[elasticsearch]
PUT /guides
{
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
      "keywords": { "type": "keyword" },
      "current_location": { "type": "geo_point" }
    }
  }
}
```
