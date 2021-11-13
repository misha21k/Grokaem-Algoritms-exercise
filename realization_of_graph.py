from collections import deque


def person_is_seller(name):
    return len(name) == 4  # Пусть, если длина имени равна 4, то это продавец манго


def search(name):
    search_queue = deque()  # Создание новой очереди
    search_queue += graph[name]  # Все соседи добавляются в очередь
    searched = set()
    while search_queue:  # Пока очередь не пуста...
        person = search_queue.popleft()  # Из очереди извлекается первый человек
        if person not in searched:
            if person_is_seller(person):  # Проверяем, яляется ли этот человек продавцом манго
                print(person + " is a mango seller!")  # Да, это продавец манго
                return True
            else:
                search_queue += graph[person]  # Нет, не является. Все друзья этого человека добавляются в очередь
                searched.add(person)
    return False  # Если выполнение дошло до этой строки, значит, в очереди нет продавца манго


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search("you")
