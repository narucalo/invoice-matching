# src/invoice_data.py

import csv
import logging
import os
import pandas as pd
import json

# Ensure the logs directory exists
log_dir = '../logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Setup logging
logging.basicConfig(filename=os.path.join(log_dir, 'app.log'), level=logging.DEBUG)

def load_invoices(file_path):
    """
    Load invoice data from a file. Supports CSV, Excel, and JSON formats.

    :param file_path: Path to the invoice file
    :return: List of dictionaries containing invoice data
    """
    invoices = []
    try:
        file_extension = os.path.splitext(file_path)[-1].lower()
        if file_extension == '.csv':
            invoices = load_csv(file_path)
        elif file_extension in ['.xls', '.xlsx']:
            invoices = load_excel(file_path)
        elif file_extension == '.json':
            invoices = load_json(file_path)
        else:
            logging.error(f"Unsupported file format: {file_extension}")
            raise ValueError(f"Unsupported file format: {file_extension}")
        
        logging.debug(f"Loaded {len(invoices)} invoices from {file_path}")
    except Exception as e:
        logging.error(f"Error loading invoices: {e}")
    return invoices

def load_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def load_excel(file_path):
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')

def load_json(file_path):
    with open(file_path, mode='r') as file:
        return json.load(file)

def filter_invoices_without_po(invoices):
    """
    Filter invoices that do not have a matching purchase order.

    :param invoices: List of dictionaries containing invoice data
    :return: List of invoices without POs
    """
    no_po_invoices = [invoice for invoice in invoices if not invoice.get('PO Number')]
    logging.debug(f"Filtered {len(no_po_invoices)} invoices without POs")
    return no_po_invoices

# Debug statements to test the functions
if __name__ == "__main__":
    invoice_data = load_invoices('../data/invoices.csv')
    invoices_without_po = filter_invoices_without_po(invoice_data)
    print(invoices_without_po)  # For quick debug, this will be removed later
