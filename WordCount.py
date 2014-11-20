import sublime
import sublime_plugin
import re

settings = None

def load_settings():
    global settings
    settings = sublime.load_settings("LaTeXWordCount.sublime-settings")

def plugin_loaded():
    load_settings()

load_settings()
settings.add_on_change('reload', lambda:load_settings())

if settings.get("ignore_numbers"):
    word = "[A-za-z-]+"
else:
    word = "[\w-]+"
word = re.compile(word, re.U)


def basic_wordcount(text):
    words = 0
    chars = 0
    for w in word.findall(text):
        words += 1
        chars += len(w)
    return words, chars, len(text)

# infrastructure for custom word counters for different markup languages
custom_wordcounters = {"Plain text": basic_wordcount}


def custom_wordcount(syntax,):
    def wrap(func):
        custom_wordcounters[syntax] = func
    return wrap

# custom word counters begin here!

# word counting functions should take a single string argument and
# return a triple of (words, characters, characters+spaces). ideally
# the function will just strip off any comments and markup and then
# call basic_wordcount() with the remaining cleaned-up string

latex_comment = re.compile("\n?%.*", re.MULTILINE)
latex_lformula = re.compile(r"\$\$.*?\$\$", re.MULTILINE | re.DOTALL)
latex_sformula = re.compile(r"\$.*?\$", re.MULTILINE)
latex_abstract = re.compile(
    r"\\begin\{abstract\}.*?\\end\{abstract\}", re.MULTILINE | re.DOTALL)
latex_header = re.compile(
    r"\\(part|chapter|(sub)*section|paragraph)\*?\{", re.MULTILINE)
latex_footnote = re.compile(r"", re.MULTILINE)
latex_command = re.compile(
    r"\\[A-Za-z]+((\s*\{[^\}]*?\})?(\s*\[.*?\])?(\s*\{.*?\})+)?\s*",
    re.MULTILINE | re.DOTALL)


@custom_wordcount("LaTeX")
def wordcount_latex(text):
    global settings
    latex_settings = settings.get("LaTeX")

    # strip latex comments
    text = latex_comment.sub(" ", text)

    # skip the preamble (if there is one)
    begin = text.find("\\begin{document}")
    if begin != -1:
        text = text[begin + 16:]

    if latex_settings.get("exclude_appendices"):
        appendix = text.find("\\appendix")
        if appendix != -1:
            text = text[:appendix]

    # strip formulas
    text = latex_lformula.sub(" ", text)
    text = latex_sformula.sub(" ", text)

    # remove abstract
    if latex_settings.get("exclude_abstract"):
        text = latex_abstract.sub("", text)

    # get started with commands
    # strip acceptable markup
    for cmd in latex_settings.get("markup_commands"):
        text = re.sub(r"\\" + cmd + r"\{", " ", text)

    if not latex_settings.get("exclude_headers"):
        # rescue section headers from beging purged
        text = latex_header.sub(" ", text)

    if not latex_settings.get("exclude_footnotes"):
        # rescue footnotes from being purged
        text = text.replace(r"\\footnote\{", " ")

    # get rid of all commands that are still left
    text = latex_command.sub(" ", text)

    text = text.replace("~", " ")
    text = text.replace("--", " ")
    text = text.replace("{", " ")
    text = text.replace("}", "")
    text = text.replace("\\", "")
    return basic_wordcount(text.strip())


find_language = re.compile(r"([\w -]+)\.tmLanguage").search


class LatexWordCountCommand(sublime_plugin.TextCommand):

    def description(self):
        return "Display word count"

    def run(self, edit):
        selected = self.view.sel()
        lines = len(self.view.lines(selected[0]))
        scope = "selected region"
        if len(selected) == 1 and selected[0].empty():
            selected = [sublime.Region(0, self.view.size())]
            lines = self.view.rowcol(self.view.size())[0] + 1
            scope = "entire file"

        # find any custom word counters
        language = find_language(self.view.settings().get("syntax")).group(1)
        wordcount_fn = custom_wordcounters.get(language)
        if wordcount_fn:
            language = "Using custom word counting for " + language
        else:
            language = "No custom support for " + \
                language + " syntax, treating file as plain text"
            wordcount_fn = basic_wordcount

        total_chars = 0
        words = 0
        chars = 0
        for region in selected:
            (rwords, rchars, rtotal) = wordcount_fn(self.view.substr(region))
            words += rwords
            chars += rchars
            total_chars += rtotal

        sublime.message_dialog('''\
Word count for %s

Words:\t\t\t\t\t\t%d
Characters (ignoring whitespace):\t%d
Characters (with whitespace):\t%d
Lines:\t\t\t\t\t\t%d

%s''' % (scope, words, chars, total_chars, lines, language))
