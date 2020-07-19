# Web Scraping and Linear Regression

### Project 2 at Metis
**Objective: "How many plays will this board game get?"**

The goal of the project is to find a correlation between the average plays per person on a boardgame and other board game features that can be found on BoardGameGeek.com (BGG). For the project, this will be calculated by dividing the total number of plays a game has by the total number of owners of the game.

## Webscrape & A Baseline Model

- Webscrape BGG using requests, BeautifulSoup, regex, and json
- Itterate over multiple browsing pages (10 pages: 100 games per = 1,000 games)
- Clean data (manage null values and outliers) and fix categorical data
- EDA using pandas, matplotlib, and seaborn (Pair plot and correlation plot)
- Linear Regression Analysis and Assumptionsusing sklearn and statsmodel
- Kfold Cross Validation - 10 folds

**Jupyter Notebooks**

["Web Scraping and Cleaning BGG.com" Notebook](https://github.com/er-arcadio/Project2_2020_Metis/blob/master/BGG_Scrape_Clean.ipynb)

["EDA and Model Selection" Notebook](https://github.com/er-arcadio/Project2_2020_Metis/blob/master/BGG_Model.ipynb)

*Note: The target is "Avg_Plays"*
<br>

## Model Selection and Python Files
- Feature Engineering -  play with Polynomial, Log, and Sqrt features to increase complexity where needed
- Outliers - remove outliers that mess up the Linear Assumptions
- Multicolinearity - Fine tune model using Regularization if needed (Ridge, Lasso)
- Write and organaize code in python files for Web Scraping BGG  and model selection.

**Python Files**

[Web Scraping BGG.com .py](https://github.com/er-arcadio/Project2_2020_Metis/blob/master/BGG.py)

[Linear Regression Model Selection .py](https://github.com/er-arcadio/Project2_2020_Metis/blob/master/model_selection.py)
<br>

## Results 

**Best Model:** eliminate outliers (3% of data), add log and square root features, and use polynomial features: degree 3, and lasso regularization: lambda 0.0075

**Key Features:** Diificulty, Time, Rank, 6 players

**r^2:** originally: 0.196 --- finally: **0.30**

## Future Works

Include the following attributes (harder to scrape)
- Number of expansions / reprints
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
