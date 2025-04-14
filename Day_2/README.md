Random Quote Generator Web App
This project is a simple web app that generates random quotes and allows users to add their own quotes via a Flask backend and a JavaScript frontend. It is built using Flask for the backend API and JavaScript for the frontend interaction.

Features:
Generate Random Quotes: Displays a random quote each time you click the "Get Quote" button.

Add New Quotes: Users can submit their own quotes which will be added to the list of available quotes.

Tech Stack:
Frontend:

HTML

JavaScript (Fetch API for HTTP requests)

CSS (for styling the page)

Backend:

Python (Flask Framework)

JSON (for handling quote data exchange)

Tasks Completed Today:
Flask Tasks:
Task 1: Backend - Flask API Setup:

Created a Flask API to serve random quotes.

Implemented a POST method to add new quotes to the list.

Task 2: Frontend - DOM Manipulation:

Created a button that fetches a random quote using JavaScript's fetch API.

Added a click event listener to display a random quote when the user clicks the "Get Quote" button.

Set up an event listener for DOMContentLoaded to automatically display a quote when the page loads.

Task 3: User Input - Adding New Quotes:

Implemented a form and a POST request for users to add new quotes through the frontend.

The form sends the new quote to the backend, which adds it to the list of available quotes.

Task 4: Styling:

Styled the page with basic CSS to improve the look and feel of the application.

Python Problems:
Problem 1: Finding the Missing Number

Task: Write a function to find the missing number in a list containing numbers from 1 to n.

Problem 2: Finding Pairs with a Target Sum

Task: Write a function to find all pairs of integers in a list that sum up to a given target.

Solution:

Problem 3: Append Value to List

Task: Write a function that appends a value to a list, ensuring that a new list is created if no list is passed.

How it Works:
Backend API:

The API is served using Flask at the /api/quote endpoint.

It supports both GET requests (for retrieving a random quote) and POST requests (for adding new quotes to the list).

Frontend:

JavaScript is used to listen for user interactions.

When the "Get Quote" button is clicked, it fetches a random quote from the Flask API and displays it.

The user can also add a new quote through the input field, and it will be sent to the Flask API, which stores it for future use.

Future Improvements:
Add user-specific features (e.g., allowing each user to save their own quotes).

Implement error handling for API requests (e.g., notifying the user if something goes wrong).

Enhance styling and design for a better user experience.

Acknowledgements:
Inspired by common web applications that use Flask and JavaScript for backend-frontend communication.