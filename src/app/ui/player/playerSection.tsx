import React, { useState } from 'react';

type PlayerInfo = {
  name: string;
  hp: number;
  atk: number;
};

interface PlayerProps {
  player: PlayerInfo;
  attack: () => void;
}

const PlayerSection: React.FC<PlayerProps> = ({ player, attack }) => {
  return (
    <div>
      <h2>{player.name}</h2>
      <p>{player.hp}</p>
      <p>{player.atk}</p>
      <button onClick={attack}>공격!!</button>
    </div>
  );
};

export default PlayerSection;
