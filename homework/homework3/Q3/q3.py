
# Modifying and refactoring the code by removing parentheses
def apply_discount(price: int, discount: float = 0.0) -> int:
    """
    Apply Discount Percent and Calculate Final Price
    """
    final_price = int(price*(1-discount))
    assert  0 < final_price <= price, "why this AssertionError never Raised!"

    return final_price


# print(apply_discount(3,2))

# Rewrite the code without using assert
def apply_discount2(price: int, discount: float = 0.0) -> int:
    """
    Apply Discount Percent and Calculate Final Price
    """
    final_price = int(price*(1-discount))
    
    if not (0 < final_price <= price):
        raise ValueError("Final price is not within the expected range")

    return final_price

print(apply_discount2(3,2))