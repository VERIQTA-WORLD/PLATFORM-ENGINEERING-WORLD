def migrate(connection):
    columns = {row[1] for row in connection.execute("PRAGMA table_info(customers)")}
    with connection:
        if "display_name" not in columns:
            connection.execute("ALTER TABLE customers ADD COLUMN display_name TEXT")
        connection.execute("UPDATE customers SET display_name=name WHERE display_name IS NULL")
