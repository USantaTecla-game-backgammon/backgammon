## Requirements

### Domain Model
![Domain Model](/rup/domain_model/domain_model.png)

![Board](/rup/images/board.jpg)

### RULES

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

![MovePiece](/rup/usecase/move_piece.png)

### RequestBet
![RequestBet](/rup/usecase/request_bet.png)

### ResponseBet
![ResponseBet](/rup/usecase/response_bet.png)

### RollDice
![RollDice](/rup/usecase/roll_dice.png)

### Exit
![Exit](/rup/usecase/exit.png)

### ShowMenu
![ShowMenu](/rup/usecase/show_menu.png)

### GUI

```
### BACKGAMMON ###

Each player should choose a color.

Define your goal? (1-64): 65
Define your goal? (1-64): 64

First roll: choosing first player ...
Player ●: 5
Player ○: 5

First roll: choosing first player ...
Player ●: 4
Player ○: 2

-- Starting new game --

|--------------------------------------------------------|
|  13  14  15  16  17  18 |    |  19  20  21  22  23  24 |
|  5●              3○     |    |  5○                  2● |
|                         |  0○|                         |
|                         | BAR|                         |
|                         |  0●|                         |
|  5○              3●     |    |  5●                  2○ |
|  12  11  10   9   8   7 |    |   6   5   4   3   2   1 |
|--------------------------------------------------------|
1) Move from point 24 to 22 (dice 2)
2) Move from point 24 to 20 (dice 4)
3) Move from point 13 to 11 (dice 2)
4) Move from point 13 to 9 (dice 4)
5) Move from point 8 to 6 (dice 2)
6) Move from point 8 to 4 (dice 4)
7) Move from point 6 to 4 (dice 2)
8) Move from point 6 to 2 (dice 4)
9) Exit

Select your choice: 1
|--------------------------------------------------------|
|  13  14  15  16  17  18 |    |  19  20  21  22  23  24 |
|  5●              3○     |    |  5○          1●      1● |
|                         |  0○|                         |
|                         | BAR|                         |
|                         |  0●|                         |
|  5○              3●     |    |  5●                  2○ |
|  12  11  10   9   8   7 |    |   6   5   4   3   2   1 |
|--------------------------------------------------------|
1) Move from point 24 to 20 (dice 4)
2) Move from point 22 to 18 (dice 4)
3) Move from point 13 to 9 (dice 4)
4) Move from point 8 to 4 (dice 4)
5) Move from point 6 to 2 (dice 4)

Select your choice: 1
|--------------------------------------------------------|
|  12  11  10   9   8   7 |    |   6   5   4   3   2   1 |
|  5○              3●     |    |  5●                  2○ |
|                         |  0○|                         |
|                         | BAR|                         |
|                         |  0●|                         |
|  5●              3○     |    |  5○  1●      1●         |
|  13  14  15  16  17  18 |    |  19  20  21  22  23  24 |
|--------------------------------------------------------|
1) RequestBet
2) RollDice
3) Exit

Select your choice: 1

1) ResponseBet accept
2) ResponseBet reject
3) Exit

Select your choice: 1

|--------------------------------------------------------|
|  12  11  10   9   8   7 |    |   6   5   4   3   2   1 |
|  5○              3●     |    |  5●                  2○ |
|                         |  0○|                         |
|                         | BAR|                         |
|                         |  0●|                         |
|  5●              3○     |    |  5○  1●      1●         |
|  13  14  15  16  17  18 |    |  19  20  21  22  23  24 |
|--------------------------------------------------------|
1) RollDice
2) Exit

Select your choice: 2

### BYE ###
```

## Analysis

### Architecture
![Architecture](/rup/analysis/architecture.svg)

#### Use Cases

#### Start
![Start](/rup/analysis/use_cases/start.png)

### MovePiece
![MovePiece](/rup/analysis/use_cases/move_piece.png)

### RequestBet
![RequestBet](/rup/analysis/use_cases/request_bet.png)

### ResponseBet
![ResponseBet](/rup/analysis/use_cases/response_bet.png)

### RollDice
![RollDice](/rup/analysis/use_cases/roll_dice.png)

### Exit
![Exit](/rup/analysis/use_cases/exit.png)

### ShowMenu
![ShowMenu](/rup/analysis/use_cases/show_menu.png)
