from plyer import notification

title = 'Drinking Water Reminder'
message = 'You know what to do'

notification.notify(
    title=title,
    message=message,
    app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
    timeout=10,  # seconds
)
