import React from 'react';

type MonsterInfo = {
  name: string;
  hp: number;
  def: number;
};

interface MonsterProps {
  monster: MonsterInfo;
}

const MonsterSection: React.FC<MonsterProps> = ({ monster }) => {
  return (
    <div>
      <h2>{monster.name}</h2>
      <p>{monster.hp}</p>
      <p>{monster.def}</p>
    </div>
  );
};

export default MonsterSection;
