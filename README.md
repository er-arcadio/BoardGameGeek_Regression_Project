# Project2_2020_Metis

### The Goal...
**"How many plays is this board game going to get?"** The goal of the project is to predict the average plays per person. Currently, on BoardGameGeek.com (BGG), this can be calculated by dividing total plays of a game by total owners of the game. All the attributes listed below (1-11) can be found on the website.

## MVP 1

### Webscrape
- *Webscrape [BGG](https://boardgamegeek.com/boardgame/167791/terraforming-mars) : [Click here](https://github.com/er-arcadio/Project2_2020_Metis/blob/master/Scraping_BGG.ipynb) for the notebook*
- Itterate over multiple browser pages (10 pages : 1 thousand games)
- Clean data, fix categorical, and do EDA using Pandas (Pair plot)
- Linear Regression Analysis
- Validation

*Note: Attributes "Min_Age" and "*_Players" are categorical -- first being Ordinal; and latter being Nominal (Dummy Values)*

*Note:* **Y**, *Avg_Plays, the expected output, is Total_Plays/Owners*

### Presentation

1. Intro
2. Method and Tools
  - Scraped BGG for name and links then used link to scrape more info
  - formatted string to iterate over multiple pages
  - .py file with scrape methods (requests, BeautifulSoup, json)
3. Results
4. Conclusion (& Recommendation & Future Works)

### This Repo & Read me w/ process

<br>

## MVP 2
- Play with Polynomial Regression to increase/decrease complexity where needed
- Try cross Validation
- Fine tune with Regularization if needed (Ridge, Lasso)

## MVP 3
- Webscrape Amazon

For 12. Product information > Item *Weight*

and 13. Product Cost)

## Future
- Include: Prev. Owned (# of people who previously owened game)
- Include: # of comments on a game
- Number of expansions

## Other Resources
[Link](https://github.com/thisismetis/chi20_ds15/blob/master/curriculum/project-02/project-02-introduction/project_02.md) to the Specs for Project 2.

[Link](https://docs.google.com/document/d/1oAJrWNR7HxNJVI2IHUuHArEvBccowLqvPObYbqtH0rs/edit) to the Grading Rubric.
