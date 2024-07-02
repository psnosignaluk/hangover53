from __future__ import annotations

import rich


def print_help():
    console = rich.console.Console()

    console.print("[bold]h53", justify="center")
    console.print()
    console.print("Hunts for orphaned DNS records and reports on them.", justify="center")
    console.print()
    console.print("[bold]h53[/bold] [red]OPT[/red] [cyan]--ARGS[/cyan]", justify="left")
    console.print()


def main():
    """
    A container-based application that looks for orphaned DNS records and reports on them.
    """