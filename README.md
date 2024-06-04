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
After the initial phase of discussions along with data analysis and experiments, 
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
To run our query-based matching engine, you need first to install [Docker](https://www.docker.com/products/docker-desktop/).

Before doing anything, make sure to cd into the elasticsearch folder:
```
cd elasticsearch
```

For environment variables, you need a **.env** file:
```
touch .env
```
An example of the content of the **.env** file is:
```
HOST=http://localhost:9200
```

We strongly recommend you to install python dependencies into a virtual environment. 
You can create it by doing:
```
python -m venv .venv
```
Then, activate the virtual environment by doing:
```
source .venv/bin/activate
```
To install the dependencies, run:
```
make init
```

Now, start the elasticsearch container by running:
```
make up
```

To initialize the elasticsearch index, run:
```
make init_elasticsearch
```

To feed the index with random data, run:
```
make load_guides_tours
```

Now you can access the Kibana dashboard by connecting to your HOST at port **5601**.
For example, if your HOST is **http://localhost:9200**, you can access the dashboard by connecting to **http://localhost:5601**.

From there you can perform the queries by going to the Dev Tools section, create views, dashboards and see the results.

To stop the elasticsearch container, run:
```
make down
```

Depending on the settings of your docker, you might need to run the commands with **sudo**.


### Recommender System
The prototype of the recommendation engine is implemented in Python using **Jupyter Notebook**, 
where code cells are directly runnable. 

To install the required libraries, it is possible to use the command:
```sh
pip install -r recommendersystem/requirements.txt
```
