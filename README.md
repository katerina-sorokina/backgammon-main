# Backgammon

## Description
API for calculating the number of points scored by the winner and the type of his victory for short backgammon
+ OIN - position of checkers at the end of the game, in which the loser has had time to throw away at least 1 checker, while the opponent has taken all of them off the board (counts as 1 point)
+ MARS - the position of checkers at the end of the game, in which the loser has not had time to move all his checkers into his house, while the opponent has moved all of them off the board (counts as 2 points)
+ KOKS - a situation in which the loser has not had time to remove one or more of his checkers from the enemy's home, or has left a checker on the bar while the opponent has removed all of his behind the board (counts as 3 points)


## Instalation
1. Clone the repository:

```
$ git clone https://github.com/kirylrachalovsky/backgammon.git
$ cd backgammon
```
2. Build docker containers:
```
$ docker-compose up -d
```

3.  Go to the docker container terminal:
```
$ docker exec -it backgammon /bin/sh
```

4. Running tests:
```
$ pytest app/tests/
```

5. To exit the container docker terminal, use the command
```
$ exit
```

6. Application started. Navigate to http://127.0.0.1:8000 (documents API is here)


## Endpoints

1. `POST` /api/v1/short-game/check-win-type : Defining the type of victory and scoring
```
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/short-game/check-win-type' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
        'board': {
            'bar_counts': {
                'player1_UUID': 0,
                'player2_UUID': 0,
            },
        "points": [
          {
            "number": 0,
            "checkers_count": 0,
            "occupied_by": "string"
          }
        ]
        },
        'start_position': {
            'player1_UUID': 0,
            'player2_UUID': 23,
        }
    }'
```

## Swagger
To test endpoints, you can use Swagger at http://127.0.0.1:8000/docs

Test data in the file [data_for_testing.txt](https://github.com/kirylrachalovsky/backgammon/blob/main/data_for_testing.txt)
