# Challenge 4: Database CLI with Context
# Now create a CLI tool that simulates a simple database:

# Group called db
# Global --debug flag that shows extra information
# Commands: create_table, insert_record, list_records
# Use context to pass the debug setting
# Store "database" data in the context object (just use a dict)
# Debug mode should show timestamps and extra details

# Usage should be:
# bashpython script.py db create_table users
# python script.py db --debug insert_record users "John Doe"
# python script.py db list_records users

import click
from datatime import datetime

@click.group()
@click.option('--debug', is_flag=True)
@click.pass_context
def db(ctx, debug):
    ctx.ensure_object(dict)
    ctx.obj['debug'] = debug
    ctx.obj['database'] = {}
    
@db.command('create_table')
@click.argument('table_name')
@click.pass_context
def create_table(ctx, table_name):
    debug = ctx.obj['debug']
    database = ctx.obj['database']
    if table_name in database:
        click.echo(f"Table '{table_name}' already exists!")
        return
    database[table_name] = []
    
    if debug:
        timestamp = datetime.now().starttime("%Y-%m-%d %H:%M:%S")
        click.echo(f"[DEBUG {timestamp}] Created table '{table_name}'")
        click.echo(f"[DEBUG] Databse now has {len(database)} table(s)")
    else:
        click.echo(f"Created table '{table_name}")

@db.command('insert_records')
def insert_records():
    pass

@db.command('insert_record')
@click.argument('table_name')
@click.argument('record')
@click.pass_context
def insert_record(ctx, table_name, record):
    debug = ctx.obj['debug']
    database = ctx.obj['database']
    
    if table_name not in database:
        click.echo(f"Error: Table '{table_name}' doesn't exist")
        return
    database[table_name].append(record)
    
    if debug:
        timestamp = datetime.now().starttime("%Y-%m-%d %H:%M:%S")
        click.echo(f"[DEBUG {timestamp}] Inserted record: '{record}'")
        click.echo(f"[DEBUG] Table '{table_name}' now has {len(database[table_name])}")
    else:
        click.echo(f"Inserted record into '{table_name}'")
        
@db.command('list_records')
@click.argument('table_name')
@click.pass_context
def list_records(ctx, table_name):
    debug = ctx.obj['debug']
    database = ctx.obj['database']
    if table_name not in database:
        click.echo(f"Error: Table '{table_name}' doesn't exist!")
        return
    
    records = database[table_name]
    
    if debug:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        click.echo(f"[DEBUG {timestamp}] Listing records for table '{table_name}'")
    
    if not records:
        click.echo(f"Table '{table_name}' is empty")
    else:
        click.echo(f"Records in '{table_name}':")
        for i, record in enumerate(records, 1):
            click.echo(f"  {i}. {record}")
    
    if debug:
        click.echo(f"[DEBUG] Total records: {len(records)}")
    



if __name__ == '__main__':
    db()