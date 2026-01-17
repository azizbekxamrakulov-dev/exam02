def format_name(full_name):
    parts = full_name.split()
    if len(parts) < 2:
        return full_name  # Return as is if there's no last name or middle name
    last_name = parts[0]
    first_and_middle = ' '.join(parts[1:])
    return f"{first_and_middle}, {last_name}"
print(format_name("John Michael Doe"))
# "Michael Doe, John"print(format_name("Jane Smith"))
# "Smith, Jane"
format_name("Aliyev Vali G'aniyevich")
# "Vali G'aniyevich, Aliyev"
print(format_name("John Michael Doe"))
print(format_name("Jane Smith"))