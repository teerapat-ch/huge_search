import click
from minheap import MinHeap
import time

@click.command()
@click.option('--file_path', help='File path')
@click.option('--n', default=10, help='Top n values to get uuid')
def get_top_n(file_path, n):
    start = time.time()
    data = open(file_path, "r")
    heap = MinHeap(n)

    row_count = 0
    while True:
        line = data.readline()
        if not line:
            break
        row = line.split(",")
        heap.add(int(row[1]))
        row_count += 1

    row_count = 0
    occurences = 0
    data = open(file_path, "r")
    while True:
        line = data.readline()
        if not line:
            break
        row = line.split(",")
        if heap.elementInHeap(int(row[1])):
            print(row[0], row[1], end="")
            occurences += 1
        row_count += 1

    print("============================================================")
    print(f"Top {n} values  : {heap.Heap[1:]}")
    print(f"Total rows      : {row_count}")
    print(f"Matched rows    : {occurences}")
    print(f"Matched percent : {100 * occurences / row_count} %")
    print(f"Time took       : {time.time() - start} seconds")
    print("============================================================")
    return heap.Heap[1:]


if __name__ == '__main__':
    get_top_n()
