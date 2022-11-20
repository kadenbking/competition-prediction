import React from "react";
import { Routes, Route, BrowserRouter } from "react-router-dom";
import Nav from "./Nav";
import Footer from "./Footer";
import Home from "../pages/Home";
import Mlb from "../pages/Mlb";
import Nba from "../pages/Nba";
import Nfl from "../pages/Nfl";
import PageNotFound from "../pages/PageNotFound";

function App() {
  return (
    <BrowserRouter>
      <div className="transition-all bg-slate-300 dark:bg-slate-700">
        <Nav />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/mlb" element={<Mlb />} />
          <Route path="/nba" element={<Nba />} />
          <Route path="/nfl" element={<Nfl />} />
          <Route path="/404" element={<PageNotFound />} />
          <Route path="*" element={<PageNotFound />} />
        </Routes>
        <Footer />
      </div>
    </BrowserRouter>
  );
}

export default App;
