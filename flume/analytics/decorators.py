from functools import wraps
from .client import SegmentClient

segment_client = None

def init_segment_client(base_url: str):
    """
    Initialize the SegmentClient with the provided base_url.
    This should be called once in your application setup.
    """
    global segment_client
    segment_client = SegmentClient(base_url)

def track(user_id_field='user_id', event_name='Event Name'):
    """
    Decorator for tracking events.
    Automatically tracks an event with the given name after the decorated function is called.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if segment_client:
                user_id = kwargs.get(user_id_field)
                if user_id:
                    segment_client.track(user_id=user_id, event=event_name, properties=kwargs)
            return result
        return wrapper
    return decorator

def identify(user_id_field='user_id'):
    """
    Decorator for identifying users.
    Automatically sends an identify call after the decorated function is called.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if segment_client:
                user_id = kwargs.get(user_id_field)
                traits = kwargs.get('traits')
                if user_id:
                    segment_client.identify(user_id=user_id, traits=traits)
            return result
        return wrapper
    return decorator

def page(user_id_field='user_id', name_field='page_name'):
    """
    Decorator for tracking page views.
    Automatically sends a page call after the decorated function is called.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if segment_client:
                user_id = kwargs.get(user_id_field)
                name = kwargs.get(name_field)
                if user_id and name:
                    segment_client.page(user_id=user_id, name=name, properties=kwargs)
            return result
        return wrapper
    return decorator

def screen(user_id_field='user_id', name_field='screen_name'):
    """
    Decorator for tracking screen views.
    Automatically sends a screen call after the decorated function is called.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if segment_client:
                user_id = kwargs.get(user_id_field)
                name = kwargs.get(name_field)
                if user_id and name:
                    segment_client.screen(user_id=user_id, name=name, properties=kwargs)
            return result
        return wrapper
    return decorator

def group(user_id_field='user_id', group_id_field='group_id'):
    """
    Decorator for associating users with groups.
    Automatically sends a group call after the decorated function is called.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if segment_client:
                user_id = kwargs.get(user_id_field)
                group_id = kwargs.get(group_id_field)
                traits = kwargs.get('traits')
                if user_id and group_id:
                    segment_client.group(user_id=user_id, group_id=group_id, traits=traits)
            return result
        return wrapper
    return decorator

def alias(user_id_field='user_id', previous_id_field='previous_id'):
    """
    Decorator for aliasing users.
    Automatically sends an alias call after the decorated function is called.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if segment_client:
                previous_id = kwargs.get(previous_id_field)
                user_id = kwargs.get(user_id_field)
                if previous_id and user_id:
                    segment_client.alias(previous_id=previous_id, user_id=user_id)
            return result
        return wrapper
    return decorator

def flush():
    """
    Decorator for flushing the SegmentClient.
    Automatically sends a flush call after the decorated function is called.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if segment_client:
                segment_client.flush()
            return result
        return wrapper
    return decorator

# Example Usage:
# @track('User Signed Up')
# def signup(user_id, username):
#     print(f"User {username} signed up")
