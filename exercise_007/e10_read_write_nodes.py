# Read and Write Node Information# Reading node information (as dictionaries) from a file
def read_nodes_from_file(filename: str) -> dict:
    nodes = {}
    with open(filename, 'r') as file:
        for line in file:
            node_id, info = line.split(":")
            nodes[node_id] = info.strip().split(",")
    return nodes

# Writing node information to a file
def write_nodes_to_file(nodes: dict, filename: str):
    with open(filename, 'w') as file:
        for node_id, info in nodes.items():
            file.write(f"{node_id}: {', '.join(info)}\n")

# Example usage
nodes = {"node1": ["100", "200"], "node2": ["150", "300"]}
write_nodes_to_file(nodes, 'nodes_output.txt')
print(read_nodes_from_file('nodes_output.txt'))
