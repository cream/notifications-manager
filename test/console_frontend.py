from cream.contrib.notifications import Frontend

NAME = 'org.cream.notifications.frontends.Console'
OBJECT = '/org/cream/notifications/frontends/Console'
CAPABILITIES = ()

class ConsoleFrontend(Frontend):
    def __init__(self):
        Frontend.__init__(self, NAME, OBJECT, CAPABILITIES)

        self.connect('show-notification', self.sig_show_notification)
        self.connect('hide-notification', self.sig_hide_notification)

    def sig_show_notification(self, frontend, n):
        s = '#%d: %s' % (n.id, n.app_name)
        print '=' * len(s)
        print s
        print '=' * len(s)
        if n.summary:
            print n.summary
        print
        if n.body:
            print n.body
            print
        image_data = n.image_data
        print 'Image data: %r' % image_data,
        if image_data:
            try:
                image_data.to_gtk_pixbuf().save('/tmp/image_data.png', 'png')
                print ' (saved to /tmp/image_data.png)'
            except Exception, e:
                print ' (error: %r)' % e
        else:
            print
        if n.hints:
            print 'Hints:'
            for key, value in n.hints.iteritems():
                if key in ('icon_data', 'image_data'):
                    print ' - %s: ...' % key
                else:
                    print ' - %s: %r' % (key, value)
        if n.actions:
            print 'Actions:'
            for key, displayed in n.actions:
                print ' - %s: %s' % (key, displayed)
        print '=' * len(s)

    def sig_hide_notification(self, frontend, n):
        print '#%d hidden' % n.id

if __name__ == '__main__':
    from dbus.mainloop.glib import DBusGMainLoop
    DBusGMainLoop(set_as_default=True)

    frontend = ConsoleFrontend()

    import gobject
    mainloop = gobject.MainLoop()
    mainloop.run()
