# Project2_2020_Metis

### The Goal...
**"How many plays is this board game going to get?"** The goal of the project is to predict the average plays per person. Currently, on BoardGameGeek.com (BGG), this can be calculated by dividing total plays of a game by total owners of the game. All the attributes listed below (1-11) can be found on the website.

## MVP 1

### Webscrape
- Webscrape [BGG](https://boardgamegeek.com/boardgame/167791/terraforming-mars) : [Click here](https://github.com/er-arcadio/Project2_2020_Metis/blob/master/Scraping_BGG.ipynb) for the notebook
- Clean the code enough to itterate multiple game links
- Use Selenium to get more than 100 rows
- Clean and EDA using Pandas (Pair plot)
- Linear Regression
- Validation

Attributes
1. Avg. Rating (out of 10)
2. No. of Ratings (people who've rated it)
3. Weight (Difficulty)
4. Overall Rank
5. Playing Time (low end)
6. *Age*
7. *Number of players*
10. Cost of Game
10. **Yn - All Time Plays**
11. **Yd - Own (# of people that own game)**

*Note: 6 and 7 are categorical -- 6 is Ordinal; 7 is Nominal*

*Note:* **Y**, *the expected output, is Yn/Yd*

### Presentation

1. Intro
2. Method and Tools
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
