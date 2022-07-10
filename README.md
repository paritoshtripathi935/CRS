<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="CRS" />

  &#xa0;

  <!-- <a href="https://crs.netlify.app">Demo</a> -->
</div>

<h1 align="center">CRS</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/paritoshtripathi935/CRS?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/paritoshtripathi935/CRS?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/paritoshtripathi935/CRS?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/paritoshtripathi935/CRS?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/{{YOUR_GITHUB_USERNAME}}/crs?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/{{YOUR_GITHUB_USERNAME}}/crs?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/{{YOUR_GITHUB_USERNAME}}/crs?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  CRS 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/paritoshtripathi935" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Describe your project
It is Course Recommendation Engine built uisng similarity matrix techinique in python with help of pandas and numpy.

### Technologies - 
1. Neat text – for cleaning of descriptions and titles
2. Pandas – for data frame handling
3. Sklearn CountVectorizer,TfidfVectorizer
4. Sklearn cosine similarity,linear kernel 

### Algorithms Approach - 
1. First we will get all the data and use description and title for getting keywords. We will use neat text for getting rid of all pro propositions and other characters from the description.
2. Building a new column of clean titles and descriptions from original columns to
help convert them.
3. now we will convert the cleaned titles into Vector using sklearn CountVectorizer,TfidfVectorizer.
4. Now we will use cosine similarity to generate a similarity score between courses
and other parameters
5. Now we will sort the scores to get the top 10 scores when a keyword is entered. 

### Cosine similarity
Cosine similarity is the measure of similarity between two vectors, by computing the cosine of the angle between two vectors projected into multidimensional space. It can be applied to items available on a dataset to compute similarity to one another via keywords or other metrics. Similarity between two vectors (A and B) is calculated by taking the dot product of the two vectors and dividing it by the magnitude value as shown in the equation below. We can simply say that the CS score of two vectors increases as the angle between them decreases.

## :sparkles: Features ##

:heavy_check_mark: Feature 1;
:heavy_check_mark: Feature 2;
:heavy_check_mark: Feature 3;

## :rocket: Technologies ##

The following tools were used in this project:

- [python](https://www.python.org/)
- [sklearn](https://scikit-learn.org/)
- [pandas](https://pandas.pydata.org/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [python](https://www.python.org/) installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/{{YOUR_GITHUB_USERNAME}}/crs

# Access
$ cd crs

# Install dependencies
$ pip install -r requirements.txt

# Run the project
$ streamlit run app.py

# The server will initialize in the <http://localhost:3000>
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made with :heart: by <a href="https://github.com/paritoshtripathi" target="_blank">Paritosh Tripathi</a>

&#xa0;

<a href="#top">Back to top</a>
