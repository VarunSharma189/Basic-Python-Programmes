import functools

# Dummy function to get user permissions, replace with actual implementation
def get_current_user_permissions():
    # For example purposes, we'll return a list of permissions
    return ['admin', 'editor']

def requires_permission(permission):
    def decorator(func):
        @functools.wraps(func)  # This will preserve the original function metadata
        def wrapper(*args, **kwargs):
            user_permissions = get_current_user_permissions()  # Get current user permissions
            if permission in user_permissions:  # Check if the user has the required permission
                return func(*args, **kwargs)
            else:
                raise PermissionError("You do not have permission to access this resource.")
        return wrapper
    return decorator

@requires_permission('admin')
def delete_user(user_id):
    print(f"User {user_id} deleted")
        
try:
    delete_user(123)
except PermissionError as e:
    print(e)

print("THIS PROGRAM IS WRITTEN BY VARUN SHARMA ERP :- 0221BCA136")