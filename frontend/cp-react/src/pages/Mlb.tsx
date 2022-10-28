import React, { useState, useEffect } from "react";

function Mlb() {
  const [teamsList, setTeamsList] = useState<string[]>();

  useEffect(() => {
    getData();
  }, []);

  function getData() {
    fetch("/mlb")
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        setTeamsList(data);
      });
  }

  const listItems = teamsList?.map((team) => (
    <li className="text-2xl text-black dark:text-white" key={team.toString()}>
      {team}
    </li>
  ));

  return (
    <div className="min-h-screen flex flex-col lg:flex-row items-center justify-center">
      <ul>{listItems}</ul>
    </div>
  );
}

export default Mlb;
