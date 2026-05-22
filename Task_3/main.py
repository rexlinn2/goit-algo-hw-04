import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)


def print_tree(directory: Path, indent: str = ""):
    """
    Рекурсивно виводить структуру директорії
    """
    try:
        items = sorted(directory.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    except PermissionError:
        print(indent + Fore.RED + "[Немає доступу]")
        return

    for item in items:
        if item.is_dir():
            print(indent + Fore.BLUE + f"📂 {item.name}")
            print_tree(item, indent + "    ")
        else:
            print(indent + Fore.GREEN + f"📜 {item.name}")


def main():
    if len(sys.argv) < 2:
        print(Fore.RED + "Помилка: не вказано шлях до директорії")
        print("Використання: python main.py /шлях/до/директорії")
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.exists():
        print(Fore.RED + "Помилка: такий шлях не існує")
        sys.exit(1)

    if not path.is_dir():
        print(Fore.RED + "Помилка: це не директорія")
        sys.exit(1)

    print(Fore.YELLOW + f"📦 {path.name}")

    print_tree(path)


if __name__ == "__main__":
    main()