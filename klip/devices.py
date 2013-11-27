# -*- coding: utf8 -*-


class OldGenKindle(object):
    noises = [
        "\xef\xbb\xbf",
        "\xe2\x80\x94",
        "\xc2\xa0",
        "\n",
    ]
    title = "([^\-].*)"
    author_in_title = "\((.*?)\)"
    # -" Note on Page 20 | Added on Monday, November 14, 2011, 10:27 AM
    type_info = "- (.*?)\|"
    time_format = "%A, %B %d, %Y, %I:%M %p"
    clip_type = "(Highlight|Note|Bookmark) "
    page = "Page ([0-9]{1,})"
    location = "Loc. ([0-9]+\-[0-9]+|[0-9]+) "
    added_on = "Added on (.*?)\n"
    content = "Added on .*?\n(.*)"


class Paperwhite(OldGenKindle):
    time_format = "%A, %B %d, %Y %I:%M:%S %p"
    clip_type = "Your (Highlight|Note|Bookmark) "
    location = "Location ([0-9]+\-[0-9]+|[0-9]+) "


class Touch(Paperwhite):
    pass
