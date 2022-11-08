import React, { useState, useEffect } from "react";
import Select, { StylesConfig } from "react-select";
import makeAnimated from "react-select/animated";
import { Button } from "flowbite-react";
import { ThemeContext } from "../components/ThemeContext";
import { OptionType, OptionsType } from "./../util/types";

function Mlb() {
  const { theme } = React.useContext(ThemeContext);
  const [teamsList, setTeamsList] = useState<OptionsType>();
  const [homeTeam, setHomeTeam] = useState<OptionType>();
  const [awayTeam, setAwayTeam] = useState<OptionType>();
  const [run, setRun] = useState<boolean>(false);

  useEffect(() => {
    getData();
  }, []);

  function getData() {
    const teamOptions: OptionsType = [];
    fetch("/mlb")
      .then((res) => res.json())
      .then((data) => {
        for (let i = 0; i < data.length; i++) {
          teamOptions.push({ label: data[i], value: i });
        }
        setTeamsList(teamOptions);
      });
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

  function predict() {
    if (homeTeam && awayTeam) {
      setRun(true);
    }
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center text-black dark:text-white">
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
        <Button onClick={predict}>Predict</Button>
        {run ? (
          <div>
            <span>{homeTeam?.label}</span>
            <span>vs</span>
            <span>{awayTeam?.label}</span>
          </div>
        ) : (
          <></>
        )}
      </div>
    </div>
  );
}

export default Mlb;

// const listItems = teamsList?.map((team) => (
//   <li
//     className={`text-2xl text-black p-2 m-2 bg-${mlbTeamColors[team]}-400`}
//     key={team.toString()}
//   >
//     {team}
//   </li>
// ));
