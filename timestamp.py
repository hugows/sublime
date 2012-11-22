# import sublime, sublime_plugin

# class ExampleCommand(sublime_plugin.TextCommand):
#     def run(self, edit):
#         self.view.insert(edit, 0, "Hello, World!")

# -*- coding: utf-8 -*-

from datetime import datetime
import sublime, sublime_plugin


class MyTimestampCommand(sublime_plugin.EventListener):
    """Expand `isoD`, `now`, `datetime`, `utcnow`, `utcdatetime`,
       `date` and `time`
    """
    def on_query_completions(self, view, prefix, locations):
        if prefix in ('now'):
            formatted_date = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
            formatted_date += "\n" + len(formatted_date)*'-' + "\n"
            return [(prefix, prefix, formatted_date)]
        else:
            return []

