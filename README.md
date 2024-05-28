## Set Game

A set is a group of cards such that for any given attribute each card has the same value for the attribute, or each card has a different value for the attribute.  


Assume each card has 4 attributes (shape, color, shade, number), each with 3 possible values.  Assume a set_size of 3.


Examples of valid sets: [“1111”, “2222”, “3333”], [“1111”, “2221”, “3331”]

Examples of invalid sets: [“1111”, “1222”, “3333”], [“1211”, “2221”, “3311”]


## Usage
- `pip install -r requirements.txt`
- `python main.py` or `python3 main.py`

## Tests
Valid Set 1:
```sh 
curl -X POST "http://127.0.0.1:8080/find_all_valid_sets"\
  -H "Content-Type: application/json"\
  -d '{
      "cards": 
          ["1111", "2222", "3333"]
      }'
```

Valid Set 2:
```sh 
curl -X POST "http://127.0.0.1:8080/find_all_valid_sets"\
  -H "Content-Type: application/json"\
  -d '{
      "cards": 
          ["1111", "2221", "3331"]
      }'
```

Invalid Set 1:
```sh 
curl -X POST "http://127.0.0.1:8080/find_all_valid_sets"\
  -H "Content-Type: application/json"\
  -d '{
      "cards": 
          ["1111", "1222", "3333"]
      }'
```

Invalid Set 2:
```sh 
curl -X POST "http://127.0.0.1:8080/find_all_valid_sets"\
  -H "Content-Type: application/json"\
  -d '{
      "cards": 
          ["1211", "2211", "3331"]
      }'
```


Bonus Valid Set:
Invalid Set 2:
```sh 
curl -X POST "http://127.0.0.1:8080/find_all_valid_sets"\
  -H "Content-Type: application/json"\
  -d '{
      "cards": 
          ["1231", "2211", "3221"]
      }'
```