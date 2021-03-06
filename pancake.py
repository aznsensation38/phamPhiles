# Develop a program that acts as a point of sale interface for a small restaurant.
#######################################################################

def get_table_number(): 
    ''' Function queries and accepts the Table Number Input from the user.
        # Parameters: <none>
        # returns int <table_num>
    '''
    table_num = int(input("\nTable number: "))
    return table_num

def get_number_of_diners_at_table():
    ''' Prompts user to enter the number of diners at this table; collects and returns the user's input.
        # Parameters: <none>
        # returns int <num_of_diners>
    '''                           
    num_of_diners = int(input("Number of diners: "))
    return num_of_diners

def get_table_order(number_of_diners):
    ''' Function calculates the total of all diners (total of table) after tax.
        Calls get_diner_order for each diner at this table.
        Calls display_diners_totals, calls display_table_total_info,
        Computes and returns the grand total for the whole table including tip
        # Parameters: int <number_of_diners>
        # returns float <tbl_grand_total> 
    '''         
    tbl_total_before_tax = 0.0
    query_each_diner = number_of_diners

    # While Loop to cycle through each diner at a table to get the table's pre-tax total
    while query_each_diner > 0 :
        print("\nDiner # " + str(query_each_diner) + " what is your order? ")
        tbl_total_before_tax = get_diner_order() + tbl_total_before_tax
        query_each_diner = query_each_diner - 1  

    tbl_total_after_tax = calculate_table_total(tbl_total_before_tax)
    tbl_grand_total = display_table_total_info(tbl_total_after_tax)
    display_diners_totals(tbl_total_before_tax, tbl_total_after_tax, tbl_grand_total)
    
    return tbl_grand_total
    
def get_diner_order():
    ''' Function calculates the before tax total cost for the diners
        Calls display_menu_of_food_items, and then calls get_menu_item as many times as needed to 
        collect the items ordered by this diner while accumulating the total of the item prices; 
        # Parameters: <none>
        # returns the float <diner_total_cost_before_tax>
    '''                         
    diner_total_cost_before_tax = 0.0
    print("\nMENU")
    display_menu_of_food_items()
    order_boolean = str(input("\nDo you want to order an item? Answer y or n: ")).lower()
    
    while order_boolean != 'y' and order_boolean != 'n':
        order_boolean = str(input("Please use a 'y' or 'n' \nDo you want to order an item? Answer y or n: ")).lower()

    while order_boolean == 'y': 
        item_boolean = 'y'

        while item_boolean == 'y':
            menu_item = get_menu_item()    
            if menu_item == 1:
                menu_item_price = float(3.25)
            elif menu_item == 2:
                menu_item_price = float(4.00)
            elif menu_item == 3:
                menu_item_price = float(2.50)
            elif menu_item == 4:
                menu_item_price = float(1.25)
            elif menu_item == 5:
                menu_item_price = float(3.99)
            elif menu_item == 6:
                menu_item_price = float(1.25)
            elif menu_item == 7:
                menu_item_price = float(2.00)
            else :
                menu_item_price = float(0.00)
            diner_total_cost_before_tax = diner_total_cost_before_tax + menu_item_price
            
            item_boolean = str(input("Want to order another item? Answer y or n: ")).lower()
            
            while item_boolean != 'y' and item_boolean != 'n':
                item_boolean = str(input("Please use a 'y' or 'n' \nDo you want to order an item? Answer y or n: ")).lower()

            if item_boolean == 'n':
                order_boolean = 'n'  
    
    return diner_total_cost_before_tax      

def display_menu_of_food_items():
    ''' Function displays the menu or available food items
        # Parameters: <none>
        # returns <none>
    '''                              
    print("1) eggs             $3.25")
    print("2) bacon            $4.00")
    print("3) pancakes         $2.50")
    print("4) orange juice     $1.25")
    print("5) oatmeal          $3.99")
    print("6) milk             $1.25")
    print("7) donut            $2.00")
    return()
 
