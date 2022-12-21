import { TextField, Button } from "@mui/material";
import { FormEvent, useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import styles from './formCreateProblem.module.css';

import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormLabel from '@mui/material/FormLabel';

import { useContextProblem } from "../context/ProblemContentex";
import { green } from "@mui/material/colors";
// import {useHistory} from 'react-router-dom';



interface IDataProblem {
  numberVariable: number,
  numberConstraints: number,
  method: string,
  option: string,
  type: string
}

export function FormCreateProblem() {
  const [dataProblem, SetNewDataProblem] = useState<IDataProblem>({} as any)

  const object = useContextProblem()
  const history = useNavigate()

  async function postData() {
    fetch('http://localhost:3000/dataProblem', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: `{
              "numberVariable": ${dataProblem.numberVariable},
              "numberConstraints": ${dataProblem.numberConstraints},
              "method": ${dataProblem.method},
              "option": ${dataProblem.option}
            }`
    }).then(data => data.json())
  }

  function handleCreateNewData(event: FormEvent) {
    event.preventDefault();
    object.setData(dataProblem)
    history('/GenerateProblem')
  }

  async function loadData() {
    const response = await fetch('http://localhost:3000/dataProblem');
    const data = await response.json();

    SetNewDataProblem(data);
  }

  const handleNewDataChange = (event: any) => {
    SetNewDataProblem({ ...dataProblem, [event.target.name]: event.target.value })
  }

  return (
    <div>
      <form onSubmit={handleCreateNewData} className={styles.form} action="">
        <div className={styles.number}>
          <div className={styles.inputRadio}>
            <div className={styles.FormLabel}>
              <FormLabel id="demo-row-radio-buttons-group-label">Método</FormLabel>
              <RadioGroup
                row
                aria-labelledby="demo-row-radio-buttons-group-label"
                name="method"
                value={dataProblem?.method}
                onChange={handleNewDataChange}
              >
                <FormControlLabel value="Maximizar" control={<Radio sx={{
                  color: 'green',
                  '&.Mui-checked': {
                    color: 'green',
                  },
                }} />} label="Maximizar" />
                <FormControlLabel value="Minimizar" control={<Radio sx={{
                  color: 'green',
                  '&.Mui-checked': {
                    color: 'green',
                  },
                }} />} label="Minimizar" />
              </RadioGroup>
            </div>

            <div className={styles.FormLabel}>
              <FormLabel id="demo-row-radio-buttons-group-label" >Objetivo</FormLabel>
              <RadioGroup
                row
                aria-labelledby="demo-row-radio-buttons-group-label"
                name="option"
                color="success"
                value={dataProblem?.option}
                onChange={handleNewDataChange}

              >
                <FormControlLabel value="Primal" control={<Radio sx={{
                  color: 'green',
                  '&.Mui-checked': {
                    color: 'green',
                  },
                }} />} label="Primal" />
                <FormControlLabel value="Dual" control={<Radio sx={{
                  color: 'green',
                  '&.Mui-checked': {
                    color: 'green',
                  },
                }} />} label="Dual" />
              </RadioGroup>
            </div>
            <div className={styles.FormLabel}>
              <FormLabel id="demo-row-radio-buttons-group-label">Objetivo2</FormLabel>
              <RadioGroup
                row
                aria-labelledby="demo-row-radio-buttons-group-label"
                name="type"
                color="success"
                value={dataProblem?.type}
                onChange={handleNewDataChange}
              >
                <FormControlLabel value="Tabular" control={<Radio sx={{
                  color: 'green',
                  '&.Mui-checked': {
                    color: 'green',
                  },
                }} />} label="Tabular" />
                <FormControlLabel value="Graph" control={<Radio sx={{
                  color: 'green',
                  '&.Mui-checked': {
                    color: 'green',
                  },
                }} />} label="Graph" />
              </RadioGroup>
            </div>
          </div>
          <div className={styles.inputText}>
            <TextField
              name="numberVariable"
              value={dataProblem?.numberVariable}
              onChange={handleNewDataChange}
              id="numberVariable"
              label="Numero de Variaveis de Decisao"
              type='number'
              color="success"
              focused
              required
            />
            <TextField
              name="numberConstraints"
              value={dataProblem?.numberConstraints}
              onChange={handleNewDataChange}
              id="numberConstraints"
              label="Numero de Variaveis de Restricao"
              type='number'
              color="success"
              focused
              required
            />
          </div>
        </div>
        <footer>

          <Button type="submit" variant="contained" color="success">
            Continuar
          </Button>
        </footer>
      </form>
    </div>
  );
}