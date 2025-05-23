s={7,17,12, "harry", [1,2]}


# Error:
# This will raise:

# bash
# Copy
# Edit
# TypeError: unhashable type: 'list'
# Explanation:
# Python sets can only contain hashable (immutable) items.

# Lists are mutable and therefore unhashable, so they can't be added to a set.

# Valid types for set elements include: int, str, float, tuple (if the tuple contains only hashable items), etc.

# Fix:
# If you want to include [1, 2], convert it to a tuple:

# python
# Copy
# Edit
# s = {7, 17, 12, "harry", (1, 2)}
# Would you like a quick explanation of hashable vs unhashable types in Python?








