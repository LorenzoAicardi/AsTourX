GET ${exampleVariable1} // _search
{
  "query": {
    "function_score": {
      "query": {
        "bool": {
          "must": [
            { 
              "match": { 
                "now_available": true 
              }
            },
            { 
              "terms": { 
                "languages_spoken": ["english", "spanish"] 
              }
            }
          ]
        }
      },
      "functions": [
        {
          "field_value_factor": {
            "field": "price",
            "factor": 0.7,
            "missing": 1
          }
        },
        {
          "gauss": {
            "current_location": {
              "origin": "41.8781, -87.6298",
              "scale": "100km",
              "offset": "0km",
              "decay": 0.5
            }
          }
        },
        {
          "filter": { 
            "terms": { 
              "keywords": ["history", "art"] 
            }
          },
          "weight": 0.5
        },
        {
          "filter": { 
            "term": { 
              "education": "college" 
            }
          },
          "weight": 0.2
        }
      ],
      "score_mode": "sum",
      "boost_mode": "multiply"
    }
  }
}