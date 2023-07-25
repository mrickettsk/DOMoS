import os
import base64

try:
    # Encode the token using base64 encoding and store it in the auth variable
    auth = str(base64.b64encode(bytes(":" + os.environ["TOKEN"], "ascii")), "ascii")

    if os.environ.get("STORAGE_CONNECTION_STRING"):
        # Retrieve the storage connection string from the environment variables and store it in the storage_connection_string variable
        storage_connection_string = os.environ.get("STORAGE_CONNECTION_STRING")
        # Set the storage_account_name and storage_account_key variables to None if connection string is used
        storage_account_name = None
        storage_account_key = None
    else:
        # Retrieve the storage account name from the environment variables and store it in the storage_account_name variable
        storage_account_name = os.environ.get("STORAGE_ACCOUNT_NAME")
        # Retrieve the storage account key from the environment variables and store it in the storage_account_key variable
        storage_account_key = os.environ.get("STORAGE_ACCOUNT_KEY")
        # Set the storage_connection_string variable to None if account name and key are used
        storage_connection_string = None

    # Retrieve the table name from the environment variables and store it in the table_name variable
    storage_table_name = os.environ.get("STORAGE_TABLE_NAME")
except:
    raise exit("Error in environment variables")