import React, { useState, useEffect } from "react";
import Select, { StylesConfig } from "react-select";
import makeAnimated from "react-select/animated";
import { SpinnerRoundFilled } from "spinners-react";
import { Button } from "flowbite-react";
import { ThemeContext } from "../components/ThemeContext";
import { OptionType, OptionsType } from "./../util/types";
import { nflTeams, nflLogos } from "../util/nfl";
import frame from "../img/cp-frame.png";

function Nfl() {
  const { theme } = React.useContext(ThemeContext);
  const [spinning, setSpinning] = useState<boolean>(false);
  const [teamsList, setTeamsList] = useState<OptionsType>();
  const [homeTeam, setHomeTeam] = useState<OptionType>();
  const [awayTeam, setAwayTeam] = useState<OptionType>();
  const [outcome, setOutcome] = useState<string>("w");

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
      .then((res) => res.text())
      .then((text) => {
        setOutcome(text);
        setSpinning(false);
      });
  }

  return (
    <div className="min-h-screen flex flex-col items-center mt-32 text-black dark:text-white">
      <h1 className="my-5 text-2xl font-bold">NFL Game Predictor</h1>
      {spinning ? (
        <div>
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
                  src={nflLogos["KCC"]}
                  alt="team logo"
                  className="relative mx-auto w-56 md:w-72"
                />
                <div className="absolute top-0 w-60 md:w-80">
                  <img
                    src={frame}
                    alt="crystal ball"
                    className="-mx-14 md:-mx-24 -mt-20"
                  />
                </div>
              </div>
              <div>
                <p className="mt-72">
                  <span>{homeTeam?.label}</span> has a <span>{outcome}</span>{" "}
                  chance to beat <span>{awayTeam?.label}</span>
                </p>
              </div>
            </div>
          ) : (
            <>
              <p className="my-5 max-w-md md:max-w-xl">
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
