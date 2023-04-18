## Introduction

Welcome to Aspen Capital's Software Engineer challenge. This assignment will help us better assess your technical and design skills. We recommend that you focus on the requirements listed below, and if time permitting, work on any additional features of your own choosing. These additional features can be new, functional pieces within the application, or even relevant design artifacts. It should be fun and highlight what you think your best skills are.

## File Structure
* The codebase contains two files which perform the following:
	* app.py : Main file that contains the logic
	* test.py : Three testcases for the logic in app.py

## How to Run Without Docker
* Install the required dependencies: To run the code, you'll need to have Python and Flask installed on your machine. You can install Flask and the other required dependencies by running the following command in your terminal:
	* pip install Flask Flask-SQLAlchemy

* Start the deployment server using this command: 
	* python app.py

* Test the endpoints: You can now test the endpoints using a tool like curl, or by opening them in a web browser. For example, you can start a game by sending a POST request to http://localhost:5000/start_game, and you can get lifetime wins by sending a GET request to http://localhost:5000/lifetime_wins. You can also reset the game using http://localhost:5000/reset_game

* Run the tests using the following command:
	* python3 test.py

## Output

* The output when going to the start_game URL will consists of a message for the game being run, with the trace of the different turns in the game, and the final winner.
* The lifetime_wins URL shows the statistics of the victories.

## How to Run With Docker
* Create the docker image with the following command:
	* docker build -t aspencapitalchallenge .
* Run the docker using the following command:
	* docker run -p 5000:5000 aspencapitalchallenge
* Go to http://127.0.0.1:5000/start_game or http://127.0.0.1:5000/lifetime_wins same as described above.


## Background

Your task is to implement an application that plays the card game of [War](https://en.wikipedia.org/wiki/War_(card_game))

Use the rules [here](https://bicyclecards.com/how-to-play/war/)

## Requirements

### High Level

* Create a RESTful service with two endpoints:

	* An endpoint to start a game. Two simulated players will play out the game.
	* An endpoint to get lifetime wins for each player stored in a database.

* You should include some basic tests along with the application code.

### Technical

* The service can be created in the language/framework of your choice. However, please do not reuse boilerplate
  code from another project as this makes it hard to see the pieces you have created which is a goal
  of this exercise.
* You can use any db technology you like.

Bonuses for providing:

* A Docker image or a link to a cloud deployment of the service.
* A simple UI showing the game being played.
* You can also implement variations of the basic game if you have time.

## Submission
* Your submission should be accessible in a public git repository that includes a README.md with all the pertinent information of how to run your application. 
The expectation is that we can easily follow the steps provided and run the application without any guesswork.
* If your submission does include additional artifacts that are not represented within the repository - the README should provide information on how to retrieve and access these items.

* Details on anything further that you would like to achieve given more time, including any trade-offs that you may have made.

Good luck and thank you for your time - we look forward to seeing your submission.

