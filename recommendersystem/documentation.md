# Task Description

This part of the project consists in building a recommender system to make personalized recommendations
of guides or organized tours for each tourist. The recommendations are based on the profiles of tourists, which include keywords that describe their interests, and the ratings given to guides or tours by tourists themselves.


# Project Scope

The primary objective of this recommender system is to:

- Recommend guides or tours to tourists based on their profile keywords
- Utilize the ratings provided by tourists to improve the accuracy of recommendations


# Project Presentation

The working procedure involves two phases:
1. [**Data Generation**](Datageneration.ipynb) focuses on creating synthetic datasets to train the models. Due to the current scarcity of real data, we simulate dataframes sampled from statistical distributions. However, these simulation are carefully constrined to reflect real-world scenarios. The data that we consider relevant for our purposes are:
  - Profiles of tourists
  - Profiles of guides
  - Interactions between tourists and guides
  - Interactions between tourists and tours

  In particular, the interactions are presented in the form of explicit ratings given by the tourists, 
in a rating scale from 1 to 5.


2. **Recommendation Pipeline** includes the steps involved in generating recommendation using the available data. Two distinct approaches have been explored:

- Recommendation of guides: Based on past interactions between tourists and guides, this approach recommends guides to tourists. The recommendation algorithm indentifies guides that are similar to those previously favored by tourists.

- Recommendation of tours associated with guides: This approach considers past interactions between tourists and projected tours associated with guides. It recommends tours that are likely to appeal to tourists based on their previous preferences.

These phases collectively form the foundation of our recommender system, aiming to enhance tourists' experiences by providing personalized and relevant recommendations.

# Conclusion

This phase of the project is focused on identifying the most suitable "products" for tourists, rather than real-time matching. We believe that recommending specific tours is more meaningful to tourists than merely suggesting guides, as tourists are generally more interested in the places they wish to visit.

However, due to the current lack of user profiles and interaction data between guides and tourists, the model cannot be trained to produce accurate and sensible results. As more data is collected, the recommendation system will be able to provide increasingly personalized recommendations to each tourist, enhancing their overall experience.
