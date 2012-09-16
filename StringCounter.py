import sublime, sublime_plugin
import locale
 
class StringcounterCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    count = 0
    
    for region in self.view.sel():
      count += len(self.view.substr(region))

      if count == 0:
          count = self.view.size()
    
    locale.setlocale(locale.LC_ALL, "")
    sublime.status_message("Count: " + locale.format("%d", count, grouping=True))
    