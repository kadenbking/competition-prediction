import React from "react";
import logo from "./../img/cp-logo.png";

function Home() {
  return (
    <div className="min-h-screen flex flex-col lg:flex-row items-center justify-center">
      <header className="App-header">
        <img
          src={logo}
          alt="Competition Prediction Logo"
          className="w-56 my-5 mx-auto"
        />
        <p className="text-3xl font-bold text-black dark:text-white">
          Competition Prediction
        </p>
      </header>
    </div>
  );
}

export default Home;
