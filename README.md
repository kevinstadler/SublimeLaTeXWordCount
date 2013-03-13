## LaTeX Word Count

A SublimeText 2 word and character count plugin for LaTeX and plaintext files, based on [string_counter](https://github.com/naomichi-y/string_counter) by Naomichi Yamakita.

### Usage

Install LaTeX Word Count automatically via Sublime Package Control: http://wbond.net/sublime_packages/package_control

Go to Tools -> Word Count to display word, character and line counts for the current selection, or for the entire file if nothing is selected.

The default key binding is _Control + Shift + C_

### LaTeX support

The main purpose of this plugin was to support reliable word counts for files with LaTeX markup. The plugin ignores the preamble, abstract, formulas, captions, and supports excluding headers, footnotes and appendices. Have a look at the available config options in Sublime Text 2 -> Preferences -> Package Settings -> LaTeX Word Count to customise what gets counted.

### Suggestions

 * Adding support for other markup languages should be pretty straightforward, just have a look at https://github.com/lionandoil/LaTeXWordCount/blob/master/SublimeWordCount.py#L42 and chip in!
 * A real-time word count displayed in the status bar a la [WordCount](https://github.com/titoBouzout/WordCount) would be nice and not too hard to implement. If anyone's actually using this plugin and would like this feature just let me know and I'll add it!
 * SublimeText's scope_name() function could potentially be used to produce more robust stripping of LaTeX commands than the current regexp-wizardry.

### License
Released under the [MIT License](http://opensource.org/licenses/MIT)
