# Fake News Detector
## [**Click here to view the app**](https://detect-fake-news-app.herokuapp.com)
## Project Dcescription
The goal of this project is to create a model using machine learning that can determine whether an article is fake news or not. To interact with this model, a web page will be created that will allow a user to enter a article title/paragraph/URL and have the model determine whether that specific article is fake news or real news. An analysis will also be conducted to see what the characteristics of a fake news article are and compare to the characteristic of real news article and help make fake news more identifiable.

## Motivation
Fake news has become an issue in today’s climate, especially with the prevalence of social media and easily shareable content. Fake news can often spread quickly and can be taken as fact when it is bias and/or opiniated. It is also sometimes difficult/time consuming to determine what is fake news or not. This is why we have decided explore what makes fake news, fake news and how to distinguish it from real news.

## **Using the App**:
To get a prediction enter an article title or paragraph(s) in the input box and click go. To view the analysis click on the arrows on the dashboard.

## **Tools used**:
- Python (for data pre-processing and model creation)
- HTML (app Design)
- CSS
- Heroku (for deploying the app)


## **Python Packages Used**:
- Pandas (for data pre-processing)
- Scikit-learn (for model creation)
- Flask (for app creation)
- nltk, spacy (for natural language processing)
- pickle (for model saving)

## **Conclusions**


## **Screenshots**
## **Before Article is entered**
![Web application before entering article](Screenshots/enter.png)

## **After Article is entered (real prediction)**
![Web application after entering article (true)](Screenshots/true.png)

## **After Article is entered (fake prediction)**
![Web application before entering article (false)](Screenshots/fake.png)

## **Analysis**
![Data percentage](Screenshots/tableau1.png)
![Body/Title Length](Screenshots/tableau2.png)
![Data percentage](Screenshots/tableau3.png)


## **Running the jupyter notebooks**
1. Before running any of the jupyter notebooks please install needed packages running the following code in the terminal.
         
        pip install pandas
        pip install sqlalchemy
        pip install geopandas
        pip install Flask-sqlalchemy
        pip install matplotlib
Or run this code in the first Jupyter Notebook

        ! pip install --user pandas
        ! pip install --user sqlalchemy
        ! pip install --user geopandas
        ! pip install --user Flask-sqlalchemy
2. Run the file *DataCleaning.ipynb* 


3. Run the file *Conclusions.ipynb* 