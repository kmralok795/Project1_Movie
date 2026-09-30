Movie Recommendation System

Ever found yourself scrolling through movies for 20 minutes and still couldn't decide what to watch? This project was built to make that process a little easier.

The Movie Recommendation System is a machine learning project that recommends movies similar to a movie selected by the user. Instead of relying on user ratings or watch history, the system looks at the content of the movies—such as genre, keywords, tagline, cast, and director—to find movies with similar characteristics.

How It Works:
The recommendation system follows a Content-Based Filtering approach.
First, the relevant information about each movie is combined into a single set of features. These textual features are converted into numerical vectors using TF-IDF (Term Frequency-Inverse Document Frequency).

The system then uses Cosine Similarity to compare these vectors and determine how similar one movie is to another.

When a user enters a movie name, the system:

Finds the closest matching movie title.
Retrieves its similarity scores with other movies.
Sorts the movies according to their similarity.
Selects the most similar movies.
Displays the recommendations to the user.
🛠️ Technologies Used
Python – Main programming language
Pandas – Data loading and preprocessing
Scikit-learn – TF-IDF and Cosine Similarity
Difflib – Finding the closest matching movie title
Streamlit – Building the interactive web interface


Project Structure
Movie-Recommendation-System/
│
├── Project1_Movie.ipynb    # Complete ML implementation
├── recommender.py          # Recommendation engine
├── app.py                  # Streamlit application
├── tmdb.py                 # Movie poster/rating API
├── requirements.txt        # Required Python libraries
├── .gitignore              # Files excluded from Git
└── README.md               # Project documentation
