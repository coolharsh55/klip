# -*- coding: utf8 -*-


import datetime

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from klip import load, load_from_file


class KlipTests(unittest.TestCase):

    def setUp(self):
        self.clip_datas = None

    def _get_clip_datas(self):
        if not self.clip_datas:
            clip_datas = []

            # kindle paperwhite
            clip_data = load_from_file('tests/paperwhite_clippings.txt')
            clip_datas.append(clip_data)

            # old gen kindles
            clip_data = load_from_file('tests/old_gen_kindle_clippings.txt', device="OldGenKindle")
            clip_datas.append(clip_data)

            # kindle touch
            clip_data = load_from_file('tests/touch_clippings.txt', device="Touch")
            clip_datas.append(clip_data)

            self.clip_datas = clip_datas

        return self.clip_datas

    def test_load(self):
        clip_datas = self._get_clip_datas()
        for _clip_data in clip_datas:

            # type control
            assert isinstance(_clip_data, list), "invalid type for clip_data"

        # len control
        self.assertEqual(len(clip_datas[0]), 3)
        self.assertEqual(len(clip_datas[1]), 4)
        self.assertEqual(len(clip_datas[2]), 2)

    def test_authors(self):

        clip_data = self._get_clip_datas()

        for item in clip_data[0]:
            assert(item["author"] in ["Daniel Greenfeld;Audrey Roy", "Frederick P. Brooks"])

        for item in clip_data[1]:
            assert(item["author"] in ["Mark Lutz", "Timu Eren"])

        for item in clip_data[2]:
            assert(item["author"] in ["Jan Goyvaerts and Steven Levithan", "Didier Drogba"])

    def test_books(self):
        clip_data = self._get_clip_datas()

        for item in clip_data[0]:
            assert(item["title"] in ["The Mythical Man Month", "Two Scoops of Django: Best Practices for Django 1.5"])

        for item in clip_data[1]:
            assert(item["title"] in ["Learning_Python_Fourth_Edition", "Learning_Python_Second_Edition"])

        for item in clip_data[2]:
            assert(item["title"] in ["Regular Expressions Cookbook", "Das Kapital"])

    def test_content(self):
        clip_data = self._get_clip_datas()

        for item in clip_data[0]:
            self.assertIsNotNone(item["content"])
            assert len(item["content"]) > 10

        for item in clip_data[1]:
            self.assertIsNotNone(item["content"])
            assert len(item["content"]) > 10

        for item in clip_data[2]:
            self.assertIsNotNone(item["content"])
            assert len(item["content"]) > 10

    def test_added_on(self):
        clip_data = self._get_clip_datas()

        for item in clip_data[0]:
            self.assertIsNotNone(item["added_on"])
            assert isinstance(item["added_on"], datetime.datetime)

        for item in clip_data[1]:
            self.assertIsNotNone(item["added_on"])
            assert isinstance(item["added_on"], datetime.datetime)

        for item in clip_data[2]:
            self.assertIsNotNone(item["added_on"])
            assert isinstance(item["added_on"], datetime.datetime)

    def test_location(self):
        clip_data = self._get_clip_datas()

        self.assertEqual(clip_data[0][0]["meta"]["location"], '181-182')
        self.assertEqual(clip_data[2][0]["meta"]["location"], '391')

    def test_page(self):
        clip_data = self._get_clip_datas()

        self.assertEqual(clip_data[1][0]["meta"]["page"], 20)
        self.assertEqual(clip_data[2][1]["meta"]["page"], 41)

    def test_type(self):
        clip_data = self._get_clip_datas()

        self.assertEqual(clip_data[0][2]["meta"]["type"], "Highlight")
        self.assertEqual(clip_data[2][0]["meta"]["type"], "Note")


if __name__ == '__main__':
    unittest.main()