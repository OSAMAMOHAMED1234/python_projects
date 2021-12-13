from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast(
  'Notification Title1',
  'Notification Body',
  icon_path=None,
  duration=10,
  threaded=True
)


from plyer import notification
notification.notify(
  title='Notification Title2',
  message='Notification Body',
  app_icon=None,
  timeout=10,
)