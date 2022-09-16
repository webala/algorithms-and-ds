from collections import deque

def person_is_seller(name):
    if name[-1] == 'm':
        return True
    return False

graph = dict()
def search(name):
    search_queue = deque()
    searched = []
    search_queue += graph[name]

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print('{} is a mango seller'.format(person))
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    
    return False