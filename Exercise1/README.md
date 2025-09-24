# Shop Billing System Project
<img width="1919" height="1079" alt="Image" src="https://github.com/user-attachments/assets/d2fadbb9-7586-472d-bbd5-deff02ec806a" />

A hands-on Python project that demonstrates practical data handling for a simple shop billing scenario. This project shows how to work with different data types and structures while managing product sales information.

## What This Project Does

This code simulates basic shop operations by tracking product quantities, managing inventory, and generating simple reports. It's designed to help learners understand how different Python data structures work together in a real-world context.

## How the Code Works

### Tracking Product Quantities
We start with a list of how many items were sold for different products:

quantities = [6, 10, 17, 3, 90]
The code then calculates basic statistics:

Total items sold: 126

Average per product: 25.2

Slowest selling product: 3 items

Fastest selling product: 90 items

Generating Sales Reports
The system creates two types of reports using f-strings:

Detailed Report - shows all the calculations in a readable format

Summary Report - gives a quick overview of key numbers

Checking Sales Performance
The code automatically checks if sales are meeting expectations:

python
threshold = 7
if average > threshold and maximum > 11:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")
This uses a compound condition - both the average must be above 7 AND at least one product must have sold more than 11 units.

Managing Inventory
We keep track of what products are in stock:

python
items = ["Notebook", "Pen", "Laptop", "Smartphone", "Tablet"]
The system can:

Add new products (like "Mouse")

Remove products that start with 'T'

Sort the list alphabetically

Working with Prices
We store prices using Python's array module, which is efficient for numbers:

python
import array
price_array = array.array('i', [1000000, 25000, 750, 300, 300000])
The code compares working with arrays versus regular lists to show they give the same results for basic math operations.

Keeping Product Records
Each product has its own record with details:

python
records = [
    {"id": 1, "name": "Laptop", "Value": 1000000, "Quantity sold": 6},
    {"id": 2, "name": "Mouse", "Value": 25000, "Quantity sold": 10},
    # ... more products
]
The system can update product information (like changing a price) and remove products that are no longer available.

What You'll See When You Run the Code
Sales Analysis Output
text
Quantities sold are: 	[6, 10, 17, 3, 90]
 Total quantity sold:	126
 Average of the quantities sold:	25.2
 The minimum quantity sold:	3
 The maximum quantity sold:	90

Total: 126, Average: 25.2, Min: 3, Max: 90
Performance Check
text
Status: Above Standard
Inventory Changes
text
Original list: ['Notebook', 'Pen', 'Laptop', 'Smartphone', 'Tablet']
Updated list: ['Laptop', 'Mouse', 'Notebook', 'Pen', 'Smartphone']
Data Structure Comparison
text
Array sum equals list sum: True
Learning Points
This project helps you understand:

Integers and math operations: Calculating totals, averages, min/max values

String formatting: Creating readable reports with f-strings

Boolean logic: Using conditions to make decisions about data

List operations: Adding, removing, and sorting items

Arrays: Storing numeric data efficiently

Dictionaries: Organizing structured information about products

Getting Started
Make sure you have Python installed (version 3.6 or newer)

Copy the code into a .py file

Run it from your terminal or IDE

The code will execute all operations automatically and show you the results

Notes About This Project
This is a self-contained demonstration - no user input needed

All data is hardcoded to show specific examples

The focus is on learning how different data structures work together

You can modify the numbers and lists to see how the results change

This project shows how basic programming concepts come together to create a functional data handling system. It's a great starting point for understanding how real-world applications manage and process information.
alt="Image" src="https://github.com/user-attachments/assets/401443b3-50e1-4ddb-9330-d218f39cc0a7" /

<img width="1919" height="1079" alt="Image" src="https://github.com/user-attachments/assets/17bcbf8a-f957-4ded-9009-3c01d87dd163" />
