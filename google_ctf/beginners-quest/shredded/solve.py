import os
import pathlib
import numpy as np
from PIL import Image

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False

def main():
    file_path = pathlib.Path(__file__).parent
    image_folder = file_path / 'bin'
    
    # Read files and sort to ensure deterministic order
    files = sorted(os.listdir(image_folder))
    n = len(files)
    
    images = []
    left_edges = []
    right_edges = []
    widths = []
    
    print("Loading images...")
    for file in files:
        img = Image.open(image_folder / file)
        images.append(img)
        widths.append(img.size[0])
        
        # Convert to numpy array
        # False (0) is black (writing), True (1 or 255) is white (background).
        # We represent writing as 1 and background as 0 for distance metrics.
        arr = (np.array(img) == False).astype(int)
        
        left_edges.append(arr[:, 0])
        right_edges.append(arr[:, -1])
        
    print(f"Loaded {n} images.")
    
    # Calculate costs for all pairs (i, j) where i is left of j
    # cost(i, j) = L1 distance between right_edge[i] and left_edge[j]
    edges = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            # Simple XOR-like distance: number of mismatched pixels on the edge
            cost = np.sum(np.abs(right_edges[i] - left_edges[j]))
            edges.append((cost, i, j))
            
    # Sort edges by cost ascending
    edges.sort()
    
    # Reconstruct the chain using Kruskal-like algorithm
    uf = UnionFind(n)
    right_neighbor = [None] * n
    left_neighbor = [None] * n
    
    connections = 0
    for cost, i, j in edges:
        # Check if i already has a right neighbor or j has a left neighbor
        if right_neighbor[i] is not None or left_neighbor[j] is not None:
            continue
            
        # Check if they belong to the same set (to prevent cycle)
        if uf.find(i) == uf.find(j):
            continue
            
        # Accept this edge
        uf.union(i, j)
        right_neighbor[i] = j
        left_neighbor[j] = i
        connections += 1
        
        if connections == n - 1:
            break
            
    # Find the start node (the one with no left neighbor)
    start_nodes = [i for i in range(n) if left_neighbor[i] is None]
    if len(start_nodes) != 1:
        print(f"Warning: Expected 1 start node, found {len(start_nodes)}: {start_nodes}")
        # If there are multiple chains (due to perfect loops or disjoint paths),
        # we pick the one with most nodes or just the first one.
        start_node = start_nodes[0]
    else:
        start_node = start_nodes[0]
        
    # Traverse the chain to get the final ordered sequence of images
    ordered_sequence = []
    curr = start_node
    while curr is not None:
        ordered_sequence.append(curr)
        curr = right_neighbor[curr]
        
    print(f"Chain reconstruction finished. Chain length: {len(ordered_sequence)}")
    if len(ordered_sequence) < n:
        print(f"Warning: Disconnected nodes! Unused nodes: {set(range(n)) - set(ordered_sequence)}")
        
    # Rotate the sequence to start with the blank margin image (54164269.png)
    target_filename = "54164269.png"
    if target_filename in files:
        target_node = files.index(target_filename)
        if target_node in ordered_sequence:
            idx_in_seq = ordered_sequence.index(target_node)
            ordered_sequence = ordered_sequence[idx_in_seq:] + ordered_sequence[:idx_in_seq]
            print(f"Rotated chain to start with {target_filename} (node {target_node})")
        else:
            print(f"Warning: {target_filename} not found in ordered sequence!")
    else:
        print(f"Warning: {target_filename} not found in files list!")
        
    # Stitch images together
    total_width = sum(widths[i] for i in ordered_sequence)
    height = images[0].size[1]
    
    # Create new mode '1' image with white background (color=1 or True)
    combined = Image.new('1', (total_width, height), color=1)
    
    current_x = 0
    for idx in ordered_sequence:
        combined.paste(images[idx], (current_x, 0))
        current_x += widths[idx]
        
    # Rotate the image 90 degrees counter-clockwise
    print("Rotating image 90 degrees counter-clockwise...")
    combined = combined.rotate(90, expand=True)
        
    output_path = file_path / "solved.png"
    combined.save(output_path)
    print(f"Stitched image saved successfully to: {output_path}")

if __name__ == "__main__":
    main()