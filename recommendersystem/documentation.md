# Task Description

This part of the project consists in building a recommender system to make personalized recommendations
of guides or organized tours for each tourist.
The recommendations are based on the profiles of tourists, guides and tours, which include keywords that characterize them, 
and the ratings given to guides or tours by tourists themselves.


# Project Scope

The primary objective of this recommender system is to:
- Recommend guides or tours to tourists based on their profile keywords
- Utilize the ratings provided by tourists to improve the accuracy of recommendations


# Project Presentation

The working procedure involves two phases:
## [**Data Generation**](Datageneration.ipynb) 

It focuses on creating synthetic datasets to train the models. Due to the current scarcity of real data, we simulate dataframes sampled from statistical distributions. 
However, these simulations are carefully constrained to reflect real-world scenarios. The data that we consider relevant for our purposes are:
  - Profiles of tourists
  - Profiles of guides
  - Attributes of tours
  - Interactions between tourists and guides
  - Interactions between tourists and tours

In particular, the interactions are presented in the form of explicit ratings given by the tourists, 
in a rating scale from 1 to 5. The attributes about tourists, guides and tours are selected and generated according to 
the application's requirements. 

In the folder [Data](Data) we have saved two sets of generated samples that we use to implement and test our algorithms:
1) 200 tourists, 40 guides and 40 tours;
2) 500 tourists, 50 guides and 50 tours.

Generally, recommendation systems tend to work better when there is possibility to collect a great amount of reliable samples. 
In this way they have more information from which learn patterns and distributions, in order to produce
more consistent suggestions. Moreover, when many samples are present, it would be nice to hold out a portion of data for testing purposes.


## **Recommendation Pipeline**
It includes the steps involved in generating recommendation using the available data, such as:
- Load and preprocess dataframes.
- Create the **User Rating Matrix** (URM) and the **Item Content Matrix** (ICM) from data.
These matrices contain the information we need to train the models, and they are essential for the proper functioning of recommender systems. 
- Implement the **similarity function** and the **recommender algorithms**. 
  
  We have used two kinds of approaches to solve the tasks:
    - **Collaborative Filtering**, which only relies on the past ratings of tourists without considering any attributes.
    - **Content-Based Filtering**, which evaluates the similarity between guides or tours through their common attributes. 
  
    In addition, the cosine similarity metric is chosen to evaluate whether two "items" are similar.
- Build and fit the models.
- Generate the recommendations.

These phases collectively form the foundation of our recommender system, aiming to enhance tourists' experiences by providing personalized and relevant recommendations.

With respect to the pipeline, two distinct problems have been explored:

- [**Recommendation of guides**](GuideRecommendation.ipynb): this notebook file reports the process of recommending guides to the tourists.

- [**Recommendation of tours**](TourRecommendation.ipynb) associated to the guides: 
this notebook documents the process of recommending organized tours that are likely to appeal to the tourists.

The recommendation algorithms allow us to emphasize highly relevant constraints (e.g. languages), and to take them into account during the matching
procedure. Hyperparameters such as the shrink value can be tuned to obtain better performance. 

Further details about the implementation can be found in the notebooks.

# Conclusion

This part of the project is focused on identifying and recommending the most suitable "items" (guides or organized tours) for the tourists with respect to stored data, rather than real-time matching.
We start working from the recommendation of guides, and conclude with adapting the framework to the case of published tours. 

We believe that recommending specific tours is more meaningful to tourists than merely suggesting guides, as tourists are generally more interested in the places they wish to visit.

However, due to the current lack of user profiles and interaction data between guides and tourists, we cannot properly estimate the performance of the models, which are trained on synthetic datasets for now.

As more data is collected, the recommendation system will be able to provide increasingly personalized and accurate recommendations to each tourist, enhancing their overall experience.
