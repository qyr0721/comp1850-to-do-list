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
    """返回下一个可用的任务编号。空列表返回 1。"""
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1


def add_task(tasks, description, priority=2):
    """向任务列表中添加一条新任务，返回新任务的 id。"""
    new_id = get_next_id(tasks)
    task = {
        "id": new_id,
        "description": description,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    return new_id


def view_tasks(tasks):
    """在屏幕上打印所有任务。空列表时打印提示信息。"""
    if not tasks:
        print("No tasks in the list.")
        return
    print(f"{'ID':<5} {'Pri':<5} {'Done':<6} Description")
    print("-" * 45)
    for t in tasks:
        done = "Yes" if t["completed"] else "No"
        print(f"{t['id']:<5} {t['priority']:<5} {done:<6} {t['description']}")


def mark_complete(tasks, task_id):
    """把指定 id 的任务标记为已完成。成功返回 True，找不到返回 False。"""
    for t in tasks:
        if t["id"] == task_id:
            t["completed"] = True
            return True
    return False


def delete_task(tasks, task_id):
    """删除指定 id 的任务。成功返回 True，找不到返回 False。"""
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            tasks.pop(i)
            return True
    return False


def save_tasks(tasks, filename="tasks.json"):
    """把任务列表保存到 JSON 文件。成功返回 True。"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)
        return True
    except Exception:
        return False


def load_tasks(filename="tasks.json"):
    """从 JSON 文件加载任务列表。文件不存在或解析失败返回空列表。"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def sort_tasks(tasks):
    """按优先级从高到低（1→2→3）排序，返回新列表，不修改原列表。"""
    return sorted(tasks, key=lambda t: t["priority"])


def main():
    """主程序入口：显示菜单、读取用户输入、调用对应功能函数。"""
    tasks = load_tasks()
    while True:
        print("\n===== To-Do List =====")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark complete")
        print("4. Delete task")
        print("5. Sort by priority")
        print("6. Save to file")
        print("7. Load from file")
        print("0. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            desc = input("Task description: ")
            raw = input("Priority (1=high, 2=medium, 3=low) [2]: ")
            pri = int(raw) if raw else 2
            new_id = add_task(tasks, desc, pri)
            print(f"Added task #{new_id}")
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            raw = input("Task ID to mark complete: ")
            if raw.isdigit() and mark_complete(tasks, int(raw)):
                print("Marked as done!")
            else:
                print("Task not found.")
        elif choice == "4":
            raw = input("Task ID to delete: ")
            if raw.isdigit() and delete_task(tasks, int(raw)):
                print("Deleted!")
            else:
                print("Task not found.")
        elif choice == "5":
            view_tasks(sort_tasks(tasks))
        elif choice == "6":
            if save_tasks(tasks):
                print("Saved!")
            else:
                print("Save failed.")
        elif choice == "7":
            tasks = load_tasks()
            print(f"Loaded {len(tasks)} tasks.")
        elif choice == "0":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
