"""Pruebas unitarias para TaskManager (archivo en la raíz del proyecto)

Estas pruebas usan pytest fixtures: tmp_path y capsys. El archivo está pensado
para ejecutarse desde la carpeta del proyecto con el intérprete dentro de
`.venv` (por ejemplo: `.venv\Scripts\python.exe -m pytest test_task_manager_root.py`).
"""
import json
import os

from task_manager import TaskManager, Task


def _temp_filename(tmp_path):
    return str(tmp_path / "tasks.json")


def test_inicio_sin_fichero(tmp_path, capsys):
    TaskManager.FILENAME = _temp_filename(tmp_path)
    if os.path.exists(TaskManager.FILENAME):
        os.remove(TaskManager.FILENAME)
    mgr = TaskManager()
    assert mgr._tasks == []
    assert mgr._next_id == 1
    mgr.list_tasks()
    captured = capsys.readouterr()
    assert "No tasks available." in captured.out


def test_add_task_guarda_y_print(tmp_path, capsys):
    TaskManager.FILENAME = _temp_filename(tmp_path)
    mgr = TaskManager()
    mgr.add_task("Comprar leche")
    captured = capsys.readouterr()
    assert "Task added:" in captured.out
    assert "Comprar leche" in captured.out
    with open(TaskManager.FILENAME, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["id"] == 1
    assert data[0]["description"] == "Comprar leche"
    assert data[0]["completed"] is False


def test_complete_task_marcar_y_guardar(tmp_path, capsys):
    TaskManager.FILENAME = _temp_filename(tmp_path)
    mgr = TaskManager()
    mgr.add_task("Escribir tests")
    capsys.readouterr()
    mgr.complete_task(1)
    captured = capsys.readouterr()
    assert "Task completed:" in captured.out
    with open(TaskManager.FILENAME, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data[0]["completed"] is True


def test_delete_task_elimina_y_guardar(tmp_path, capsys):
    TaskManager.FILENAME = _temp_filename(tmp_path)
    mgr = TaskManager()
    mgr.add_task("Tarea uno")
    mgr.add_task("Tarea dos")
    capsys.readouterr()
    mgr.delete_task(1)
    captured = capsys.readouterr()
    assert "Task deleted:" in captured.out
    with open(TaskManager.FILENAME, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["id"] == 2


def test_load_tasks_lee_fichero_existente(tmp_path, capsys):
    path = tmp_path / "tasks.json"
    sample = [
        {"id": 1, "description": "Existente uno", "completed": False},
        {"id": 2, "description": "Existente dos", "completed": True},
    ]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(sample, f, indent=4)
    TaskManager.FILENAME = str(path)
    mgr = TaskManager()
    assert len(mgr._tasks) == 2
    assert mgr._next_id == 3
    mgr.list_tasks()
    captured = capsys.readouterr()
    assert "Existente uno" in captured.out
    assert "#1" in captured.out
