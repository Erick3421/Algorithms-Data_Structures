from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["tom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["tom"] = []
graph["jonny"] = []

def people_is_seller(name):
    return name[-1] == 'm'

def search_seller(name):
    queue_search = deque()
    queue_search += graph[name]
    verified = []

    while queue_search:
        person = queue_search.popleft()
        if person not in verified:
            if people_is_seller(person):
                print(f"{person} is a seller of manga")
                return True
            else:
                queue_search += graph[person]
                verified.append(person)
    return False

search_seller("you")
