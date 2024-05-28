# Scope of the project

The project consists in developing an algorithm that matches tourists to guides according to their preferences in an uber-like way. The project was developed considering that users may want to use the application "on the fly", inserting only essential information in a rapid way. 

# Development of the project

During the initial phases, we thought about organizing the guides in a tree-like data structure, that would put each guide in a separate bucket, according to some features. In this way, we would be updating information only about the considered bucket. The problem that arose using this solution was that certain data types (such as the keywords, which were considered by us as the main services offered by the guide) were hardly categorizable using this approach; the method also wouldn't scale well in the worst case scenario in which there was a number of buckets equal to the number of guides. 

For this reason we decided to take on different approaches; we split the group in two, with one group working on a recommender system, and the other working using ElasticSearch.

# ElasticSearch

Our sub-group (Aicardi, Benzoni, Cartechini) focused on the ElasticSearch approach. The idea behind using ElasticSearch was giving arbitrary scores to certain features, and returning an ordered list of guides according to the tourist's preferences. These scores were derived from data provided us by our supervisors, provided to us in the form of closed answers to questions concerning the importance of certain aspects in guides and tours. From there, we derived the confidence intervals for each feature weight, and decided to score as most important the ones that had the smallest intervals with the highest mean. In particular, the most important features were: 
- Price;
- Important places to be seen;
- Current location of the guide;
- Necessity of buying tickets.

However, some constraints were deemed to be too important to be ignored, such as the language spoken, and the availability of the guide. For this reason, in the query results, guides were first filtered on these 2 features, and then ranked.

We decided to use ElasticSearch in a query-like approach, using two different indices: considering previous tours, and not considering previous tours but only the relevant guide features. You can find [here](elasticsearch_schemas.md) both the indices we used.  

## Tour-less approach

In the tour-less approach, we put more weight on the guide itself rather than the tours he/she offered. We employed this strategy to study whether or not the tours themselves were relevant for the decision of the tourist. The queries were written using feature engineering, using similarity functions in order to determine the partial score of the query. The guides were then visualized ordered according to their scores.

## Tour approach

Finally, we have tried the same query approach, this time considering the information given by the tours offered by each guide. According to this approach, the most important aspect considered by the user were the tours themselves, while the guide itself wouldn't be too much of a factor in the decision. The queries were similar, but with some differences: there was a new tour keyword, it having as features the places visited, and the duration (expressed in days). The assumption is that guides typically offer similar tours: tourists are more interested in guides who provide tours they want, rather than the guides' individual features.

# Conclusion

Given the lack of data, the entirety of the project was based on assumptions. We believe the queries as they are right now would work reasonably well, and that ElasticSearch is well-scalable. However, our decisions can only be validated considering future data. This data might be used to tune the feature importance weights that compute the scores, leading to better rankings.
