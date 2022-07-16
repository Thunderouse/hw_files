from pprint import pprint
import os

file_name = "recipe.txt"


def file_reader(file_name):
    with open(file_name, "r", encoding='utf-8') as file_obj:
        global cookbook
        cookbook = {}
        for line in file_obj:
            dish_name = line.strip()
            ingredients = []
            for item in range(int(file_obj.readline())):
                ingredient = file_obj.readline().split(' | ')
                ingredients.append({'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]),
                                    'measure': ingredient[2].strip()})
            cookbook[dish_name] = ingredients
            file_obj.readline()
    return cookbook


dishes = file_reader(file_name)
pprint(dishes)
print()


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in cookbook:
            for ingredient in cookbook[dish]:
                if ingredient['ingredient_name'] in result:
                    result[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                else:
                    result[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                             'quantity': (ingredient['quantity'] * person_count)}
        else:
            print(f'Блюда "{dish}" нет в книге рецептов')
    return result


dishes_list = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
pprint(dishes_list)
print()



dir_name = "venv"
catalog_name = "task_3"
final_file_name = "final_file.txt"

base_path = os.getcwd()
dir_path = os.path.join(base_path, dir_name)
catalog_path = os.path.join(base_path, dir_name, catalog_name)
final_file_name_path = os.path.join(base_path, final_file_name)


def process_files(dir_path, catalog_path):
    files = os.listdir(catalog_path)
    files_data = {}
    for filename in files:
        if "%.txt" in filename:
            with open(os.path.join(catalog_path, filename), 'r', encoding='utf-8') as read_file:
                file_lines = read_file.readlines()
                count = len(file_lines)
                files_data[filename] = (count, file_lines)

            sorted_files_data = sorted(files_data.items(), key=count)
            with open(os.path.join(dir_path, final_file_name), 'w', encoding='utf-8') as write_file:
                write_file.write(sorted_files_data)

        else:
            print('В данном каталоге нет файлов с расширением .txt')


process_files(dir_path, catalog_path)
