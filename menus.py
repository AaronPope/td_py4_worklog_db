from menu import Menu

main_menu = Menu({
        "A": "Add New Entry",
        "L": "Lookup Previous Entries",
        "C": "Clear Worklog",
        "Q": "---QUIT---"
})
    
lookup_menu = Menu({
        "D": "Date",
        "T": "Time Spent",
        "S": "Exact Search",
        "P": "Pattern Search",
        "B": "<--MAIN MENU---"
})
