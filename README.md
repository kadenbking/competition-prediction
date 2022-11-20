# competition-prediction

A Web App built with a Python Flask API and React Frontend to display outcome predictions using statiscal simulations and trained supervised learning models.

## Check it out!

To use the Web App, visit [competition-prediction](https://competition-prediction.netlify.app/).

## Supervised Learning Models

Predictions for MLB and NFL games are both the result of trained supervised learning models. 

### Datasets

To train the MLB model, a dataset containing all 2021 MLB games with labels for `home_team`, `away_team`, and `result` was used. To train the NFL model, a dataset containing all NFL games from 2018-2021 with labels `home_team`, `away_team`, and `result` was used. These massive datasets were necessary to ensure that the model had a basis for every possible matchup. To prevent the need for encoding the labels, MLB and NFL teams were stored in the dataset by a unique `team_id` that could be translated into the team acronym through a python dictionary, and wins and losses were stored in the datasets as 1's and 0's.

### Models

Lorem Ipsum...

### Statistical Simulation

To predict NBA games, a statistical simulation using a custom team metric based on specific team stats was used. This is not AI or ML necessarily, but a fun way to produce a percentage one team has to beat another. 

## Flask API

Flask API's are an easy way to deploy a Python backend. Using a Python backend was easier since all of the model and statistical simulation work was also written in Python. A `seerver.py` file defines endpoints and return data -- which is an object containing `winningTeam`, `losingTeam` and the `percentage` that the winning team has to win.

### Available Scripts

To run the API locally, clone this repo, navigate to the `backend` directory, and run `python3 server.py`. As you hit different endpoints, watch your terminal to view printed output from the various prediction tools.

## React Frontend

The frontend was written in typescript using the Create React App boostrap template. The App is styled with Tailwind CSS.

### Available Scripts

To run the frontend locally, clone this repo, nagivate to the `frontend/cp-react` directory, and run `npm run start`. If you want the frontend to display results from the Flask API being run locally instead of the one deployed, clone this repo from the `local` branch instead of `main`.

## Learn More

To learn more about this project, check out this paper published [here](https://kadenbking.com/).

![alt text](https://github.com/kadenbking/competition-prediction/blob/main/frontend/cp-react/src/img/cp-logo.png?raw=true)
