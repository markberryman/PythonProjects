class LinkAnalysisUtility:
    @staticmethod
    def is_link_relative(link):
        isRelative = not link.lower().startswith("http")

        return isRelative


