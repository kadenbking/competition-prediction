import React from "react";
import { Navbar } from "flowbite-react";
import { ThemeContext } from "./ThemeContext";
import { FaSun, FaMoon } from "react-icons/fa";
import logo from "./../img/cp-logo.png";

function Nav() {
  const { theme, setTheme } = React.useContext(ThemeContext);

  return (
    <Navbar fluid={true} rounded={false}>
      <Navbar.Brand href="/">
        <img src={logo} className="mr-3 h-6 sm:h-9" alt="Flowbite Logo" />
        <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">
          Competition Prediction
        </span>
      </Navbar.Brand>
      <Navbar.Toggle />
      <Navbar.Collapse>
        <Navbar.Link href="/mlb" className="text-lg align-middle">
          MLB
        </Navbar.Link>
        <Navbar.Link href="/nba" className="text-lg align-middle">
          NBA
        </Navbar.Link>
        <Navbar.Link href="/nfl" className="text-lg align-middle">
          NFL
        </Navbar.Link>
        <Navbar.Link
          onClick={() => {
            setTheme(theme === "dark" ? "light" : "dark");
          }}
        >
          <div className="transition duration-500 ease-in-out rounded-full mt-1 align-middle">
            {theme === "dark" ? (
              <FaSun className="text-white text-xl cursor-pointer" />
            ) : (
              <FaMoon className="text-black text-xl cursor-pointer" />
            )}
          </div>
        </Navbar.Link>
      </Navbar.Collapse>
    </Navbar>
  );
}

export default Nav;
