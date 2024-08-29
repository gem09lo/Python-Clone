from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from urllib.request import urlopen
import json
from time import sleep
from rich.progress import track
from rich.tree import Tree
from rich.console import Console
from rich import print as rprint

nums_list = [1, 2, 3, 4]
rprint(nums_list)

nums_tuple = (1, 2, 3, 4)
rprint(nums_tuple)

nums_dict = {'nums_list': nums_list, 'nums_tuple': nums_tuple}
rprint(nums_dict)

bool_list = [True, False]
rprint(bool_list)

# Style your console with Rich
console = Console()


def merge_dict(dict_one, dict_two):
    merged_dict = dict_one | dict_two
    console.log(merged_dict, log_locals=True)


merge_dict({'id': 1}, {'name': 'Ashutosh'})

# Using Tree in Rich
tree = Tree("Family Tree")
tree.add("Mom")
tree.add("Dad")
tree.add("Brother").add("Wife")
tree.add("[red]Sister").add("[green]Husband").add("[blue]Son")

rprint(tree)

# Display a progress bar


def process_data():
    sleep(0.02)


for _ in track(range(100), description='[green]Processing data'):
    process_data()

# Record the time when a particular task is finished executing
console = Console()

data = [1, 2, 3, 4, 5]
with console.status("[bold green]Fetching data...") as status:
    while data:
        num = data.pop(0)
        sleep(1)
        console.log(f"[green]Finish fetching data[/green] {num}")

    console.log(f'[bold][red]Done!')

# Display rich columns in python


def get_content(user):
    """Extract text from user dict."""
    country = user["location"]["country"]
    name = f"{user['name']['first']} {user['name']['last']}"
    return f"[b]{name}[/b]\n[yellow]{country}"


console = Console()


users = json.loads(
    urlopen("https://randomuser.me/api/?results=30").read())["results"]
user_renderables = [Panel(get_content(user), expand=True) for user in users]
console.print(Columns(user_renderables))

# Display rich tables in python

table = Table(title="Todo List")

table.add_column("S. No.", style="cyan", no_wrap=True)
table.add_column("Task", style="magenta")
table.add_column("Status", justify="right", style="green")

table.add_row("1", "Buy Milk", "✅")
table.add_row("2", "Buy Bread", "✅")
table.add_row("3", "Buy Jam", "❌")

console = Console()
console.print(table)
