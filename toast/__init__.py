from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def notify(self, title, description=None, icon=None):
        """
        :param title: The title used for the toast notification, usually the most prominent
        :type title: str
        :param description: The description/subtitle for the notification, less prominent
        :type description: str
        :param icon: Currently not supported
        :type icon: str
        :return: Nothing
        """
        pass


class NotifydNotifier(Notifier):
    """
    Notifier for systems that support d-bus notification daemons
    """

    def notify(self, title, description=None, icon=None):
        import notify2
        notify2.init("PYTOAST")
        notify2.Notification(title, description).show()


class WindowsNotifier(Notifier):
    """
    Notifier for win10 systems.
    """

    def notify(self, title, description=None, icon=None):
        from win10toast import ToastNotifier
        notifier = ToastNotifier()
        notifier.show_toast(title, description, duration=4)


def notify(title, description=None, icon=None):
    import os
    notifier = WindowsNotifier if os.name == "nt" else NotifydNotifier
    notifier().notify(title, description, icon)
