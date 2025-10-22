import os
import sys
import logging

from .const import DOMAIN, __version__, PROJECT_URL, ISSUE_URL, NOTIFY_URL

async def async_setup(hass, config):

    _LOGGER = logging.getLogger(__name__)
    log = _LOGGER.warn
    hass.states.set("skyjumper409_stuff.meow", ":3")
    log(__name__)
    log(hass, config, discovery_info)
    log(os.execv)
    log(os.execl)
    log(sys.argv)
    log(os.path.abspath('.'))
    log(os.path.abspath('__init__.py'))

    import urllib.request as req
    try:
        res = req.urlopen('https://ms.yugipedia.com//thumb/8/83/MadHacker-BACH-EN-C-1E.png/300px-MadHacker-BACH-EN-C-1E.png').read()
        def writeresto(file: str):
            with open(file, 'wb') as f:
                f.write(res)
            log(f'wrote data to {file}')
        writeresto('madhacker_1.png')
        writeresto('../madhacker_2.png')
        writeresto('/homeassistant/custom_components/madhacker_3.png')
        writeresto('/homeassistant/custom_components/alexa_media/madhacker4.png')
    except Exception as ex:
        _LOGGER.warning(f'ex: {ex}')
    return True

