## LaTeX Word Count <a href="https://packagecontrol.io/packages/LaTeX%20Word%20Count"><img src="https://packagecontrol.herokuapp.com/downloads/LaTeX%20Word%20Count.png"></a>

A [Sublime Text](https://www.sublimetext.com) word and character count plugin for LaTeX and plaintext files.

### Usage

LaTeX Word Count can be installed easily using [Sublime Text Package Control](https://packagecontrol.io/).

Go to `Tools -> Word Count` to display word, character and line counts for the current selection, or for the entire file if nothing is selected.

The default key binding is `Control + Shift + C`

### LaTeX support

The main purpose of this plugin was to support reliable word counts for files with LaTeX markup. The plugin ignores the preamble, abstract, formulas, captions, and supports excluding headers, footnotes and appendices. Have a look at the available config options in `Preferences -> Package Settings -> LaTeX Word Count` to customise what gets counted.

### Suggestions

- Adding support for other ST-recognised markup languages should be pretty straightforward, have a look [here](https://github.com/kevinstadler/SublimeLaTeXWordCount/blob/master/WordCount.py#L64) to see how it's done for LaTeX and chip in!
- A real-time word count displayed in the status bar a la [WordCount](https://github.com/titoBouzout/WordCount) would be nice and not too hard to implement. If anyone's actually using this plugin and would like this feature just let me know and I'll add it!
- Sublime Text's `scope_name()` function could potentially be used to produce more robust stripping of LaTeX commands than the current regexp-wizardry.

### License

This plugin combines [a simple LaTeX word count python script](https://github.com/kevinstadler/bash-scripts/blob/master/wclatex) that I wrote in 2009, the basic plugin structure taken from Naomichi Yamakita's [string_counter](https://github.com/naomichi-y/string_counter), as well as changes and fixes submitted by [GitHub contributors](https://github.com/kevinstadler/SublimeLaTeXWordCount/graphs/contributors).

Released under the [MIT License](http://opensource.org/licenses/MIT)
