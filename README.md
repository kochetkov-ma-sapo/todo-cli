# todo-cli

A tiny todo list for the terminal. Python 3, standard library only. Tasks live in a JSON file (`~/.todo.json`, override with `TODO_FILE`).

## Usage

```sh
python3 todo.py add Buy milk
python3 todo.py add Call the bank
python3 todo.py list
python3 todo.py done 1
python3 todo.py remove 2
```

Example `list` output:

```
  1 [x] Buy milk
  2 [ ] Call the bank
```
