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
            Coloque o numero de variaveis de decisao e o numero de restricoes. Alem disso selecione 
          </Typography>
        </CardContent>
      </CardActionArea>
      <CardActions>
        <FormCreateProblem />
      </CardActions>
    </Card>
  );
}
