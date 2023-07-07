import re
import spacy
import warnings

def find_similar_movie(description):
    # Load movie data from the file
    with open('movies.txt', 'r') as file:
        movie_data = file.read()

    # Extract titles and descriptions from the movie data
    movie_list = re.findall(r"Movie ([A-Z]) :(.+)", movie_data)
    titles, descriptions = zip(*movie_list)

    # Add the description of Planet Hulk to the list
    titles = list(titles)
    descriptions = list(descriptions)
    titles.append('Planet Hulk')
    descriptions.append(description)

    # Initialize spaCy's English language model
    nlp = spacy.load('en_core_web_sm')

    # Suppress the warning
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning)
        # Calculate similarity scores between descriptions using spaCy
        target_doc = nlp(description)
        similarity_scores = [target_doc.similarity(nlp(desc)) for desc in descriptions]

    # Find the index of the movie with the highest similarity score (excluding "Planet Hulk")
    most_similar_index = similarity_scores.index(max(similarity_scores[:-1]))

    # Return the title and description of the most similar movie
    return titles[most_similar_index], descriptions[most_similar_index]




description = "Will he save their world or destroy it? When the Hulk becomes " \
              "too dangerous for the Earth, the Illuminati trick Hulk into a shuttle " \
              "and launch him into space to a planet where the Hulk can live in peace. " \
              "Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery " \
              "and trained as a gladiator."

similar_movie_title, similar_movie_description = find_similar_movie(description)
print("Most similar movie title:", similar_movie_title)
print("Most similar movie description:", similar_movie_description)

