import React, { useState, useEffect } from "react"
import { Card2 } from "./Card2";
import { Table } from "./Table";




export function PivotArray() {

  const [receivedData, newReceivedData] = useState([] as any)

  const getData = async () => {
    const response = await fetch('./../../problem/data.json');
    const data = await response.json();
    newReceivedData(data);
    console.log("no get", receivedData.base)
    const item = data;
  }

  useEffect(() => {
    getData();
  }, []);

  const renderData = () => {
    console.log("no render", receivedData.base)
  }
  console.log(receivedData)

  // {base, variable, table, erro, cb, z, artificial, pivo}



  return (
    <div>
      <Card2>
        <Table></Table>
      </Card2>
      {/* <button onClick={() => renderData()}></button> */}
      {/* <ul>
        {receivedData.map((rd: any) => (
          <>
            <li>{rd.base}</li>
            <li>{rd.variable}</li>
            <li>{rd.table}</li>
            <li>{rd.erro}</li>
            <li>{rd.z}</li>
            <li>{rd.artificial}</li>
            <li>{rd.pivo}</li>
          </>
        ))}</ul> */}
    </div>
  )
}

