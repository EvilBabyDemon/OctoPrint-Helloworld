# OctoPrint-Helloworld

**TODO:** Describe what your plugin does.

Kinda stole the hello world plugin tutorial and just changed a few things to have links to other 3D printers at the top.


## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/EvilBabyDemon/OctoPrint-Helloworld/archive/main.zip

**TODO:** Describe how to install your plugin, if more needs to be done than just installing it via pip or through
the plugin manager.

Don't think so?

## Configuration

**TODO:** Describe your plugin's configuration options (if any).

Under Settings -> Plugins -> Name of this Plugin: You can set the link, name and the colour.


## Why is this plugin called HelloWorld?

Well I stole the HelloWorld plugin and am too lazy to rename at this point. And quite frankly I am unsure how.


## What is not just tutorial?

Things I actually changed:

__init__.py
- Added more default entries.

helloworld_navbar.jinja2 
- Changed it to make it possible to change colour and also text

helloworld_settings.jinja2
- Added more fields for colour and text and also a 2nd link
