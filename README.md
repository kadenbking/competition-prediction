# competition-prediction

A Web App built with a Python Flask API and React Frontend to display outcome predictions using trained supervised learning models.

## Check it out!

To use the Web App, visit [competition-prediction](https://competition-prediction.netlify.app/).

## Supervised Learning Models

### Datasets

To train the models, datasets containing all 2021 MLB games, all NFL games between 2018-2021, and all NBA games from the 1940s to now were used with labels for `home_team`, `away_team`, and `result`. These massive datasets were necessary to ensure that the model had a basis for every possible matchup. To prevent the need for encoding the labels, teams were stored in the dataset by a unique `team_id` that could be translated into the team acronym through a python dictionary, and wins and losses were stored in the datasets as either `1` or `0`.

### Models

Multiple models were tested for each sport and were compared using metrics `accuracy_score`, `precision_score`, `recall`, and `computation_time`. Surpisingly, the DecisionTree performed better than the SVM or Neural Network in all three cases. Once the models were trained, they were saved as pickle files for integration into the API.

## Flask API

Flask API's are an easy way to deploy a Python backend. Python was the preferred language for the backend since all of the model work was also done in the same language. A `server.py` file defines endpoints and returns prediction scores for each league.

## React Frontend

The frontend was written in typescript using the Create React App boostrap template. The App is styled with Tailwind CSS.

## Run It Yourself

If you would like to run this project locally, clone the `dev` branch to your machine. Our code is split into 2 separate branches for the sake of live deployments with `main` being reserved for that purpose.

### Available Scripts

To run the API locally, navigate to the `backend` directory, and run `python3 server.py`. As you hit different endpoints, watch your terminal to view printed output from the various prediction tools.

To run the frontend locally, nagivate to the `frontend/cp-react` directory, and run `npm run start`. Each of the `fetch` statements on the `local` branch are using a proxy to connect to your locally run API.

### Statistical Simulation

On the `local` branch, there are an additional 2 endpoints available -- one for MLB and one for NBA. These two endpoints provide a more detailed prediction response than what is deployed live. These responses are generated through a statiscal simulation based on specific team stats. This is not an example of supervised learning, but a fun way to produce a winning percentage chance between two teams. Inspiration for the simulation was taken from [here](https://github.com/sidharthrajaram/CrystalBall).

## Learn More

To learn more about this project, check out this paper published [here](https://kadenbking.com/).

![alt text](https://github.com/kadenbking/competition-prediction/blob/main/frontend/cp-react/src/img/cp-logo.png?raw=true)
