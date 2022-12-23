import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import {  CardActionArea, CardActions } from '@mui/material';
import { FormCreateProblem } from './FormCreateProblem';
import styles from './Card.module.css';


export  function CardProblem() {
  return (
    <Card className={styles.card}>
      <CardActionArea>
        
        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
            Gerar Problema
          </Typography>
          <Typography variant="body2">   
            <strong style={{marginBottom: "0.5rem"}}> Coloque o número de variáveis de decisão e o número de restrições. Além disso selecione o método a função </strong>
            <br /> objetivo
            e o modo da tabela.
            <br/> Obs: Ao selecionar o modo Graph lembre que o maior valor para as variáveis de decisão é 2! 
          </Typography>
        </CardContent>
      </CardActionArea>
      <CardActions>
        <FormCreateProblem />
      </CardActions>
    </Card>
  );
}
