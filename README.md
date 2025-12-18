# Rock Paper Scissors Web App

**Version:** 1.0.0

## 📖 What is it?
This project is a web-based implementation of the classic hand game "Rock, Paper, Scissors". It serves as a simple, interactive application that allows users to play the game directly through their web browser using a clean and responsive interface.

## 🚀 What it does
The application hosts a local two-player game session.
* Player 1 makes a selection (Rock, Paper, or Scissors) which is temporarily hidden or queued.
* The game prompts Player 2 to take their turn.
* Once both players have chosen, the selections are revealed on the screen, allowing the players to see the result.

## 🛠️ Technologies Used
The project is built using a combination of Python for the backend and standard web technologies for the frontend:
* Backend: Python 3, Flask (Micro-framework).
* Frontend: HTML5, JavaScript (for game logic and DOM manipulation).
* Styling: Bootstrap 5.3.8 (via CDN) for responsive design and layout.

## 🎯 Project Ambition
The ambition of this project is to provide a lightweight, easy-to-deploy example of a web application that integrates a Python backend with a dynamic frontend. It aims to demonstrate basic routing, template rendering, and event handling in a fun, gamified context.

## 📊 Project Status
Current Stage: Finished (v1.0.0)
The core functionality of selecting options and displaying player choices is complete and operational.

## ⚠️ Known Issues & Improvements
While the project is functional, there are areas identified for future enhancement:planned improvement.
* **Input Masking:** Improving the UX to better hide Player 1's choice before Player 2 plays would enhance the local multiplayer experience.
* **Remote Multiplayer:** The current version is designed for two players on the same device. Future versions could implement WebSocket support for remote play.