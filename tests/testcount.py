import sublime
import sys
from unittest import TestCase

version = sublime.version()

plugin = sys.modules["LaTeXWordCount.WordCount"]

class TestFunctions(TestCase):
  def test_basic(self):
    words, chars, length = plugin.basic_wordcount("as df")
    self.assertEqual(words, 2)
    self.assertEqual(chars, 4)
    self.assertEqual(length, 5)
