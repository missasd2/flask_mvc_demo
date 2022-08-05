import sqlite3

import click
from flask import current_app, g
"""
current_app: 用于指向当前 处理请求的 flask应用
"""
def get_db():
    # g 用于存储信息，这些信息可能在 request中，被多个函数访问
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    # 使用current_app.open_resource() 无需知道应用部署的位置
    with current_app.open_resource("scheme.sql") as f:
        db.executescript(f.read().decode("utf8"))


# 自定义cmd命令，该命令名为 init-db
@click.command("init-db")
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


# register with the application
def init_app(app):
    # 在返回response后，当要清理时，调用close_db函数
    app.teardown_appcontext(close_db)
    # 添加一个新的command
    app.cli.add_command(init_db_command)



