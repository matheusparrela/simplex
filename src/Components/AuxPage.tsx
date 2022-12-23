import { useEffect, useRef, useState } from "react";
import { Card3 } from "./Card3";
import { Box, CircularProgress } from "@mui/material";
import { GraphFunction } from "./GraphFunction";
import { CardLoader } from "./CardLoader";
import styles from './cardLoader.module.css';


export function AuxPage() {
  const [receivedData, newReceivedData] = useState<Object>()
  const [load, setLoad] = useState(true);

  const intervalRef = useRef(null);

  const getData = async () => {
    const response = await fetch('./../../problem/functionGraph.json');

    const data = await response.json();
    if (data?.test) {

    }
    else {
      setLoad(false)
      newReceivedData(data);
    }
  }

  useEffect(() => {
    intervalRef.current = setInterval(() => getData(), 3000)

    if (!load) {
      clearInterval(intervalRef.current)
      intervalRef.current = null
    }
  }, [load]);

  if (load) {

    return (
      <div>
        <CardLoader>
          <Box>
          <div className={styles.loaderDescription}>
            <CircularProgress />
            <h2>Carregando Dados</h2>
          </div>
          </Box>
      </CardLoader>
      </div>
    );
  }

  else {
    return (
      <Card3>
        <GraphFunction></GraphFunction>
      </Card3>
    )
  }
}