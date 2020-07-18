# Web Scraping and Linear Regression

### Project Thesis
**"How many plays is this board game going to get?"** The goal of the project is to predict the average plays per person. Currently, on BoardGameGeek.com (BGG), this can be calculated by dividing total plays of a game by total owners of the game.

## MVP 1 - Webscrape & Baseline Model

- Webscrape BGG
- Itterate over multiple browser pages (10 pages : 1 thousand games)
- Clean data and fix categorical
- EDA using Pandas (Pair plot and correlations)
- Linear Regression Analysis and Assumptions
- Kfold Cross Validation - 10 folds

**Jupyter Notebooks**

[Web Scraping BGG.com Notebook](https://github.com/er-arcadio/Project2_2020_Metis/blob/master/Scraping_BGG.ipynb)

[Linear Regression Model Selection Notebook](https://github.com/er-arcadio/Project2_2020_Metis/blob/master/BGG_Model.ipynb)

*Note: The target is Avg_Plays*
<br>

## MVP 2 - Model Tuning and Python Files
- Model Tuning - Feature Engineering, Outliers, Multicolinearity
- Play with Polynomial, Log, and Sqrt Features to increase complexity where needed
- Fine tune with Regularization if needed (Ridge, Lasso)
- Write .py files for Web Scraping BGG (requests, BeautifulSoup, regex, json)
- ...and for Cross Validate and to display Linear Assumptions (more general)

**Python Files**

[Web Scraping BGG.com .py](https://github.com/er-arcadio/Project2_2020_Metis/blob/master/BGG.py)

[Linear Regression Model Selection .py](https://github.com/er-arcadio/Project2_2020_Metis/blob/master/model_selection.py)

## Results 

**Best Model:** eliminate outliers (3%), log features, square root features, polynomial: degree 3, and Lasso: lambda 0.0075

**Key Features:** Diificulty, Time, Rank, 6 players

**r^2:** originally: 0.196 --- finally: **0.30**

## Future Works

Include the following attributes (harder to scrape)
- Number of expansions 
- Theme
- Price (from Amazon)
- Weight (from Amazon)

Also...
- More rows of data (in retrospect)
- Have fun with [LARS Path](https://github.com/thisismetis/chi20_ds15/blob/master/curriculum/project-02/regularization/regularization_code.ipynb)

## Other Resources
[Link](https://github.com/thisismetis/chi20_ds15/blob/master/curriculum/project-02/project-02-introduction/project_02.md) to the Specs for Project 2.

[Link](https://docs.google.com/document/d/1oAJrWNR7HxNJVI2IHUuHArEvBccowLqvPObYbqtH0rs/edit) to the Grading Rubric.

[Link](https://data.library.virginia.edu/interpreting-log-transformations-in-a-linear-model/) to "How to interpret Beta Coefficients
