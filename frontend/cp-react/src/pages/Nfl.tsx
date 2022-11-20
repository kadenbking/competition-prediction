import React, { useState, useEffect } from "react";
import Select, { StylesConfig } from "react-select";
import makeAnimated from "react-select/animated";
import { SpinnerRoundFilled } from "spinners-react";
import { Button } from "flowbite-react";
import { ThemeContext } from "../components/ThemeContext";
import { OptionType, OptionsType, Outcome } from "./../util/types";
import { nflTeams, nflLogos } from "../util/nfl";

function Nfl() {
  const { theme } = React.useContext(ThemeContext);
  const [spinning, setSpinning] = useState<boolean>(false);
  const [teamsList, setTeamsList] = useState<OptionsType>();
  const [homeTeam, setHomeTeam] = useState<OptionType>();
  const [awayTeam, setAwayTeam] = useState<OptionType>();
  const [outcome, setOutcome] = useState<Outcome>();

  useEffect(() => {
    getData();
  }, []);

  function getData() {
    const teamOptions: OptionsType = [];
    for (let i = 0; i < nflTeams.length; i++) {
      teamOptions.push({ label: nflTeams[i], value: i });
    }
    setTeamsList(teamOptions);
  }

  const animatedComponents = makeAnimated();
  const styles: StylesConfig = {
    menu: (styles) => ({
      ...styles,
      background: theme === "light" ? "white" : "#475569",
    }),
    control: (styles) => ({
      ...styles,
      width: "200px",
      margin: "1rem 0",
      background: theme === "light" ? "white" : "#475569",
    }),
    placeholder: (styles) => ({
      ...styles,
      color: theme === "light" ? "black" : "white",
    }),
    singleValue: (styles) => ({
      ...styles,
      color: theme === "light" ? "black" : "white",
    }),
  };

  function onChangeHomeTeam(option: OptionType | any) {
    setHomeTeam(option);
  }

  function onChangeAwayTeam(option: OptionType | any) {
    setAwayTeam(option);
  }

  function isDisabled() {
    if (homeTeam && awayTeam) {
      if (homeTeam.value !== awayTeam.value) {
        return false;
      }
    }

    return true;
  }

  function predict() {
    setSpinning(true);
    fetch(`/predict/nfl/${homeTeam?.label}/${awayTeam?.label}`)
      .then((res) => res.json())
      .then((data) => {
        setOutcome(data);
        setSpinning(false);
      });
  }

  function reset() {
    setSpinning(false);
    setHomeTeam(null);
    setAwayTeam(null);
    setOutcome(null);
  }

  return (
    <div className="min-h-screen flex flex-col items-center mt-32 text-black dark:text-white">
      <h1 className="my-5 text-2xl font-bold">NFL Game Predictor</h1>
      {spinning ? (
        <div className="mt-32">
          <SpinnerRoundFilled
            size={90}
            thickness={180}
            speed={70}
            color="rgba(57, 114, 172, 1)"
          />
        </div>
      ) : (
        <>
          {outcome ? (
            <div>
              <div className="relative my-20">
                <img
                  src={nflLogos[outcome.winningTeam]}
                  alt="team logo"
                  className="mx-auto w-72 md:w-96"
                />
              </div>
              <div>
                <p className="text-xl">
                  <span className="font-bold">{outcome.winningTeam}</span> has a{" "}
                  <span className="font-bold">{outcome.percentage}</span>%
                  chance to beat{" "}
                  <span className="font-bold">{outcome.losingTeam}</span>
                </p>
              </div>
              <div className="my-10 flex justify-center">
                <Button onClick={reset}>Reset</Button>
              </div>
            </div>
          ) : (
            <>
              <p className="my-5 max-w-sm md:max-w-xl mx-auto">
                Select a home and away team and click predict to see what
                percentage of a chance each team has to win a game against each
                other based on a trained supervised learning model.
              </p>
              <div className="flex flex-col md:flex-row items-center justify-center">
                <div className="m-4">
                  <h2 className="text-center font-bold">Choose Home Team</h2>
                  <Select
                    components={animatedComponents}
                    options={teamsList}
                    styles={styles}
                    onChange={onChangeHomeTeam}
                  />
                </div>
                <div className="m-4">
                  <h2 className="text-center font-bold">Choose Away Team</h2>
                  <Select
                    components={animatedComponents}
                    options={teamsList}
                    styles={styles}
                    onChange={onChangeAwayTeam}
                  />
                </div>
              </div>
              <div className="my-5">
                <Button onClick={predict} disabled={isDisabled()}>
                  Predict
                </Button>
              </div>
            </>
          )}
        </>
      )}
    </div>
  );
}

export default Nfl;
