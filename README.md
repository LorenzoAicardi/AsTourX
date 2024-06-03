# AsTourX

## Project Description
The project has been proposed as a platform to facilitate the interaction
between tourists and professional tour guides, 
allowing tourists to book guides in real-time or to join already organized tours, 
according to their specific preferences and schedules. 

Hence, it aims to enhance the travel experience of the tourists, 
and also to provide further income opportunities to tour guides.

## Team Members
- [Lorenzo Aicardi](https://github.com/LorenzoAicardi)
- [Lorenzo Benzoni](https://github.com/lorebenzo)
- [Giacomo Cartechini](https://github.com/Ax-Time)
- [Giulia Huang](https://github.com/giuliahuang)
- [Zheng Maria Yu](https://github.com/Trixyz28)


## Project Organization
After the initial phase of discussions along with data analysis and experiments ([notebook](notebook.ipynb)), 
we decided to develop two distinct methods to solve the problem of
matching guides and organized tours to tourists. 
- [**Elastic search**](/elasticsearch) is based on the use of queries, in which
arbitrary scores are given to specific features. It is able to generate an ordered list of guides and tours
according to the importance of each feature.
- [**Recommender system**](/recommendersystem) takes origin from the supposition that similar tourists would like similar "items" 
(guides or tours). So it relies on the computation of pairwise similarity scores between guides or tours, which are ranked
for the final output.

Each of the sub-folders contains more detailed documentation about the algorithm.

## Project Setup

### Elastic Search



### Recommender System
The prototype of the recommendation engine is implemented in Python using **Jupyter Notebook**, 
where code cells are directly runnable. 

To install the required libraries, it is possible to use the command:
```sh
pip install -r recommendersystem/requirements.txt
```