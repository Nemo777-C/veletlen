import re


class ValidationError(Exception):
    pass

# Define validation functions
def validate_name(name):
    """Validate name (alphanumeric, max 50 characters, allowing Unicode characters)"""
    pattern = re.compile(r'^[a-zA-Z0-9-\s\u00C0-\u017F]{1,50}$', re.U)
    return bool(pattern.match(name))

def validate_phone(phone):
    """Validate phone number (more flexible format)"""
    pattern = re.compile(r'^\+?\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')
    return bool(pattern.match(phone))

def validate_email(email):
    """Validate email format (using LDH rule)"""
    pattern = re.compile(r'^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(pattern.match(email))

def validate_address(address):
    """Validate address (more flexible format)"""
    pattern = re.compile(r'^[a-zA-Z0-9\s\-,.]{5,255}$')
    return bool(pattern.match(address))

def validate_sku(sku):
    """Validate SKU (more flexible format)"""
    pattern = re.compile(r'^[a-zA-Z0-9\-]{3,20}$')
    return bool(pattern.match(sku))

def validate_category(category):
    """Validate category (more flexible format)"""
    pattern = re.compile(r'^[a-zA-Z0-9&\s]{0,20}$')
    return bool(pattern.match(category))

def validate_unit_price(unit_price):
    """Validate unit price (numeric, greater than 0)"""
    try:
        price = float(unit_price)
        return price > 0
    except ValueError:
        return False

def validate_quantity(quantity):
    """Validate quantity (integer, greater than or equal to 0)"""
    try:
        quantity = int(quantity)
        return quantity >= 0
    except ValueError:
        return False

def validate_order_status(order_status):
    """Validate order status (one of ('Pending', 'Shipped', 'Delivered', 'Cancelled'))"""
    return order_status in ['Pending', 'Shipped', 'Delivered', 'Cancelled']

def validate_date(date):
    """Validate date format (YYYY-MM-DD)"""
    pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    return bool(pattern.match(date))

# Suppliers table
def supplier_validation(supplier_name, contact_name, phone, email, address):
    sup_res = {
        "supplier_name": True,
        "contact_name": True,
        "phone": True,
        "email": True,
        "address": True,
    }

    if supplier_name and not validate_name(supplier_name):
        sup_res["supplier_name"] = False
    if contact_name and not validate_name(contact_name):
        sup_res["contact_name"] = False
    if phone and not validate_phone(phone):
        sup_res["phone"] = False
    if email and not validate_email(email):
        sup_res["email"] = False
    if address and not validate_address(address):
        sup_res["address"] = False

    failed_validations = {key: value for key, value in sup_res.items() if not value}
    if failed_validations:
        raise ValidationError(f"Supplier validation failed: {failed_validations}")

    return sup_res

# Products table
def product_validation(product_name, sku, description, category, unit_price, quantity_in_stock, reorder_level):
    pro_res = {
        "product_name": True,
        "sku": True,
        "description": True,
        "category": True,
        "unit_price": True,
        "quantity_in_stock": True,
        "reorder_level": True,
    }

    if product_name and not validate_name(product_name):
        pro_res["product_name"] = False
    if sku and not validate_sku(sku):
        pro_res["sku"] = False
    if description and len(description) > 255:
        pro_res["description"] = False
    if category and not validate_category(category):
        pro_res["category"] = False
    if unit_price and not validate_unit_price(unit_price):
        pro_res["unit_price"] = False
    if quantity_in_stock and not validate_quantity(quantity_in_stock):
        pro_res["quantity_in_stock"] = False
    if reorder_level and not validate_quantity(reorder_level):
        pro_res["reorder_level"] = False

    failed_validations = {key: value for key, value in pro_res.items() if not value}
    if failed_validations:
        raise ValidationError(f"Product validation failed: {failed_validations}")

    return pro_res

# Customers table
def customer_validation(customer_name, contact_name, phone, email, address):
    cus_res = {
        "customer_name": True,
        "contact_name": True,
        "phone": True,
        "email": True,
        "address": True,
    }

    if customer_name and not validate_name(customer_name):
        cus_res["customer_name"] = False
    if contact_name and not validate_name(contact_name):
        cus_res ["contact_name"] = False
    if phone and not validate_phone(phone):
        cus_res["phone"] = False
    if email and not validate_email(email):
        cus_res["email"] = False
    if address and not validate_address(address):
        cus_res["address"] = False

    if any(not valid for valid in cus_res.values()):
        raise ValidationError("Customer validation failed: " + str(cus_res))

    failed_validations = {key: value for key, value in cus_res.items() if not value}
    if failed_validations:
        raise ValidationError(f"Customer validation failed: {failed_validations}")

    return cus_res

# Orders table
def order_validation(order_date, order_status, total_amount, shipped_date):
    ord_res = {
        "order_date": True,
        "order_status": True,
        "total_amount": True,
        "shipped_date": True
    }

    if order_date and not validate_date(order_date):
        ord_res["order_date"] = False
    if order_status and not validate_order_status(order_status):
        ord_res["order_status"] = False
    if total_amount and not validate_unit_price(total_amount):
        ord_res["total_amount"] = False
    if shipped_date and not validate_date(shipped_date):
        ord_res["shipped_date"] = False

    if any(not valid for valid in ord_res.values()):
        raise ValidationError("Order validation failed: " + str(ord_res))

    failed_validations = {key: value for key, value in ord_res.items() if not value}
    if failed_validations:
        raise ValidationError(f"Order validation failed: {failed_validations}")

    return ord_res
