# Web Scraping and Linear Regression

### The Goal...
**"How many plays is this board game going to get?"** The goal of the project is to predict the average plays per person. Currently, on BoardGameGeek.com (BGG), this can be calculated by dividing total plays of a game by total owners of the game.

## MVP 1 - Webscrape & Baseline Model

- *Webscrape [BGG](https://boardgamegeek.com/boardgame/167791/terraforming-mars) : [Click here](https://github.com/er-arcadio/Project2_2020_Metis/blob/master/Scraping_BGG.ipynb) for the notebook*
- *Itterate over multiple browser pages (10 pages : 1 thousand games)*
- *Clean data and fix categorical* 
- EDA using Pandas (Pair plot and correlations)
- Linear Regression Analysis
- Cross Validation 

*Note: The target is Avg_Plays*
<br>

## MVP 2 - Model Tuning and Python Files
- Play with Polynomial, Log, and Sqrt Features to increase complexity where needed
- Fine tune with Regularization if needed (Ridge, Lasso)
- Write .py files for Scraping and Cross Validation.

### Presentation/ Results

1. Intro
2. Method and Tools
  - Scraped BGG for name and links then used link to scrape more info
  - .py file with functions used to scrape (requests, BeautifulSoup, regex, json)
  - Model Tuning: Feature Engineering, Outliers, Multicolinearity
  - .py file with functions used to cross validate and display linear assumptions
3. Results
  - Log features, square root features, polynomial degree 3, and Lasso lambda .0075
4. Conclusion (& Recommendation & Future Works)
  - Key features: Diificulty, Time, Rank, 6 players

## Future - More info!

Include the following attributes 
- Number of expansions (harder to scrape)
- Theme (harder to scrape)
- Price (from Amazon)
- Weight (from Amazon)
- More rows of data (in retrospect)

## Other Resources
[Link](https://github.com/thisismetis/chi20_ds15/blob/master/curriculum/project-02/project-02-introduction/project_02.md) to the Specs for Project 2.

[Link](https://docs.google.com/document/d/1oAJrWNR7HxNJVI2IHUuHArEvBccowLqvPObYbqtH0rs/edit) to the Grading Rubric.

[Link](https://data.library.virginia.edu/interpreting-log-transformations-in-a-linear-model/) to "How to interpret Beta Coefficients
