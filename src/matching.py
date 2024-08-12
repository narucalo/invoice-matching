# src/matching.py

import csv
from invoice_data import load_invoices, filter_invoices_without_po
from po_data import load_pos, find_matching_po

def match_invoices_to_pos(invoice_file, po_file):
    """
    Match invoices to purchase orders and return results.

    :param invoice_file: Path to the invoice CSV file
    :param po_file: Path to the PO CSV file
    :return: List of invoices with their matching POs
    """
    invoices = load_invoices(invoice_file)
    pos = load_pos(po_file)
    
    unmatched_invoices = []
    
    for invoice in invoices:
        # Attempt to match based on PO Number if available
        po_number = invoice.get('PO Number')
        matching_po = None
        
        if not po_number:
            # If no PO Number, try matching based on product_id and stock_code
            matching_po = find_matching_po(invoice, pos)
            if matching_po:
                invoice['PO Number'] = matching_po.get('PO Number')
            else:
                unmatched_invoices.append(invoice)
        else:
            # If a PO Number is present, check for exact match
            matching_po = next((po for po in pos if po.get('PO Number') == po_number), None)
            if not matching_po:
                unmatched_invoices.append(invoice)

    # Print unmatched invoices
    print("Unmatched Invoices:")
    for invoice in unmatched_invoices:
        print(invoice)

    return unmatched_invoices

def save_unmatched_invoices(unmatched_invoices, output_file):
    """
    Save the unmatched invoices to a CSV file.

    :param unmatched_invoices: List of dictionaries containing unmatched invoice data
    :param output_file: Path to the output CSV file
    """
    if unmatched_invoices:
        fieldnames = unmatched_invoices[0].keys()
        with open(output_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(unmatched_invoices)
        print(f"Unmatched invoices saved to {output_file}")
    else:
        print("No unmatched invoices to save.")

# Add this at the end of your matching.py script
if __name__ == "__main__":
    unmatched_invoices = match_invoices_to_pos('../data/invoices.csv', '../data/pos.csv')
    save_unmatched_invoices(unmatched_invoices, '../data/unmatched_invoices.csv')
    print(f"Total unmatched invoices: {len(unmatched_invoices)}")
