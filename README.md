# GraphEval36K

This repository contains GraphEval36K datasets, a collection of more than 36,000 graph datasets for evaluating graph capabilities of LLMs. The datasets include undirected and directed graphs, categorized by different types of graphs. The data is structured in `JSONL` format.

## Repository Structure

The directory structure consists of two primary categories `data/`:
- `undirected`: Contains datasets representing undirected graphs.
- `directed`: Contains datasets representing directed graphs.

Each category includes folders for specific `LeetCode` questions (e.g., `lc1761`, `lc1615`, etc.). 
Within these folders, you'll find datasets classified into different types such as `regular`, `sparse`, `dense`, `complete`, `planar` ... etc.

## Data Formats

The files are stored in `JSONL` format, where each line is a valid `JSON` object. Each JSON object in the file represents a graph, containing information about nodes, edges, and other graph properties. This format is lightweight and scalable, making it suitable for handling large datasets. Inside each `jsonl` file, there are at most four dictionaries (subcategory name). And each dictionary has the following keys: "graphs", "labels", "complexity" and other data needed for the coding problem. Now we show a simplified example `sparse.jsonl` in Leetcode 210.


```json
{"connected": {"graphs": [[[0, 1], [0, 2], [0, 4], [0, 0], [0, 5], [1, 5], [1, 2], [1, 3], [2, 3], [2, 7], [2, 9], [2, 2], [2, 8], [3, 6], [4, 3], [4, 9], [5, 7], [6, 8], [6, 5], [6, 9], [7, 9], [7, 8], [7, 0], [8, 6], [8, 3], [9, 1], [9, 0]]], "numCourse": [10], "labels": [[]], "complexity": [27]}}

{"disconnected": {"graphs": [[[1, 2], [1, 7], [3, 4]]], "numCourse": [10], "labels": [[0, 2, 7, 1, 4, 3, 5, 6, 8, 9]], "complexity": [3]}}

{"cyclic": {"graphs": [[[3, 4], [4, 5], [5, 3], [5, 4], [0, 5], [0, 3], [2, 2], [2, 5], [1, 1]]], "numCourse": [6], "labels": [[]], "complexity": [9]}}

{"acyclic": {"graphs": [[[1, 3], [2, 4], [2, 3], [2, 1], [3, 4], [3, 0], [5, 1], [5, 4], [5, 6], [5, 0], [5, 3], [6, 0]]], "numCourse": [7], "labels": [[0, 4, 3, 1, 2, 6, 5]], "complexity": [12]}}

```

### Example Data Entry
Here's an example of an entry from one of the `dense.jsonl` files:
```json
{
    [[[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 15], [0, 18], [1, 2], [1, 3], [1, 5], [1, 6], [1, 8], [1, 9], [1, 10], [1, 12], [1, 13], [1, 16], [1, 17], [1, 18], [2, 0], [2, 1], [2, 4], [2, 6], [2, 7], [2, 8], [2, 9], [2, 12], [2, 13], [2, 14], [2, 17], [2, 18], [3, 0], [3, 1], [3, 2], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12], [3, 13], [3, 15], [3, 16], [3, 17], [3, 18], [4, 0], [4, 1], [4, 2], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10], [4, 11], [4, 12], [4, 13], [4, 15], [4, 16], [4, 17], [4, 18], [5, 2], [5, 3], [5, 4], [5, 7], [5, 8], [5, 9], [5, 10], [5, 12], [5, 13], [5, 14], [5, 16], [5, 17], [5, 18], [6, 1], [6, 3], [6, 4], [6, 5], [6, 8], [6, 9], [6, 11], [6, 12], [6, 15], [6, 16], [6, 17], [6, 18], [7, 2], [7, 3], [7, 5], [7, 8], [7, 9], [7, 11], [7, 12], [7, 13], [7, 14], [7, 15], [7, 17], [7, 18], [8, 1], [8, 2], [8, 3], [8, 5], [8, 6], [8, 7], [8, 9], [8, 11], [8, 12], [8, 13], [8, 14], [8, 15], [8, 16], [8, 17], [8, 18], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [9, 10], [9, 11], [9, 12], [9, 13], [9, 14], [9, 16], [10, 0], [10, 2], [10, 3], [10, 4], [10, 6], [10, 7], [10, 8], [10, 9], [10, 11], [10, 12], [10, 14], [10, 15], [10, 16], [10, 17], [10, 18], [11, 0], [11, 1], [11, 2], [11, 3], [11, 4], [11, 5], [11, 7], [11, 8], [11, 9], [11, 10], [11, 14], [11, 15], [11, 16], [11, 17], [11, 18], [12, 0], [12, 3], [12, 5], [12, 6], [12, 7], [12, 8], [12, 9], [12, 10], [12, 11], [12, 13], [12, 15], [12, 16], [12, 17], [12, 18], [13, 0], [13, 1], [13, 2], [13, 3], [13, 4], [13, 6], [13, 7], [13, 8], [13, 9], [13, 10], [13, 11], [13, 12], [13, 14], [13, 15], [13, 16], [13, 17], [13, 18], [14, 0], [14, 1], [14, 2], [14, 3], [14, 4], [14, 5], [14, 6], [14, 8], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13], [14, 15], [14, 17], [14, 18], [15, 0], [15, 1], [15, 2], [15, 4], [15, 5], [15, 6], [15, 7], [15, 8], [15, 9], [15, 10], [15, 11], [15, 12], [15, 13], [15, 14], [15, 17], [15, 18], [16, 0], [16, 1], [16, 2], [16, 4], [16, 5], [16, 6], [16, 7], [16, 8], [16, 9], [16, 10], [16, 13], [16, 15], [16, 17], [17, 0], [17, 1], [17, 2], [17, 4], [17, 5], [17, 6], [17, 7], [17, 8], [17, 9], [17, 12], [17, 13], [17, 16], [17, 18], [18, 1], [18, 2], [18, 4], [18, 5], [18, 6], [18, 7], [18, 8], [18, 10], [18, 11], [18, 12], [18, 13], [18, 14], [18, 15], [18, 16], [18, 17]]]
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
To load the datasets, you can use the following Python code snippet (For example, we read the dense graph samples of LeetCode 797):
```python
import jsonlines
# Reading from a dense.jsonl file
with jsonlines.open('./data/directed/lc797/dense.jsonl') as reader:
    for graph in reader:
        print(graph)
```

## License
This repository is licensed under the MIT License. See the LICENSE file for more details.

