import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    file1 = {
        "nome_do_arquivo": "file.txt",
        "qtd_linhas": 5,
    }
    file2 = {
        "nome_do_arquivo": "file.txt",
        "qtd_linhas": 4,
    }
    priority_queue.enqueue(file1)
    assert len(priority_queue) == 1
    priority_queue.dequeue()
    assert len(priority_queue) == 0
    priority_queue.enqueue(file1)
    priority_queue.enqueue(file2)
    assert priority_queue.search(0) == file2
    assert priority_queue.search(1) == file1
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(3)
