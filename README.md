# Movie Recommendation System
A programme to take in the description as a parameter and return the title of the most similar movie.
This project implements a simple movie recommendation system based on similarity of movie descriptions. Given a description of a movie, the system suggests the most similar movie from a pre-defined list.

## Features

- Utilizes natural language processing (NLP) techniques to calculate similarity between movie descriptions.
- Recommends the movie that is closest in description to the input movie.
- Supports a customizable list of movies and their descriptions.

## Requirements

- Python 3.x
- Dependencies: spacy

## Installation

1. Clone the repository:
   git clone https://github.com/your-username/your-repository.git
   
Install the required dependencies:
pip install -r requirements.txt

Usage

Ensure that your movie data is stored in the movies.txt file, following the specified format.
Modify the find_similar_movie function in watch_next.py to adjust the recommendation logic if needed.
Run the script and provide a movie description as input:
python watch_next.py
The system will recommend the movie that is most similar to the input description.
Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.




