from pathlib import Path

def get_cats_info(path):
    cats_list = []

    try:
        with open(path, "r", encoding="utf-8") as file:

            for line in file:
                line = line.strip()

                if not line:
                    continue

                cat_id, name, age = line.split(",")

                cat_dict = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats_list.append(cat_dict)

        return cats_list

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []

    except ValueError:
        print("Помилка у форматі даних.")
        return []

path = Path(__file__).parent / "cats_file.txt"

cats_info = get_cats_info(path)

print(cats_info)