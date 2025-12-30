from dataclasses import dataclass
from math import hypot


@dataclass
class Vertex:
    id: int
    x: float
    y: float
    z: float

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        return False


def parse_input(file_name: str):
    boxes = []
    with open(file_name) as f:
        lines = f.readlines()
        id = 0
        for line in lines:
            coords = line[:-1].split(",")
            x, y, z = map(int, coords)
            boxes.append(Vertex(id, x, y, z))
            id += 1

    return boxes


def get_distance(point1: Vertex, point2: Vertex) -> float:
    return hypot(point1.x - point2.x, point1.y - point2.y, point1.z - point2.z)


def get_n_closest_connections(distances, jboxes: list[Vertex], n: int):
    jbox_conns = {}
    for jbox in jboxes:
        jbox_conns[jbox.id] = []

    if n > len(distances):
        raise Exception(
            f"Provided n {str(n)} too large. Maximum allowed value: {len(distances)}"
        )

    for i in range(0, n):
        point1 = distances[i]["point1"]
        point2 = distances[i]["point2"]
        jbox_conns[point1.id].append(point2.id)
        jbox_conns[point2.id].append(point1.id)

    return jbox_conns


def dfs(jbox_conns, curr_v_id: int, visited: list[int], sub_graph: list[int]):
    visited.append(curr_v_id)
    sub_graph.append(curr_v_id)
    for neighbour in jbox_conns[curr_v_id]:
        if neighbour in visited:
            continue
        dfs(jbox_conns, neighbour, visited, sub_graph)


def find_sub_graphs(jbox_conns):
    visited = []
    sub_graphs = []
    for jbox in jbox_conns:
        if jbox in visited:
            continue
        sub_graph = []
        dfs(jbox_conns, jbox, visited, sub_graph)
        sub_graphs.append(sub_graph)

    return sub_graphs


def challenge1(jboxes: list[Vertex]):
    distances = []
    for i in range(0, len(jboxes)):
        for j in range(i + 1, len(jboxes)):
            distance = get_distance(jboxes[i], jboxes[j])
            distances.append(
                {"dist": distance, "point1": jboxes[i], "point2": jboxes[j]}
            )
    distances.sort(key=lambda x: x["dist"])

    jbox_conns = get_n_closest_connections(distances, jboxes, 1000)
    sub_graphs = find_sub_graphs(jbox_conns)
    sub_graphs.sort(key=lambda graph: len(graph), reverse=True)

    return len(sub_graphs[0]) * len(sub_graphs[1]) * len(sub_graphs[2])


def challenge2(jboxes: list[Vertex]):
    jbox_conns = {}
    # Here we need to add all nodes to the graph right away because we need to know if they
    # are all connected, instead of only looking at the first 1000 connections
    for jbox in jboxes:
        jbox_conns[jbox.id] = []

    distances = []
    for i in range(0, len(jboxes)):
        for j in range(i + 1, len(jboxes)):
            distance = get_distance(jboxes[i], jboxes[j])
            distances.append(
                {"dist": distance, "point1": jboxes[i], "point2": jboxes[j]}
            )
    distances.sort(key=lambda x: x["dist"])

    # we know 1000 produces multiple graphs, so let's start with 1000 and grow until
    # we only have one subgraph
    i = 1000
    jbox_conns = get_n_closest_connections(distances, jboxes, i)
    sub_graphs = find_sub_graphs(jbox_conns)
    while len(sub_graphs) > 1:
        if i >= len(distances):
            i = len(distances) - 1
        for j in range(i, i * 2):
            point1 = distances[j]["point1"]
            point2 = distances[j]["point2"]
            jbox_conns[point1.id].append(point2.id)
            jbox_conns[point2.id].append(point1.id)
        sub_graphs = find_sub_graphs(jbox_conns)
        i = i * 2

    # We now know that first connection to create one big graph is somehwere between max_i and min_i
    max_i = i
    min_i = max_i / 2
    i = min_i + (max_i - min_i) / 2
    last_len = 1
    while True:
        jbox_conns = get_n_closest_connections(distances, jboxes, int(i))
        sub_graphs = find_sub_graphs(jbox_conns)
        if len(sub_graphs) == 1:
            if last_len != 1:
                jbox_conns = get_n_closest_connections(distances, jboxes, int(i) - 1)
                sub_graphs = find_sub_graphs(jbox_conns)
                if len(sub_graphs) > 1:
                    # we found it
                    return int(
                        distances[int(i) - 1]["point1"].x
                        * distances[int(i) - 1]["point2"].x
                    )
            max_i = i
            i = i - (i - min_i) / 2
            continue
        min_i = i
        i = i + (max_i - i) / 2
        last_len = len(sub_graphs)


def main():
    parsed = parse_input("day8/input.txt")
    result = challenge1(parsed)
    print(f"Solution to challenge 1: {result}")
    parsed = parse_input("day8/input.txt")
    result = challenge2(parsed)
    print(f"Solution to challenge 2: {result}")


if __name__ == "__main__":
    main()
