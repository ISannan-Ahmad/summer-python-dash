# Python Projects - Day 1

This repository contains Python projects to enhance problem-solving and programming skills. The projects will be built incrementally, starting from small challenges to more complex ones.

# Day 1: Problem-Solving Challenge

# Task 1: Find the Maximum Number in a List

In this challenge, we wrote a Python function `my_max()` that finds the maximum number in a list. The function iterates through the list and compares each element to determine the largest number.

# Task 2: Count Frequency of Each Element in a List

This task involves creating a function `count_frequency()` that takes a list as input and returns the most frequent number. It uses a dictionary to store the count of each number and determines the most frequent one by iterating through the dictionary.


# Flask Quote Generator API

# Overview

This is a simple Flask API that generates random quotes when requested. The API exposes a single endpoint, `/api/quote`, which returns a random quote from a predefined list.

# Features

- **Random Quote API**: A single endpoint (`/api/quote`) returns a random quote from a list of quotes.
- **Frontend Integration**: A simple HTML page with JavaScript fetches the quote from the Flask backend and displays it dynamically on the page.

# Technologies Used

- **Backend**: Flask
- **Frontend**: HTML, JavaScript
- **API Endpoint**: `/api/quote` (returns a random quote as JSON)


# How It Works

- The frontend HTML page makes a request to the `/api/quote` route using JavaScript (`fetch`).
- When the user clicks the "Get Quote" button, the frontend sends a request to the backend, and the backend returns a random quote as JSON.
- The quote is then displayed dynamically on the page.

# Example API Response

When you make a GET request to `/api/quote`, the API returns a random quote in the following format:

{
  "Quote": "The only limit to our realization of tomorrow is our doubts of today."
}
