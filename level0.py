import json
import networkx as nx

def main(input_path, output_path):
    # Read input JSON
    with open(input_path, 'r') as file:
        input_data = json.load(file)

    # Extract neighborhood information
    distances = input_data['neighbourhoods']['n0']['distances']

    # Create a complete weighted graph using networkx
    G = nx.complete_graph(len(distances))

    # Solve TSP using greedy algorithm
    tour = nx.approximation.traveling_salesman_problem(G, cycle=True)

    # Create output data in the desired format
    output_data = {
        'v0': {
            'path': ["r0"] + [f"n{i}" for i in tour[1:]] + ["r0"]
        }
    }
    # Write output to JSON file
    with open(output_path, 'w') as output_file:
        json.dump(output_data, output_file, indent=2)

    # Print optimal path in the desired format
    print("Optimal path:", ["r0"] + [f"n{i}" for i in tour[1:]] + ["r0"])

if __name__ == "__main__":
    input_file_path = "C:\\21pw14 - hack\\level0.json"
    output_file_path = "C:\\21pw14 - hack\\level0_output.json"
    main(input_file_path, output_file_path)