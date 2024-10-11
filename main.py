# mention ldh rule for email domain
# check bout latin char in name ascii/unicode
# https://regex101.com/
import re


# suppliers Tables
def supplier_validation(supplier_name, contact_name, phone, email, address):
    supres = {
        "supplier_name": True,
        "contact_name": True,
        "phone": True,
        "email": True,
        "address": True,
    }

    supplier_name_pattern = re.compile(r"^[a-zA-Z\s.]{2,100}$")
    if supplier_name and not supplier_name_pattern.match(supplier_name):
        res["supplier_name"] = False

    contact_name_pattern = re.compile(r"^[a-zA-Z\s-]{2,100}$")
    if contact_name and not contact_name_pattern.match(contact_name):
        res["contact_name"] = False

    phone_pattern = re.compile(r"^\+1-\d{3}-\d{3}-\d{4}$")
    if phone and not phone_pattern.match(phone):
        res["phone"] = False

    email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,}$")
    if email and not email_pattern.match(email):
        res["email"] = False

    address_pattern = re.compile(r"^[a-zA-Z0-9\s\-,]{5,255}$")
    if address and not address_pattern.match(address):
        res["address"] = False

    return res


supplier_name = "Example Supplier"
contact_name = "John Doe"
phone = "+1-123-456-7890"
email = "example@example.com"
address = "123 Main St, Anytown, USA"

validation_results = supplier_validation(supplier_name, contact_name, phone, email, address)

print("Validation Results:")
for field, result in validation_results.items():
    print(f"{field}: {result}")
