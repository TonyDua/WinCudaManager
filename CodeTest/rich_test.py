from rich.console import Console
from rich.table import Table

# 创建一个控制台对象
console = Console()

# 打印彩色文本
console.print("[bold magenta]WinCudaManager 输出信息[/bold magenta]")

# 创建一个表格
table = Table(show_header=True, header_style="bold blue")
table.add_column("Version", style="dim", width=12)
table.add_column("Status", justify="right", style="green")

# 添加表格行
table.add_row("CUDA 10.2", "Active")
table.add_row("CUDA 11.1", "Inactive")

# 打印表格
console.print(table)
