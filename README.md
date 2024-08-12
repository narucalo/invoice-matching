# Invoice-Purchase Order Matching Script

## Overview

This Python script matches invoices to purchase orders based on specified criteria such as `PO Number`, `product_id`, and `stock_code`. Any unmatched invoices are saved to a CSV file for further review.

## Project Structure

invoice-matching/
│
├── src/
│ ├── matching.py # Main script for matching invoices to POs
│ ├── invoice_data.py # Module for loading and processing invoice data
│ ├── po_data.py # Module for loading and processing purchase order data
│
├── data/
│ ├── invoices.csv # Example CSV file containing invoice data
│ ├── pos.csv # Example CSV file containing purchase order data
│ ├── unmatched_invoices.csv # Output CSV file for unmatched invoices
│
├── logs/
│ └── app.log # Log file for debugging and tracking program execution
│
├── requirements.txt # Python dependencies required for the project
└── README.md # Project description and usage instructions

## How to Use

### Prerequisites

- Python 3.x
- Ensure that your CSV files (`invoices.csv` and `pos.csv`) are properly formatted and located in the `data/` directory.

### Setup

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the script using the following command:

   ```bash
   python src/matching.py
