
async def async_setup_platform(hass, config, add_devices_callback, discovery_info=None) -> bool:
    return True

async def async_setup_entry(hass, config_entry, async_add_devices) -> bool:
    """Set up the Alexa switch platform by config_entry."""
    return await async_setup_platform(
        hass, config_entry.data, async_add_devices, discovery_info=None
    )

async def async_unload_entry(hass, entry) -> bool:
    return True
