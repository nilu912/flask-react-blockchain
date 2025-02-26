import React, { useState } from "react";

const AddBlock = (props) => {
  const [sender, setSender] = useState("");
  const [receiver, setReceiver] = useState("");
  const [amount, setAmount] = useState(0);

  const onFormSubmitHandler = async(e) => {
    e.preventDefault();
    const data = {sender,receiver,amount}
    // console.log(data)
    await props.addBlockData(data)
    console.log("form submitted..")
}
  return (
    <div>
      <form method="POST">
        <p>Enter sender name:</p>
        <input
          type="text"
          name="sender"
          placeholder="sender data"
          onChange={(e)=> setSender(e.target.value)}
          value={sender}
        />
        <p>Enter Receiver name:</p>
        <input
          type="text"
          name="receiver"
          placeholder="receiver data"
          onChange={(e)=> setReceiver(e.target.value)}
          value={receiver}
        />
        <p>Amount:</p>
        <input
          type="number"
          name="amount"
          placeholder="amount"
          onChange={(e)=>setAmount(e.target.value)}
          value={amount}
        />
        <button onClick={onFormSubmitHandler}>Click</button>
      </form>
    </div>
  );
};

export default AddBlock;
