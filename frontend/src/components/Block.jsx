import React from "react";

const Block = (props) => {
  console.log(props);
  return (
    <div>
      {props.data.map((block) => {
        return (
          <div key={block.index}>
            <p>{block.index}</p>
            <p>{block.hash}</p>
            <p>{block.previous_hash}</p>
          </ div>
        );
      })}
    </div>
  );
};

export default Block;
