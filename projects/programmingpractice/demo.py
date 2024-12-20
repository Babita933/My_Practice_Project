from bs4 import BeautifulSoup
import openpyxl

# Load the HTML file
with open('../Practice_project/Amazon.in _ iphone 13.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find all the required divs
divs = soup.find_all('div',
                     class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-vsom9k8yemr4u1yo82zayoamev s-latency-cf-section puis-card-border')

# Create a new Excel workbook and select the active worksheet
wb = openpyxl.Workbook()
ws = wb.active
ws.append(['Product_Name', 'Product_price', 'Product_reviews'])

# Extract the required information
for div in divs:
    try:
        product_name = div.find('span', class_='a-size-medium a-color-base a-text-normal').text.strip()
    except AttributeError:
        product_name = " "

    try:
        product_price = div.find('span', class_='a-price-whole').text.strip()
    except AttributeError:
        product_price = " "

    try:
        product_reviews = div.find('i', class_='a-icon a-icon-popover').text.strip()
    except AttributeError:
        product_reviews = " "

    # Append the data to the Excel sheet
    ws.append([product_name, product_price, product_reviews])

# Save the Excel file
wb.save('Amazon_Products.xlsx')
