import { Card, CardActionArea, CardActions, CardContent, Typography } from "@mui/material";
import styles from './Card.module.css';


export function Card3({ children }:any) {
  return (
    <Card className={styles.card}>
      <CardActionArea>

        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
            Resultado 
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