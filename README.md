<h1 align="center">Movie Recommendation API</h1>

<p align="center">
  <b>A movie recommendation system based on user preferences.</b><br>
  Built with Scikit-Learn for machine learning and Flask for the web framework.
</p>

---

## 📝 Table of Contents
1. [Introduction](#introduction)
2. [Technology Stack](#technology-stack)
3. [Relevant Hardware Specifications](#relevant-hardware-specifications)
4. [Data](#data)
5. [Features](#features)
6. [Installation](#installation)
7. [Usage](#usage)
8. [API Endpoints](#api-endpoints)
9. [Requests and Examples](#requests-and-examples)

---

## 📖 Introduction

This API is a **content-based recommendation system**. It suggests movies similar to those that users have previously liked based on features like genre, cast, and plot. For example, if a user enjoys *Joker*, the system recommends movies with similar themes, genres, or actors.

## 🛠 Technology Stack

- **Programming Language:** Python
- **Framework:** Flask (for REST API)
- **Machine Learning Library:** Scikit-Learn

## 💻 Relevant Hardware Specifications

The project is developed on a MacBook with the **Apple M3 Max chip**, which offers the following benefits for model training and API performance:

- **CPU:** 16 cores (12 performance cores, 4 efficiency cores), optimized for efficient multitasking.
- **Neural Engine:** 16 cores, designed for machine learning tasks to speed up calculations.
- **Memory Bandwidth:** 400GB/s, enabling fast data processing, suitable for handling large movie datasets.

## 🎬 Data

The data includes metadata on movies such as genres, casts, and overviews. The datasets are publicly available on Kaggle:

- [The Indian Movie Database](https://www.kaggle.com/datasets/pncnmnp/the-indian-movie-database)
- [TMDB Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## ✨ Features

1. **Dataset Description:** Overview of the datasets used, including sources and how they are utilized in the recommendation system.
2. **Content-Based Recommendation System:** Predicts movie recommendations based on user preferences using Scikit-Learn.
3. **REST API with Flask:** Simple REST API to get movie recommendations locally.
4. **Localhost Testing:** Easily test the API on `127.0.0.1` to see recommendations based on specific movie inputs.

## ⚙️ Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>
