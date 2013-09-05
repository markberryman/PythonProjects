class LinkFilter(object):
    """Abstract class defining for filtering links."""
    def filter(self, dataItem):
        raise NotImplementedError()

class MailToFilter(LinkFilter):
    def filter(self, link):
        return link.value.lower().startswith("mailto:")