def get_menu_item():
    ''' Function prompts the user to enter a food item number from the menu; 
        Collects and returns the item number the diner is ordering.
        # Parameters: <none>
        # returns int <menu_item_number>
    '''                            
    menu_item_number = int(input("Enter a menu item number: ")) 
    while (menu_item_number < 1 or menu_item_number > 7):
        menu_item_number = int(input("Please try again. Enter a menu item number: "))
    
    return menu_item_number

def display_diners_totals(table_total_before_tax, table_total_after_tax, table_grand_total):     
    ''' Displays the before and after tax totals for each diner at this table.
        # Parameters: float <table_total_before_tax, table_total_after_tax, table_grand_total>
        # Returns: <none>
    '''
    print("\nTable Order Info: ")
    print("Total before taxes: $" + str(round(table_total_before_tax, 2)))
    print("Total after taxes: $" + str(round(table_total_after_tax, 2)))
    print("The grand total (including tip) for the table is: $" + str(round(table_grand_total, 2)))
    return()         

def calculate_table_total(table_total_before_taxes):    
    ''' Calculates and returns the after tax total for the table. Use sales tax = 8%
        # Parameters: float <table_total_before_taxes>
        # Returns: float <table_total_after_tax_tip>
    '''                          
    table_total_after_tax = table_total_before_taxes * 1.08
    
    return table_total_after_tax  # returns the grand total

def display_table_total_info(table_total_after_taxes):
    ''' Description: Displays the list of suggested tip amounts based on the input table total value. 
        Prompts the user to enter the tip amount, collects it and adds it to the table total after tax. 
        Display the grand_total amount after adding the total with tip amount. Returns the grand total. 
        # Parameters: float <table_total_after_taxes>
        # Returns: float <grand_total>
    '''
    calc_10 = round((table_total_after_taxes * .1), 2)
    calc_15 = round((table_total_after_taxes * .15), 2)
    calc_20 = round((table_total_after_taxes * .2), 2)
    calc_25 = round((table_total_after_taxes * .25), 2)
    text_10 = ("10% tip:   $" + str(calc_10))
    text_15 = ("15% tip:   $" + str(calc_15))
    text_20 = ("20% tip:   $" + str(calc_15))
    text_25 = ("25% tip:   $" + str(calc_15))
    print("\nSuggested tip amounts based on your total table amount of: $" + str(round(table_total_after_taxes, 2)))
    print(text_10)
    print(text_15)
    print(text_20)
    print(text_25)
    tip_chosen = float(input("\nWhat tip amount would you like to leave?: $"))
    
    grand_total = table_total_after_taxes + tip_chosen                       
    
    return(grand_total)

def main(): 
    ''' Description: Repeatedly calls get_table_number, get_number_of_diners_at_table and 
        get_table_order until the user reports that there are no more tables for today, 
        while accumulating the total sales for the day; then outputs the total sales for the day.
        # Parameters: <none>
        # Returns: <nothing> 
    '''
    total_sales_for_day = 0.0
    tab_num_boolean = 'y'

    while tab_num_boolean == 'y':

        tab_num_boolean = input("\nDo you want to enter table orders for the day? Answer y or n: ").lower()

        while tab_num_boolean != 'y' and tab_num_boolean != 'n':
            tab_num_boolean = str(input("Please use a 'y' or 'n' \nDo you want to enter table orders for the day? Answer y or n: ")).lower()

        while tab_num_boolean == 'y':
            table_number = get_table_number()                           
            number_of_diners = get_number_of_diners_at_table()
            total_sales_for_day = total_sales_for_day + get_table_order(number_of_diners)

            tab_num_boolean = input("\nDo you want to enter another table order for the day? Answer y or n: ").lower()

            while tab_num_boolean != 'y' and tab_num_boolean != 'n':
                tab_num_boolean = str(input("Please use a 'y' or 'n' \nDo you want to enter another table order for the day? Answer y or n: ")).lower()
        
    print("\nTotal Sales for the day: $" + str(round(total_sales_for_day,2)) + "\n")


main()


