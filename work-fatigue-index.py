class MaxHeap:
    def __init__(self):
        self.elems = []

    def push(self, elem):
        self.elems.append(elem)
        self._heapify_up(len(self.elems) - 1)

    def pop(self):
        if not self.elems:
            return None

        max_val = self.elems[0]
        last_val = self.elems.pop()

        if self.elems:
            self.elems[0] = last_val
            self._heapify_down(0)

        return max_val

    def _heapify_up(self, idx):
        elems = self.elems

        while idx > 0:
            parent = (idx - 1) // 2

            if elems[idx] <= elems[parent]:
                break

            elems[idx], elems[parent] = elems[parent], elems[idx]
            idx = parent

    def _heapify_down(self, idx):
        elems = self.elems
        size = len(elems)

        while True:
            largest = idx
            left = idx * 2 + 1
            right = idx * 2 + 2

            if left < size and elems[largest] < elems[left]:
                largest = left

            if right < size and elems[largest] < elems[right]:
                largest = right

            if largest == idx:
                break

            elems[idx], elems[largest] = elems[largest], elems[idx]
            idx = largest


def test_max_heap(elems: list[int]) -> list[int]:
    max_heap = MaxHeap()
    for elem in elems:
        max_heap.push(elem)

    max_heap.pop()

    return max_heap.elems


assert test_max_heap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [9, 8, 6, 7, 3, 2, 5, 1, 4]
assert test_max_heap([-1, 2, 3, 4, 5, 6]) == [5, 4, 2, -1, 3]


def solution(n: int, works: list[int]) -> int:
    max_heap = MaxHeap()
    for work in works:
        max_heap.push(work)

    while n > 0:
        work = max_heap.pop()
        if work is None or work == 0:
            break

        max_heap.push(work - 1)
        n -= 1

    answer = 0
    while True:
        work = max_heap.pop()
        if work is None:
            break

        answer += work**2
    return answer


assert solution(4, [4, 3, 3]) == 12
assert solution(1, [2, 1, 2]) == 6
assert solution(3, [1, 1]) == 0

print("All tests passed!")
