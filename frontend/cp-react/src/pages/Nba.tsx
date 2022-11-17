import React, { useState, useEffect } from "react";
import Select, { StylesConfig } from "react-select";
import makeAnimated from "react-select/animated";
import { SpinnerRoundFilled } from "spinners-react";
import { Button } from "flowbite-react";
import { ThemeContext } from "../components/ThemeContext";
import { OptionType, OptionsType } from "./../util/types";
import { nbaTeams, nbaLogos } from "../util/nba";

function Nba() {
  const { theme } = React.useContext(ThemeContext);
  const [spinning, setSpinning] = useState<boolean>(false);
  const [teamsList, setTeamsList] = useState<OptionsType>();
  const [homeTeam, setHomeTeam] = useState<OptionType>();
  const [awayTeam, setAwayTeam] = useState<OptionType>();
  const [outcome, setOutcome] = useState<string>();

  useEffect(() => {
    getData();
  }, []);

  function getData() {
    const teamOptions: OptionsType = [];
    for (let i = 0; i < nbaTeams.length; i++) {
      teamOptions.push({ label: nbaTeams[i], value: i });
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
    fetch(`/predict/nba/${homeTeam?.label}/${awayTeam?.label}`)
      .then((res) => res.text())
      .then((text) => {
        setOutcome(text);
        setSpinning(false);
      });
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center text-black dark:text-white">
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
              <h2>{outcome}</h2>
              <img src={nbaLogos["OKC"]} alt="team logo" />
            </div>
          ) : (
            <>
              <div className="flex flex-row items-center justify-center">
                <div className="m-4">
                  <h2>Choose Home Team</h2>
                  <Select
                    components={animatedComponents}
                    options={teamsList}
                    styles={styles}
                    onChange={onChangeHomeTeam}
                  />
                </div>
                <div className="m-4">
                  <h2>Choose Away Team</h2>
                  <Select
                    components={animatedComponents}
                    options={teamsList}
                    styles={styles}
                    onChange={onChangeAwayTeam}
                  />
                </div>
              </div>
              <div>
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

export default Nba;
