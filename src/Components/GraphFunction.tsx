import { Card3 } from "./Card3";
import styles from './GraphFunction.module.css';
import Graph from './../../scripts/figure/graph.png';
import { useEffect, useState } from "react";

export function GraphFunction() {
  
  const [receivedData, newReceivedData] = useState([] as any)

  const getData = async () => {
    const response = await fetch('./../../problem/nicePoint.json');
    const data = await response.json();
    newReceivedData(data);
    const item = data;
  }

  useEffect(() => {
    getData();
  }, []);
  
 
  return (
    <div>
  
      <div className={styles.divText}>
        <strong style={{ color: '#1C724B' }}>Ponto Ótimo:</strong>
        {receivedData != undefined && receivedData.map((item: any) => (
          <label ><strong> X1:{item.solution.X1}    X2:{item.solution.X2}   X3:{item.solution.X3} </strong></label>
        ))
        }
      </div>
      <div className={styles.divText}>
        <strong style={{ color: '#1C724B' }}>Valor Otimo: </strong>
        {receivedData != undefined && receivedData.map((item: any) => (
          <label ><strong>{item.solution.Z}</strong></label>
        ))
        }
        <img src={Graph} className={styles.img} />
      </div>
    </div>
  );
}