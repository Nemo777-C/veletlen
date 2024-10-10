import re

#suppliers Tables
class SupplierValidator:
    def __init__(self):
        self.suppName_pattern = re.compile(r"^[a-zA-Z\s.]{2,100}$")
        self.suppContactName_pattern = re.compile(r"^[a-zA-Z\s]{2,100}$")
        self.suppAddress_pattern = re.compile(r"[a-zA-Z0-9\s-,]{5,255}$")

class ProductValidator:
    def __init__(self):
        self.prodName_pattern = re.compile(r"^[a-zA-Z0-9\s\-]{2,100}$")
        self.prodDescription_pattern = re.compile(r"^.{0,255}$")
        self.prodCategory_pattern = re.compile(r"^[a-zA-Z\s]{0,255}$")
        self.prodUnitPrice_pattern = re.compile(r"^\d+(\.\d{2})?|(\.\d{2})$")
        self.prodStockQuantity_pattern = re.compile(r"^\d+$")
        self.prodReorderLevel_pattern = re.compile(r"^\d+$")

#customers Tables
class CustomerValidator:
    def __init__(self):
        self.custName_pattern = re.compile(r"^[A-Za-z\s]{2,100}$")
        self.custContactName_pattern = re.compile(r"^[A-Za-z\s]{2,100}$")
        self.custAddress_pattern = re.compile(r"[a-zA-Z0-9\s-,]{5,255}$")

class OrdersValidator:
    def __init__(self):
        self.ordrDate_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}-$")
        self.ordrStatus_pattern = re.compile(r"^(Pending|Shipped|Delivered|Cancelled)$")
        self.ordrTotalAmount_pattern = re.compile(r"^\d+(\.\d{2})?|(\.\d{2})$")
        self.ordrShipDate_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}-$")


#COMMON expressions
email_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,}$")
phone_regex = re.compile(r"^\+1-\d{3}-\d{3}-\d{4}$")
sku_regex = re.compile(r"^[a-zA-Z0-9\-]{3,15}$")

