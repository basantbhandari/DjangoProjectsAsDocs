from django.dispatch import Signal, receiver

# creating Signals
notification = Signal(providing_args=["request", "user"])

# Receiver Function


@receiver(notification)
def show_notification(sender, **kwargs):
    print(sender)
    print(f"kwargs : {kwargs}")
    print("...............Notification..........")
