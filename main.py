from typing import List
from itertools import combinations
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# This is a Pydantic model to define the input request body.
# Models can be placed in a different directory in a more complicated application/structure.
class CardsDto(BaseModel):
    cards: List[str]
    # set_size: int  # We could pass in set size to make this more modular - following instructions to assume set size of 3.


# Method checks to make sure the list of cards are a valid set.
def is_valid(cards: List[str]) -> bool:
    # Check if all cards have the same or all different values for each attribute
    for i in range(4):  # Assuming each card has 4 attributes (shape, color, shade, number)
        card_values = [card[i] for card in cards]
        if len(set(card_values)) != 1 and len(set(card_values)) != len(cards):  # If any fail, it is not a valid set
            return False
    return True  # All passed, this is a valid set


@app.post("/find_all_valid_sets")
def find_all_sets(request: CardsDto):
    # Get the data from the request object (CardsDto)
    cards = request.cards
    set_size = 3  # Directions said to assume a set size of 3
    possible_combinations = combinations(cards, set_size)  # Generate all possible unique combinations
    valid_sets = [list(combination) for combination in possible_combinations if is_valid(combination)]  # Creates a list with valid sets
    return {
        "sets": valid_sets
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)  # Start the FastAPI application and make it accessible at http://0.0.0.0:8080.
