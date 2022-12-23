import { Card, CardActionArea, CardActions, CardContent, Typography } from "@mui/material";
import styles from './cardLoader.module.css';


export function CardLoader({ children }:any) {
  return (
    <Card className={styles.card}>
      <CardActionArea>

        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
            <h2>Gerando solução do Problema </h2>
          </Typography>
          <Typography variant="body2">
            <strong></strong>
          </Typography>
        </CardContent>
      </CardActionArea>

      <CardActions style={{display:'block'}}>
        {children}
      </CardActions>
    </Card>
  )
}