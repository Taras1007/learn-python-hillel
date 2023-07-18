from FileProcessor import read_file
class Event:
    def __init__(self):
        self.date = read_file("date")
        self.time = read_file("time")
        self.sku = read_file("sku")
        self.warehouse = read_file("warehouse")
        self.warehouse_cell_id = read_file("warehouse_cell_id")
        self.operation = read_file("operation")
        self.invoice = read_file("invoice")
        self.expiration_date = read_file("expiration_date")
        self.operation_cost = read_file("operation_cost")
        self.comment = read_file("comment")
n = Event()