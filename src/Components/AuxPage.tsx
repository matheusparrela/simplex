import { useEffect, useRef, useState } from "react";
import { Card3 } from "./Card3";
import { Box, CircularProgress } from "@mui/material";
import { GraphFunction } from "./GraphFunction";


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
        <Card3>
          <Box>
            <CircularProgress />
            <h2>Carregando Dados</h2>
          </Box>
        </Card3>

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