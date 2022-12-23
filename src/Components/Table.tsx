import { useEffect, useRef, useState } from 'react';
import styles from './table.module.css'


export function Table() {
  const [receivedData, setReceivedData] = useState<object[]>()
  const [nicePoint, setNicePoint] = useState<object[]>()

  const getData = async () => {
    const response = await fetch('./../../problem/data.json');
    const data = await response.json();
    setReceivedData(data);
  }

  const getDataNicePoint = async () => {
    const response = await fetch('../../../problem/nicePoint.json');
    const dataNicePoint = await response.json();
    setNicePoint(dataNicePoint);
  }

  useEffect(() => {
    getData();
    getDataNicePoint();
  }, []);


  return (

    <div>
      <div className={styles.divText}>
        <strong style={{ color: '#1C724B' }}>Ponto Ótimo:</strong>
        {nicePoint != undefined && nicePoint.map((item: any) => (
          <label ><strong> X1:{item.solution.X1}    X2:{item.solution.X2}   X3:{item.solution.X3} </strong></label>
        ))
        }
      </div>
      <div className={styles.divText}>
        <strong style={{ color: '#1C724B' }}>Valor Otimo: </strong>
        {nicePoint != undefined && nicePoint.map((item: any) => (
          <label ><strong>{item.solution.Z}</strong></label>
        ))
        }
      </div>
      <div className={styles.goodPoint}>
        {receivedData != undefined && receivedData.map((item: any) => (
          item.erro !== '' && <strong>Não foi possível encontrar a solução inteira </strong>
        ))
        }

      </div>
      {receivedData != undefined && receivedData.map((rd: any) => (
        rd.erro !== '' && <p>{rd.erro}</p>
      ))}


      <div>
        {receivedData != undefined && receivedData.map((rd: any) => (
          <div className={styles.tableContainer}>
            <table className={styles.table}>
              <thead>
                <td>Table 1</td>
                <td></td>
                <td></td>
                {
                  (rd.z).map((item: string) => (
                    <td>{item}</td>
                  ))
                }
                <tr>
                  <th>BASE</th>
                  {
                    (rd.variable).map((item: string) => (
                      <th>{item}</th>
                    ))
                  }
                </tr>
              </thead>
              <tbody>
                <tr>
                </tr>
                {
                  (rd.base).map((item: string, index: number) => (
                    <tr>
                      <td>{item}</td>
                      {
                        rd.table[index].map((subItem: any, indexNumber: number) => (
                          index == (rd.pivo[0]) && indexNumber == (rd.pivo[1]) ? <td style={{ backgroundColor: '#7890a8', color: 'white' }}>{subItem}</td>
                            : <td>{subItem}</td>
                        ))
                      }
                    </tr>
                  ))
                }
                <td>Z</td>
                <td></td>
                {
                  rd.table[rd.table.length - 1].map((value: any) => (
                    <td>{value}</td>
                  ))
                }
              </tbody>
            </table>
          </div>
        ))}
      </div>
    </div>
  );
}

