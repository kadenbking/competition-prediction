import React from "react";
import logo from "./../img/cp-logo.png";

function Home() {
  return (
    <div className="min-h-screen flex flex-col lg:flex-row justify-center text-black dark:text-white">
      <header className="my-32">
        <img
          src={logo}
          alt="Competition Prediction Logo"
          className="w-60 my-5 mx-auto"
        />
        <h1 className="text-3xl text-center my-20 font-bold">
          Welcome to Competition Prediction!
        </h1>
        <p className="max-w-sm md:max-w-xl my-5 mx-auto">
          Competition Prediction is a simple web app that uses trained
          supervised learning models to predict outcomes of MLB, NBA, and NFL
          games.
        </p>
        <p className="max-w-sm md:max-w-xl my-5 mx-auto">
          Select your sport of choice, home team, and away team to see
          predictions for any combination of teams.
        </p>
        <p className="max-w-sm md:max-w-xl my-5 mx-auto">
          To learn more about how the predictor works, visit the repository
          below and check out the README.md and published paper.
        </p>
      </header>
    </div>
  );
}

export default Home;
