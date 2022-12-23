import { Table } from "./Table";
import { CardLoader } from "./CardLoader";
import { Card3 } from './Card3';
import { Box, CircularProgress } from "@mui/material";
import { useEffect, useRef, useState } from "react";
import styles from './cardLoader.module.css';

export function PivotArray() {

  const [receivedData, setReceivedData] = useState<object[]>()

  const [load, setLoad] = useState(true);
  const intervalRef = useRef(null);

  const getData = async () => {
    const response = await fetch('./../../problem/data.json');
    const data = await response.json();
    
    if (data?.teste) {
    }
    else {
      setLoad(false)
      setReceivedData(data);
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
      <CardLoader>
          <Box>
          <div className={styles.loaderDescription}>
            <CircularProgress />
            <h2>Carregando Dados</h2>
          </div>
          </Box>
      </CardLoader>
    );
  }

  else {
    return (
      <Card3>
        <Table></Table>
      </Card3>
    )
  }
}

