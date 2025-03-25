rows = 5  # Number of rows

for i in range(1, rows + 1):
    space = rows - i  # Number of spaces
    star = i  # Number of stars
    
    print(f"space = {space}, star = {star} -> ", end="")  
    print(" " * space + "* " * star)  # Printing spaces and stars


# output:
# space = 4, star = 1 ->     * 
# space = 3, star = 2 ->    * * 
# space = 2, star = 3 ->   * * * 
# space = 1, star = 4 ->  * * * * 
# space = 0, star = 5 -> * * * * * 