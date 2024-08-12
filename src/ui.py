# src/ui.py

import tkinter as tk
from tkinter import filedialog, messagebox
from matching import match_invoices_to_pos, save_unmatched_invoices

class InvoiceMatcherUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Invoice-Purchase Order Matcher")

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Invoice File Selection
        self.invoice_label = tk.Label(self.root, text="Select Invoice File:")
        self.invoice_label.grid(row=0, column=0, padx=10, pady=10)

        self.invoice_path = tk.Entry(self.root, width=50)
        self.invoice_path.grid(row=0, column=1, padx=10, pady=10)

        self.invoice_button = tk.Button(self.root, text="Browse", command=self.browse_invoice_file)
        self.invoice_button.grid(row=0, column=2, padx=10, pady=10)

        # PO File Selection
        self.po_label = tk.Label(self.root, text="Select PO File:")
        self.po_label.grid(row=1, column=0, padx=10, pady=10)

        self.po_path = tk.Entry(self.root, width=50)
        self.po_path.grid(row=1, column=1, padx=10, pady=10)

        self.po_button = tk.Button(self.root, text="Browse", command=self.browse_po_file)
        self.po_button.grid(row=1, column=2, padx=10, pady=10)

        # Start Matching Button
        self.match_button = tk.Button(self.root, text="Start Matching", command=self.start_matching)
        self.match_button.grid(row=2, column=1, pady=20)

        # Result Display
        self.result_text = tk.Text(self.root, height=10, width=80)
        self.result_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def browse_invoice_file(self):
        filepath = filedialog.askopenfilename(
            title="Select Invoice File", 
            filetypes=(("All Supported Formats", "*.csv;*.xls;*.xlsx;*.json"),
                       ("CSV files", "*.csv"),
                       ("Excel files", "*.xls;*.xlsx"),
                       ("JSON files", "*.json"))
        )
        self.invoice_path.insert(0, filepath)

    def browse_po_file(self):
        filepath = filedialog.askopenfilename(
            title="Select PO File", 
            filetypes=(("All Supported Formats", "*.csv;*.xls;*.xlsx;*.json"),
                       ("CSV files", "*.csv"),
                       ("Excel files", "*.xls;*.xlsx"),
                       ("JSON files", "*.json"))
        )
        self.po_path.insert(0, filepath)

    def start_matching(self):
        invoice_file = self.invoice_path.get()
        po_file = self.po_path.get()

        if not invoice_file or not po_file:
            messagebox.showerror("Error", "Please select both invoice and PO files.")
            return

        unmatched_invoices = match_invoices_to_pos(invoice_file, po_file)
        save_unmatched_invoices(unmatched_invoices, "unmatched_invoices.csv")

        if unmatched_invoices:
            result_message = f"Total unmatched invoices: {len(unmatched_invoices)}"
            self.result_text.insert(tk.END, result_message + "\n")
            self.result_text.insert(tk.END, "Unmatched invoices saved to unmatched_invoices.csv\n")
        else:
            self.result_text.insert(tk.END, "All invoices matched successfully!\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = InvoiceMatcherUI(root)
    root.mainloop()
