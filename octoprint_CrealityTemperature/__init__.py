# coding=utf-8

import octoprint.plugin
import re

class CrealityTemperaturePlugin(octoprint.plugin.OctoPrintPlugin):
	def log(self, comm_instance, line, *args, **kwargs):
		if re.match("^(ok)?\s*==T", line):
			fix = re.sub("==", "", line)
			return fix
		return line

__plugin_name__ = "Creality Temperature Fix"
def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = CrealityTemperaturePlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.comm.protocol.gcode.received": __plugin_implementation__.log
	}
