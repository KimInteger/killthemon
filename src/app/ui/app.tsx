import React, { useState } from 'react';
import PlayerSection from './player/playerSection';

const App: React.FC = () => {
  const [player, setPlayer] = useState({
    name: 'player',
    hp: 100,
    atk: 20,
  });

  const [monster, setMonster] = useState({
    name: 'monster',
    hp: 200,
    def: 10,
  });

  function attack() {
    setMonster((prevMonster) => ({
      ...prevMonster,
      hp: prevMonster.hp - Math.max(player.atk - prevMonster.def, 0),
    }));
  }

  return (
    <>
      <h1>몬스터를 죽여라!</h1>
      <PlayerSection player={player} attack={attack} />
    </>
  );
};

export default App;
