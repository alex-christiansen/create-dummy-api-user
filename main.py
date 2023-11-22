import looker_sdk
from looker_sdk import models

# For this to work you must either have set environment variables or created a looker.ini as described below in "Configuring the SDK"
sdk = looker_sdk.init40()  
user_first_name = "API User"
user_last_name = "No Email"

# Create API Only user with no email and get user_id 
new_user = sdk.create_user(
    body=models.WriteUser(
        first_name=user_first_name,
        is_disabled=False,
        last_name=user_last_name
    )
)
# Get admin role ID
admin_role_id = sdk.search_roles(fields="id",name="Admin")[0].id
# Give admin role to new user
sdk.set_user_roles(user_id=new_user.id,body=[admin_role_id])
# Get api creds for new user
api_creds = sdk.create_user_credentials_api3(user_id=new_user.id)

print_string = f""" 
New User Created with the following characters, save off API creds or view under /admin/next/users
User Name: {user_first_name} {user_last_name}
User ID: {new_user.id}
User Role: Admin
User API Client ID: {api_creds.client_id}
User API Client Secret: {api_creds.client_secret}
"""

print(print_string)