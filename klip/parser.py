# -*- coding: utf-8 -*-

import re
import datetime
import time

import devices


class ClippingLoader(object):

    ENTRY_SEPERATOR = "=" * 10

    def __init__(self, content=None, device="Paperwhite"):

        if isinstance(device, basestring):
            self.patterns = getattr(devices, device)()
        elif issubclass(device, devices.BaseKindle):
            self.patterns = device()

        if content:
            self.load_from_string(content)

    def load_from_string(self, data):
        self.clip_data = data
        self.chunks = self._save_chunks()

        self.parse()

    def load_file(self, _file):
        with open(_file, "r") as file_content:
            self.load_from_string(file_content.read())

        return self

    def _save_chunks(self):
        return self.clip_data.split(self.ENTRY_SEPERATOR)

    def get_title_and_author(self, item):
        title, author = '', ''

        title_pattern = re.search(self.patterns.title, item)

        if title_pattern:
            author_pattern = re.findall(self.patterns.author_in_title, title_pattern.group(1))
            if author_pattern:
                author = self.remove_noise(author_pattern[-1])
                title = self.remove_noise(title_pattern.group(1).replace("({})".format(author_pattern[-1]), ''))

        return title.strip(), author.strip()

    def get_added_on(self, item):
        added_on_pattern = re.search(self.patterns.added_on, item)
        if added_on_pattern:
            timestamp = time.strptime(added_on_pattern.group(1).strip(), self.patterns.time_format)
            _date = datetime.datetime.fromtimestamp(time.mktime(timestamp))

            return _date

    def remove_noise(self, data):
        for noise in self.patterns.noises:
            data = data.replace(noise, "")

        return data

    def get_content(self, item):
        content_pattern = re.search(self.patterns.content, item, flags=re.DOTALL | re.MULTILINE)
        if content_pattern:
            return self.remove_noise(content_pattern.group(1))

    def get_type_info(self, item):
        type_dict = {
            'type': None,
            'page': None,
            'location': None,
        }

        type_info_pattern = re.search(self.patterns.type_info, item)
        if type_info_pattern:
            type_info = type_info_pattern.group(1)

            # get the clip type, highlight or note.
            type_pattern = re.search(self.patterns.clip_type, type_info)

            if type_pattern:
                type_dict.update({
                    "type": type_pattern.group(1),
                })

                page_pattern = re.search(self.patterns.page, type_info)

                if page_pattern:
                    type_dict.update({
                        'page': int(page_pattern.group(2)),
                    })

                # location
                location_pattern = re.search(self.patterns.location, item)

                if location_pattern:
                    type_dict.update({
                        'location': location_pattern.group(1),
                    })

        return type_dict

    def parse(self):
        entries = []

        for chunk in self.chunks:
            if len(chunk) > 5:
                title, author = self.get_title_and_author(chunk)

                entries.append({
                    'meta': self.get_type_info(chunk),
                    'added_on': self.get_added_on(chunk),
                    'title': title,
                    'author': author,
                    'content': self.get_content(chunk),
                })

        self.parsed_data = entries


def load(content, device="Paperwhite"):
    clipper = ClippingLoader(content, device=device)
    return clipper.parsed_data


def load_from_file(file_name, device="Paperwhite"):
    clipper = ClippingLoader(device=device)
    clipper.load_file(file_name)
    return clipper.parsed_data
