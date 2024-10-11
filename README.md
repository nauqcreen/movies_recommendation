Movie Recommendation API

This project is a movie recommendation system that uses Scikit-Learn for model building and Flask as a web framework. The API provides personalized movie recommendations based on user preferences.

Table of Contents

	1.	Technology Stack
	2.	Relevant Hardware Specifications
	3.	Description
	4.	Data
	5.	Features
	6.	Installation
	7.	Usage
	8.	API Endpoints
	9.	Example Request

Technology Stack

	•	Programming Language: Python
	•	Frameworks: Flask (for REST API)
	•	Machine Learning Library: Scikit-Learn

Relevant Hardware Specifications

This project is developed on a MacBook with the Apple M3 Max chip, which provides the following benefits for model training and API performance:

	•	CPU: 16 cores (12 performance cores, 4 efficiency cores), allowing for efficient multitasking and processing.
	•	Neural Engine: 16 cores, optimized for machine learning tasks, enhancing the speed of recommendation calculations.
	•	Memory Bandwidth: 400GB/s, which supports fast data processing, beneficial for large movie datasets.

Description

The recommendation system is a content-based recommendation engine. It recommends movies similar to those the user has previously liked based on features like genre, cast, and other attributes. For example, if a user enjoys Joker, the system will recommend movies with similar themes, and genres, or featuring the same cast.

Data

The data for this project includes metadata on movies such as genres, casts, and plot overviews. The datasets used are publicly available on Kaggle:

	•	The Indian Movie Database (https://www.kaggle.com/datasets/pncnmnp/the-indian-movie-database)
	•	TMDB Movie Metadata (https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

Features

	1.	Dataset Description: Details of the datasets used, including the source, features, and how they are utilized in the recommendation system.
	2.	Content-Based Recommendation System: A Scikit-Learn-based system that predicts movie recommendations based on user preferences.
	3.	REST API with Flask: A simple REST API that can be accessed locally to get movie recommendations.
	4.	Testing on Localhost: Easily test the API on 127.0.0.1 to see recommendations based on specific movie preferences.

Installation



