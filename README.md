Overview
The Segment Python SDK provides a simple and flexible way to integrate with Segment's analytics API. The SDK allows you to easily track events, identify users, manage page and screen views, associate users with groups, and handle user aliases. It is designed with decorators that can be applied to your functions to automatically send analytics data to Segment.


Installation
To use this SDK, you can simply include it in your Python project. Ensure you have the necessary dependencies installed:
pip install requests


Initialization
Before using the SDK, you need to initialize the SegmentClient with the base URL of your Segment API server. This should be done once during the setup of your application.

from decorators import init_segment_client
init_segment_client(base_url="http://localhost:8000")


Usage
1. Tracking Events
Use the @track_event decorator to automatically send event tracking data after a function is called. You can specify the event name and the user ID field.

from decorators import track_event
@track_event(event_name="User Signed Up")
def signup(user_id, username):
    print(f"User {username} signed up")


2. Identifying Users
Use the @identify decorator to automatically send user identification data after a function is called.

from decorators import identify
@identify()
def update_profile(user_id, traits):
    print(f"Updating profile for user {user_id}")


3. Tracking Page Views
Use the @page decorator to track page views.

from decorators import page
@page(name_field="page_name")
def view_page(user_id, page_name):
    print(f"User {user_id} viewed page {page_name}")


4. Tracking Screen Views
Use the @screen decorator to track screen views in mobile applications.

from decorators import screen
@screen(name_field="screen_name")
def view_screen(user_id, screen_name):
    print(f"User {user_id} viewed screen {screen_name}")


5. Grouping Users
Use the @group decorator to associate users with groups.

from decorators import group
@group(group_id_field="group_id")
def assign_group(user_id, group_id):
    print(f"User {user_id} assigned to group {group_id}")


6. Aliasing Users
Use the @alias decorator to alias users.

from decorators import alias
@alias(previous_id_field="old_id")
def merge_users(old_id, new_id):
    print(f"User {old_id} merged into user {new_id}")


7. Flushing Events
Use the @flush decorator to flush the SegmentClient after a function is called.

from decorators import flush
@flush()
def complete_batch():
    print("Batch processing completed")


Client Methods
SegmentClient Methods
The SegmentClient class contains the following methods that can be called directly:

identify: Identify a user.
track_event: Track an event.
page: Track a page view.
screen: Track a screen view.
group: Associate a user with a group.
alias: Alias a user.
flush: Flush all pending events.
Each method takes in the necessary parameters, including user IDs, event names, and additional properties or context.


Example of Direct Client Usage

from client import SegmentClient
client = SegmentClient(base_url="http://localhost:8000")
client.identify(user_id="12345", traits={"email": "user@example.com"})
client.track_event(user_id="12345", event="User Logged In", properties={"method": "email"})


Error Handling
The SDK will raise HTTP exceptions if any requests fail. Make sure to handle these exceptions in your application to ensure graceful error recovery.

try:
    client.track_event(user_id="12345", event="User Logged In")
except requests.exceptions.HTTPError as e:
    print(f"Failed to track event: {e}")

    
Conclusion
This Segment Python SDK is designed to make integrating with Segment's analytics API straightforward and efficient. With the use of decorators and direct client methods, you can easily incorporate robust tracking into your application.