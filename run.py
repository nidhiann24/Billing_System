from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

from flask_migrate import MigrateCommand
from flask.cli import with_appcontext
import click

@app.shell_context_processor
def make_shell_context():
    from app.models import User, Customer, Product, Invoice, InvoiceItem
    return {'db': db, 'User': User, 'Customer': Customer, 'Product': Product, 'Invoice': Invoice, 'InvoiceItem': InvoiceItem}
