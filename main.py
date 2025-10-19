from task_manager import TaskManager
from ai_service import create_simple_tasks


def print_menu():
    print("\n--- Gestor de Tareas inteligente ---\n")
    print("1. Agregar tarea.")
    print("2. Agregar tarea compleja (con IA).")
    print("3. Listar tareas.")
    print("4. Completar tarea.")
    print("5. Eliminar tarea.")
    print("6. Salir.")

def main():

    manager = TaskManager()

    while True:
        
        print_menu()

        try:
            choice = int(input("Seleccione una opción: "))

            match choice:
                case 1:
                    description = input("Ingrese la descripción de la tarea:  ")
                    manager.add_task(description)
                case 2:
                    description = input("Ingrese la descripción de la tarea compleja:  ")
                    subtasks = create_simple_tasks(description)
                    for subtask in subtasks:
                        if not subtask.startswith("Error"):
                              manager.add_task(subtask)
                        else:
                              print(subtask)
                              break
                case 3:
                    manager.list_tasks()
                case 4:
                    id = int(input("Ingrese el ID de la tarea a completar: "))
                    manager.complete_task(id)
                case 5:
                    id = int(input("Ingrese el ID de la tarea a eliminar: "))
                    manager.delete_task(id)
                case 6:
                    print("Saliendo...")
                    return
                case _:
                    print("Opción no válida.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

if __name__ == "__main__":
                main()