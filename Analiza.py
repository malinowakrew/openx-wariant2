# Wykorzystywana biblioteka
import pandas as pd

def merge(df1, df2, str):
    return pd.merge(df1, df2, on=str, how='outer')


def author_count(data):
    posts_number = data.value_counts()
    str_list = []
    for number, name in enumerate(posts_number.index):
        str_list.append(str(name) + " napisała(a) " + str(posts_number.iloc[number]) + " postów")
    return(str_list)


def unique_titles(data):
    if data.is_unique == True:
        return("Tytuły są unikalne")
    else:
        duplicates = data.duplicated()
        duplicates_list = list(data[duplicates].unique())
        return duplicates_list


def neighbour(data):
    the_clost = []
    for number, address in enumerate(data):
        close_value = 36000
        close_number = number
        lat = float((address["geo"])["lat"])
        lng = float((address["geo"])["lng"])

        for number2, address2 in enumerate(data):
            if number != number2:
                i = (lat - float((address2["geo"])["lat"])) ** 2 + (lng - float((address2["geo"])["lng"])) ** 2
                if close_value > i:
                    close_value = i
                    close_number = number2

        the_clost.append(close_number)

    return(the_clost)

def neighbour_connestion(data, numbers_list, column_name):
    neighbours_names = []
    for number in numbers_list:
        neighbours_names.append(data["username"].iloc[number])

    data[column_name] = pd.Series(neighbours_names)
    return(data)

def main():
    # Pobieramy dane
    data_users = pd.read_json("https://jsonplaceholder.typicode.com/users")
    data_posts = pd.read_json("https://jsonplaceholder.typicode.com/posts")

    # Zmienimy nazwy kolumn w tabeli, tak aby było możliwe połączenie ich na podstawie tego samego klucza ("id").
    data_posts_rename = data_posts.rename(columns={'id': 'post_id', 'userId': 'id'})

    # Połączenie
    data = merge(data_users, data_posts_rename, 'id')

    # Policzenie ilości postów danego autora
    authors = author_count(data["username"])
    # Wyświetlanie
    for item in authors:
        print(item)

    # Sprawdzenie unikalności i zwrot duplikatów
    duplicated_titles = unique_titles(data["title"])
    # Wyświetlanie
    if str(type(duplicated_titles)) == "<class 'str'>":
        print(duplicated_titles)
    else:
        for item in duplicated_titles:
            print(item)

    # Znajdowanie sąsiada i dodawanie go do tabeli data_users
    # Każdy element kolumny address jest słownikiem
    result = neighbour(data_users["address"])
    # Wyświetlanie
    data_with_neighbours = neighbour_connestion(data_users, result, "neighbour")
    print(data_with_neighbours)


if __name__ == "__main__":
    main()