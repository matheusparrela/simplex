import { Card, CardActionArea, CardActions, CardContent, Typography } from "@mui/material";
import styles from './Card.module.css';


export function Card2({ children }:any) {
  return (
    <Card className={styles.card}>
      <CardActionArea>

        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
            Inserir Dados 
          </Typography>
          <Typography variant="body2">
            <strong>Inserir os valores da Função na primeira linha. Depois preencha o sistemas com suas inequações</strong>
          </Typography>
        </CardContent>
      </CardActionArea>

      <CardActions style={{display:'block'}}>
        {children}
      </CardActions>
    </Card>
  )
}