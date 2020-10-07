def generate_sales_report(sales_report):
    """Generate sales report showing total melons each salesperson sold."""

    report = open(sales_report)

    sales_information = {}

    for line in report:
        line = line.rstrip()
        entries = line.split('|')

        salesperson = entries[0]
        total_sales = entries[1]
        melons_sold = entries[2]

        sales_information['salesperson'] = sales_information.get('salesperson', salesperson)
        # sales_information['salesperson']['total sales'] = sales_information['salesperson'].get('total sales', total_sales)
    
    return sales_information
             


# #Initiate an empty list for the names of salespeople.
# salespeople = []
# #Initiate an empty list for number of melons sold.
# melons_sold = []

# #Open a sales report into the variable f.
# f = open('sales-report.txt')
# #Look at the report line by line.
# #Strip white space from the right side of the report.
# #Tokenize the report lines using pipe as the delimeter.
# for line in f:
#     line = line.rstrip()
#     entries = line.split('|')
    
#     #The first item in each line is the salesperson.
#     salesperson = entries[0]
#     #The third item in each line is the number of melons sold.
#     melons = int(entries[2])

#     #If the salesperson on that line is already in the list of salespeople...
#     if salesperson in salespeople:
#         #use the index of the salesperson's name as a reference...
#         position = salespeople.index(salesperson)
#         #and add the new amount of melons to the existing list for melons_sold.
#         melons_sold[position] += melons
#     #If the salesperson on that line is NOT already in the list of salespeople...
#     else:
#         #Append the salesperson's name and number of melons sold to their respective lists.
#         salespeople.append(salesperson)
#         melons_sold.append(melons)

# #Line by line, print out the salesperson's name and number of melons sold.
# for i in range(len(salespeople)):
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')
