import json
from typing import Union


def get_sound(animal: str) -> str:

    """Function defines key which need to take value"""

    sounds: dict[str, str] = {
                        "dog": "bark",
                        "cat": "meow",
                        "cow": "moo",
                        "rat": "pipi",
                        "alien": "KILL",
                        }

    return sounds.get(animal, None)


def take_animal(json_file: str) -> Union[str, None]:

    '''Checks and works with json file'''

    try:

        with open(f'{json_file}', 'r', encoding='utf-8') as data:

            result: list[str] = []

            animal_data_list: dict[str, str] = json.load(data)
            
            if animal_data_list:

                for animal_data in animal_data_list:

                    animal: str = animal_data.get('animal')

                    result.append(get_sound(animal=animal))

            else:

                return print("Data doesn't contain an animal")

        return print(result)

    except FileNotFoundError:

        print("File was not found")

        return None

    except json.JSONDecodeError:

        print("File Decoding error was occured")

        return None


if __name__ == "__main__":

    take_animal('json_full.json')
