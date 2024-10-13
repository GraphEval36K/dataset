# GraphEval36K

This repository contains GraphEval36K datasets, a collection of more than 36,000 graph datasets for evaluating graph capabilities of LLMs. The datasets include undirected and directed graphs, categorized by different types of graphs. The data is structured in `JSONL` format.

## Repository Structure

The directory structure consists of two primary categories `data/`:
- `undirected`: Contains datasets representing undirected graphs.
- `directed`: Contains datasets representing directed graphs.

Each category includes folders for specific `LeetCode` questions (e.g., `lc1761`, `lc1615`, etc.). 
Within these folders, you'll find datasets classified into different types such as `regular`, `sparse`, `dense`, `complete`, `planar` ... etc.

## Data Formats

The files are stored in `JSONL` format, where each line is a valid `JSON` object. Each JSON object in the file represents a graph, containing information about nodes, edges, and other graph properties. This format is lightweight and scalable, making it suitable for handling large datasets.

### Example JSONL Entry
Here's an example of an entry from one of the `dense.jsonl` files:
```json
{
    
}
```

## Graph Types

Each graph file (e.g., sparse.jsonl, dense.jsonl) corresponds to a different graph structure:
- Regular Graphs: Graphs where each node has the same number of edges.
- Sparse Graphs: Graphs with fewer edges relative to the number of nodes.
- Dense Graphs: Graphs where most nodes are connected by edges.
- Complete Graphs: Graphs where every pair of nodes is connected.
- Planar Graphs: Graphs that can be embedded in a plane without edges crossing.
- Pseudo Graphs: Graphs that may contain loops or multiple edges between two nodes.

> Note: For some graph types, not all categories may be present. For example, a `complete` graph may not have a `sparse` category.


## Usage
To load the datasets, you can use the following Python code snippet:
```python
import jsonlines
# Reading from a dense.jsonl file
with jsonlines.open('path/to/dense.jsonl') as reader:
    for graph in reader:
        print(graph)
```

## License
This repository is licensed under the MIT License. See the LICENSE file for more details.

