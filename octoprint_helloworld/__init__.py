# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin

class HelloWorldPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin):
    def on_after_startup(self):
        self._logger.info("Hello World!")

    def get_settings_defaults(self):
        return dict(url="https://en.wikipedia.org/", text="Text", colour="color: \#FFFFFF", url2="https://en.wikipedia.org/", text2="Text2", colour2="color: \#FFFFFF")


    def get_template_configs(self):
    	return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
    	]

__plugin_name__ = "Hello World"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = HelloWorldPlugin()

