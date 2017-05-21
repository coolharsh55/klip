class BaseKindle(object):
    '''Represents an abstract basic Kindle annotation'''

    # noise is characters that need to be removed
    noises = None
    # title of the book
    title = None
    # author of the book, specified in title
    author_in_title = None
    # type of annotation
    type_info = None
    # datetime format
    time_format = None
    # type of annotation
    clip_type = None
    # page in book
    page = None
    # location in book
    location = None
    # date of highlight
    added_on = None
    # content of annotation
    content = None


class OldGenKindle(BaseKindle):
    '''Kindle 1-4'''

    noises = [
        "\xef\xbb\xbf",
        "\xe2\x80\x94",
        "\xc2\xa0",
        "\n",
    ]
    title = "([^\-].*)"
    author_in_title = "\((.*?)\)"
    type_info = "- (.*?)\|"
    time_format = "%A, %B %d, %Y, %I:%M %p"
    clip_type = "(Highlight|Note|Bookmark) "
    page = "(p|P)age ([0-9]{1,})"
    location = "Loc. ([0-9]+\-[0-9]+|[0-9]+) "
    added_on = "Added on (.*?)\n"
    content = "Added on .*?\n(.*)"


class Kindle4(OldGenKindle):
    time_format = "%A, %d %B %y %H:%M:%S"
    added_on = "Added on (.+) GMT.*\n"


class Paperwhite(OldGenKindle):
    time_format = "%A, %B %d, %Y %I:%M:%S %p"
    clip_type = "Your (Highlight|Note|Bookmark) "
    location = "Location ([0-9]+\-[0-9]+|[0-9]+) "


class Touch(Paperwhite):
    pass
