"""
to_do_list.py — To-Do List 小组项目

数据结构：
    tasks 是一个 list，每个元素是一个 dict：
    {
        "id": int,            # 唯一编号，从 1 开始自增
        "description": str,   # 任务描述
        "priority": int,      # 1=高, 2=中, 3=低
        "completed": bool     # True=已完成, False=未完成
    }

文件格式：JSON（使用内置 json 模块）
"""

import json


def get_next_id(tasks):
    """返回下一个可用的任务编号。

    规则：取当前所有任务中最大的 id 加 1；
    空列表则返回 1。删除任务后不复用编号。

    Args:
        tasks (list[dict]): 当前任务列表。

    Returns:
        int: 下一个唯一任务编号。
    """
    pass


def add_task(tasks, description, priority=2):
    """向任务列表中添加一条新任务。

    Args:
        tasks (list[dict]): 当前任务列表（会被原地修改）。
        description (str): 任务描述文字。
        priority (int): 优先级，1=高, 2=中, 3=低。默认为 2。

    Returns:
        int: 新创建任务的 id。
    """
    pass


def view_tasks(tasks):
    """在屏幕上打印所有任务，以表格形式显示。

    格式示例：
        ID  | Pri | Done | Description
        ----+-----+------+------------------
         1  |  2  |  No  | Buy milk
         2  |  1  | Yes  | Finish report

    空列表时打印提示信息，不崩溃。

    Args:
        tasks (list[dict]): 要显示的任务列表。

    Returns:
        None
    """
    pass


def mark_complete(tasks, task_id):
    """把指定 id 的任务标记为已完成。

    Args:
        tasks (list[dict]): 当前任务列表。
        task_id (int): 要标记完成的任务编号。

    Returns:
        bool: 找到并标记成功返回 True；编号不存在返回 False。
    """
    pass


def delete_task(tasks, task_id):
    """从任务列表中删除指定 id 的任务。

    Args:
        tasks (list[dict]): 当前任务列表（会被原地修改）。
        task_id (int): 要删除的任务编号。

    Returns:
        bool: 找到并删除成功返回 True；编号不存在返回 False。
    """
    pass


def save_tasks(tasks, filename="tasks.json"):
    """把任务列表保存到 JSON 文件。

    Args:
        tasks (list[dict]): 要保存的任务列表。
        filename (str): 目标文件路径，默认为 "tasks.json"。

    Returns:
        bool: 保存成功返回 True；写入失败返回 False。
    """
    pass


def load_tasks(filename="tasks.json"):
    """从 JSON 文件加载任务列表。

    Args:
        filename (str): 要读取的文件路径，默认为 "tasks.json"。

    Returns:
        list[dict]: 加载到的任务列表；文件不存在或解析失败时返回空列表 []。
    """
    pass


def sort_tasks(tasks):
    """按优先级从高到低（1 → 2 → 3）排序列表，返回新列表。

    不修改原列表。同优先级的任务保持原有顺序。

    Args:
        tasks (list[dict]): 待排序的任务列表。

    Returns:
        list[dict]: 按优先级排序后的新任务列表。
    """
    pass


def main():
    """主程序入口：显示菜单、读取用户输入、调用对应功能函数。

    菜单循环直到用户选择退出：
        1. 添加任务
        2. 查看任务
        3. 标记完成
        4. 删除任务
        5. 按优先级查看
        6. 保存到文件
        7. 从文件加载
        0. 退出

    Returns:
        None
    """
    pass


if __name__ == "__main__":
    main()
