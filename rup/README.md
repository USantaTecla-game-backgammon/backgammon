## Requirements

### Domain Model
![Domain Model](/rup/domain_model/domain_model.png)

### RULES
Estado inicial del tablero
```
|--------------------------------------------------------|
|  13  14  15  16  17  18 |    |  19  20  21  22  23  24 |
|  5●              3○     |    |  5○                  2● |
|                         |  0○|                         |
|                         | BAR|                         |
|                         |  0●|                         |
|  5○              3●     |    |  5●                  2○ |
|  12  11  10   9   8   7 |    |   6   5   4   3   2   1 |
|--------------------------------------------------------|
```

Mover en forma de herradura, y bajando posiciones 
```
Rojo mueve del 1 al 24 
Negro mueve del 24 al 1
```

Movimiento inválido 1: 
```
Si al mover una pieza acabas en una posición donde el 
otro jugador tiene 2 o más piezas
```

Movimiento inválido 2: 
```
Si sacas una pieza del tablero y no todas tus fichas están 
en el último cuadrante
```
Movimiento inválido 3: 
```
Si tienes piezas en BAR e intentas mover otra pieza que no está en el BAR
Si el movimiento de la pieza usado es menor al valor del dado y tienes 
otra ficha que pueda utilizar más movimiento
```


### Use Cases

![Use Cases](/rup/usecase/use_cases.png)

### Context

![Context](/rup/context/context.png)

### Start
![Start](/rup/usecase/start.png)

### MovePiece

RollDice is so similar to MovePiece

![MovePiece](/rup/usecase/move_piece.png)


### RejectBet
![RejectBet](/rup/usecase/reject_bet.png)

### Exit
![Exit](/rup/usecase/exit.png)

### GUI
![GUI](/rup/context/gui.png)

## Analysis

### Architecture
![Architecture](/rup/analysis/architecture.png)

#### Use Cases

#### Start
![Start](/rup/analysis/use_cases/start.png)

#### MovePiece
![MovePiece](/rup/analysis/use_cases/move_piece.png)

#### Bet
![Bet](/rup/analysis/use_cases/bet.png)
