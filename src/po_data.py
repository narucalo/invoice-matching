# src/po_data.py

import csv
import logging

# Setup logging
logging.basicConfig(filename='../logs/app.log', level=logging.DEBUG)

def load_pos(file_path):
    """
    Load purchase order data from a CSV file.

    :param file_path: Path to the PO CSV file
    :return: List of dictionaries containing PO data
    """
    pos = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                pos.append(row)
            logging.debug(f"Loaded {len(pos)} purchase orders from {file_path}")
        return pos
    except Exception as e:
        logging.error(f"Error loading purchase orders: {e}")
        return pos

def find_matching_po(invoice, pos):
    """
    Find a matching PO for a given invoice based on criteria such as product_id or stock_code.

    :param invoice: Dictionary containing invoice data
    :param pos: List of dictionaries containing PO data
    :return: Matching PO or None
    """
    for po in pos:
        if po.get('product_id') == invoice.get('product_id') and po.get('stock_code') == invoice.get('stock_code'):
            logging.debug(f"Found matching PO for invoice {invoice['invoice_date']}: {po['PO Number']}")
            return po
    logging.debug(f"No matching PO found for invoice {invoice['invoice_date']}")
    return None

# Debug statements to test the functions
if __name__ == "__main__":
    po_data = load_pos('../data/pos.csv')
    print(po_data)  # For quick debug, this will be removed later
