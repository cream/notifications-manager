import pynotify
import gtk

if pynotify.init("My Application Name"):
    n = pynotify.Notification("Title", "message")
    n.set_urgency(pynotify.URGENCY_CRITICAL)
    n.set_timeout(pynotify.EXPIRES_NEVER)

    def _callback(notification, action, data):
        print '%r %r %r' % (notification, action, data)
    n.add_action("clicked", "Button yay", _callback, None)

    n.show()
else:
    print "there was a problem initializing the pynotify module"
