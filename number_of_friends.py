def make_friends_graph(people, friends):
    # graph of friends (adjacency lists representation)
    G = {person: [] for person in people} # person -> direct friends list
    for a, b in friends:
        G[a].append(b) # a is friends with b
        G[b].append(a) # b is friends with a
    return G

def networks(num_people, friends):
    direct_friends = make_friends_graph(range(num_people), friends)
    seen = set() # already seen people

    # person's friendship circle is a person themselves 
    # plus friendship circles of all their direct friends
    # minus already seen people
    def friendship_circle(person): # connected component
        seen.add(person)
        yield person

        for friend in direct_friends[person]:
            if friend not in seen:
                yield from friendship_circle(friend)
                # on Python <3.3
                # for indirect_friend in friendship_circle(friend):
                #     yield indirect_friend

    # group people into friendship circles
    circles = (friendship_circle(person) for person in range(num_people)
               if person not in seen)

    # print friendship circles
    for i, circle in enumerate(circles):
        print("Social network %d is {%s}" % (i, ",".join(map(str, circle))))
        
networks(5, [(0,1),(1,2),(3,4)])
# -> Social network 0 is {0,1,2}
# -> Social network 1 is {3,4}


def networks(n,lst):
    groups = []
    for i in range(n):
        groups.append({i})
    for pair in lst:
        union = groups[pair[0]]|groups[pair[1]]
        for p in union:
            groups[p] = union
    sets = set()
    for g in groups:
        sets.add(tuple(g))
    i = 0
    for s in sets:
        print("network",i,"is",set(s))
        i+=1

print(networks(5,  [(0,1),(1,2),(3,4)]))
