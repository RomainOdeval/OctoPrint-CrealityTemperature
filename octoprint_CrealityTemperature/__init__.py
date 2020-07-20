# -*- coding: utf-8 -*-
from __future__ import absolute_import

import octoprint.plugin
import re

class CrealityTemperaturePlugin(octoprint.plugin.OctoPrintPlugin):

	def log(self, comm_instance, line, *args, **kwargs):
		if re.match("^(ok)?\s*==T", line):
			fix = re.sub("==", "", line)
			return fix
		return line

	##~~ Softwareupdate hook
	def get_update_information(self):
		return dict(
			CrealityTemperature=dict(
				displayName=self._plugin_name,
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="RomainOdeval",
				repo="OctoPrint-CrealityTemperature",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/RomainOdeval/OctoPrint-CrealityTemperature/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "Creality Temperature"
__plugin_pythoncompat__ = ">=2.7,<4" # python 2 and 3

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = CrealityTemperaturePlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.comm.protocol.gcode.received": __plugin_implementation__.log,
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}
