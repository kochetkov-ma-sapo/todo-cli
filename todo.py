#!/usr/bin/env python3
"""Minimal todo list CLI backed by a JSON file."""
import argparse
import json
import os
from pathlib import Path

DB = Path(os.environ.get("TODO_FILE", Path.home() / ".todo.json"))


def load():
    return json.loads(DB.read_text()) if DB.exists() else []


def save(items):
    DB.write_text(json.dumps(items, indent=2))


def find(items, item_id):
    for item in items:
        if item["id"] == item_id:
            return item
    raise SystemExit(f"no task with id {item_id}")


def main():
    parser = argparse.ArgumentParser(prog="todo", description="Tiny todo list")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("add", help="add a task").add_argument("text", nargs="+")
    sub.add_parser("list", help="show tasks")
    sub.add_parser("done", help="mark a task done").add_argument("id", type=int)
    sub.add_parser("remove", help="delete a task").add_argument("id", type=int)
    args = parser.parse_args()

    items = load()
    if args.cmd == "add":
        new_id = max((i["id"] for i in items), default=0) + 1
        items.append({"id": new_id, "text": " ".join(args.text), "done": False})
        print(f"added #{new_id}")
    elif args.cmd == "list":
        if not items:
            print("nothing to do")
        for i in items:
            print(f"{i['id']:>3} [{'x' if i['done'] else ' '}] {i['text']}")
        return
    elif args.cmd == "done":
        find(items, args.id)["done"] = True
        print(f"done #{args.id}")
    elif args.cmd == "remove":
        items.remove(find(items, args.id))
        print(f"removed #{args.id}")
    save(items)


if __name__ == "__main__":
    main()
