"""
test_to_do_list.py — Unit tests for to_do_list.py
Run with: pytest -v
"""

import os
from to_do_list import (
    get_next_id, add_task, view_tasks, mark_complete, delete_task,
    save_tasks, load_tasks, sort_tasks
)


# --- get_next_id ---

def test_get_next_id_empty():
    assert get_next_id([]) == 1


def test_get_next_id_nonempty():
    tasks = [{"id": 1}, {"id": 5}, {"id": 3}]
    assert get_next_id(tasks) == 6


# --- add_task ---

def test_add_task_basic():
    tasks = []
    tid = add_task(tasks, "Buy milk")
    assert tid == 1
    assert tasks[0]["description"] == "Buy milk"
    assert tasks[0]["priority"] == 2
    assert tasks[0]["completed"] is False


def test_add_task_with_priority():
    tasks = []
    add_task(tasks, "Urgent", priority=1)
    assert tasks[0]["priority"] == 1


def test_add_task_increments_id():
    tasks = []
    id1 = add_task(tasks, "First")
    id2 = add_task(tasks, "Second")
    assert id2 == id1 + 1


# --- mark_complete ---

def test_mark_complete_success():
    tasks = []
    tid = add_task(tasks, "Test")
    assert mark_complete(tasks, tid) is True
    assert tasks[0]["completed"] is True


def test_mark_complete_not_found():
    tasks = []
    add_task(tasks, "Test")
    assert mark_complete(tasks, 999) is False


# --- delete_task ---

def test_delete_task_success():
    tasks = []
    tid = add_task(tasks, "To delete")
    assert delete_task(tasks, tid) is True
    assert len(tasks) == 0


def test_delete_task_not_found():
    tasks = []
    add_task(tasks, "Keep")
    assert delete_task(tasks, 999) is False
    assert len(tasks) == 1


# --- sort_tasks ---

def test_sort_tasks_by_priority():
    tasks = []
    add_task(tasks, "Low", priority=3)
    add_task(tasks, "High", priority=1)
    add_task(tasks, "Medium", priority=2)
    result = sort_tasks(tasks)
    assert result[0]["description"] == "High"
    assert result[1]["description"] == "Medium"
    assert result[2]["description"] == "Low"


def test_sort_does_not_modify_original():
    tasks = []
    add_task(tasks, "B", priority=2)
    add_task(tasks, "A", priority=1)
    sort_tasks(tasks)
    assert tasks[0]["description"] == "B"


# --- save / load ---

def test_save_and_load(tmp_path):
    tasks = []
    add_task(tasks, "Test task", priority=1)
    f = str(tmp_path / "test.json")
    assert save_tasks(tasks, f) is True
    loaded = load_tasks(f)
    assert len(loaded) == 1
    assert loaded[0]["description"] == "Test task"
    assert loaded[0]["priority"] == 1
    assert loaded[0]["completed"] is False


def test_load_nonexistent_file():
    assert load_tasks("no_such_file_12345.json") == []
