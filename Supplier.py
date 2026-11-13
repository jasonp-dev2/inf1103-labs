"""
Supplier class
    -Stores supplier information
    -Manages its own state
"""


class Supplier:
    def __init__(self, supplier_id: str, name: str, contact: str) -> None:
        self.__supplier_id: str = supplier_id
        self.__name: str = name
        self.__contact_email: str = contact

    def display_information(self) -> dict[str, str]:
        return {
            "ID": self.__supplier_id,
            "Name": self.__name,
            "Contact Email": self.__contact_email,
        }