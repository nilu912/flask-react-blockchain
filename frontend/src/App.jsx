import { useState, useEffect } from "react";
import "./App.css";
import Block from "./components/Block";
import AddBlock from "./components/AddBlock";

function App() {
  const [chain, setChain] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchChain = () => {
      fetch("http://127.0.0.1:5000/get-chain/")
        .then((response) => response.json())
        .then((data) => {
          setChain(data.chain);
          setLoading(false);
        })
        .catch((error) => {
          console.error("Error fetching blockchain data: ", error);
          setLoading(false);
        });
    };
    fetchChain();
    const interval = setInterval(fetchChain, 5000);
    return () => clearInterval(interval);
  }, []);
  const addBlockData = (data) => {
    fetch("http://127.0.0.1:5000/transactions/new", {
      method: "POST",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        sender: data.sender,
        receiver: data.receiver,
        amount: data.amount,
      }),
    });
  };
  // if(!loading) return <h5>Blockchain data is loading...</h5>
  return (
    <>
      <h1 className="m-5">Hello world</h1>
      <AddBlock addBlockData={addBlockData} />
      <Block data={chain} />
    </>
  );
}

export default App;
