from functools import wraps

# Decorator for logging actions
def log_action(action_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[LOG] Performing action: {action_name}")
            try:
                result = func(*args, **kwargs)
                print(f"[LOG] Completed action: {action_name}\n")
                return result
            except Exception as e:
                print(f"[ERROR] Action '{action_name}' failed: {e}\n")
                raise
        return wrapper
    return decorator