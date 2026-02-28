import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_TYPE, UNIT_PERCENT, UNIT_CELSIUS, DEVICE_CLASS_BATTERY,
    DEVICE_CLASS_TEMPERATURE, STATE_CLASS_MEASUREMENT, ENTITY_CATEGORY_DIAGNOSTIC,
    ICON_BATTERY
)
from .. import WavinAHC9000

CONF_PARENT_ID = "wavinahc9000v3_id"
CONF_CHANNEL = "channel"

# Setup distinct base schemas for the different sensor types
BATTERY_SCHEMA = sensor.sensor_schema(
    unit_of_measurement=UNIT_PERCENT,
    device_class=DEVICE_CLASS_BATTERY,
    state_class=STATE_CLASS_MEASUREMENT,
    entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
    icon=ICON_BATTERY,
    accuracy_decimals=0,
)

TEMP_SCHEMA = sensor.sensor_schema(
    unit_of_measurement=UNIT_CELSIUS,
    device_class=DEVICE_CLASS_TEMPERATURE,
    state_class=STATE_CLASS_MEASUREMENT,
    accuracy_decimals=1,
)

CONFIG_SCHEMA = cv.typed_schema(
    {
        "battery": BATTERY_SCHEMA.extend({
            cv.GenerateID(CONF_PARENT_ID): cv.use_id(WavinAHC9000),
            cv.Required(CONF_CHANNEL): cv.int_range(min=1, max=16),
        }),
        "temperature": TEMP_SCHEMA.extend({
            cv.GenerateID(CONF_PARENT_ID): cv.use_id(WavinAHC9000),
            cv.Required(CONF_CHANNEL): cv.int_range(min=1, max=16),
        }),
        "comfort_setpoint": TEMP_SCHEMA.extend({
            cv.GenerateID(CONF_PARENT_ID): cv.use_id(WavinAHC9000),
            cv.Required(CONF_CHANNEL): cv.int_range(min=1, max=16),
        }),
        "floor_temperature": TEMP_SCHEMA.extend({
            cv.GenerateID(CONF_PARENT_ID): cv.use_id(WavinAHC9000),
            cv.Required(CONF_CHANNEL): cv.int_range(min=1, max=16),
        }),
        "floor_min_temperature": TEMP_SCHEMA.extend({
            cv.GenerateID(CONF_PARENT_ID): cv.use_id(WavinAHC9000),
            cv.Required(CONF_CHANNEL): cv.int_range(min=1, max=16),
        }),
        "floor_max_temperature": TEMP_SCHEMA.extend({
            cv.GenerateID(CONF_PARENT_ID): cv.use_id(WavinAHC9000),
            cv.Required(CONF_CHANNEL): cv.int_range(min=1, max=16),
        }),
    },
    lower=True,
)

async def to_code(config):
    hub = await cg.get_variable(config[CONF_PARENT_ID])
    sens = await sensor.new_sensor(config)
    sens_type = config[CONF_TYPE]
    ch = config[CONF_CHANNEL]

    if sens_type == "battery":
        cg.add(hub.add_channel_battery_sensor(ch, sens))
    elif sens_type == "temperature":
        cg.add(hub.add_channel_temperature_sensor(ch, sens))
    elif sens_type == "comfort_setpoint":
        cg.add(hub.add_channel_comfort_setpoint_sensor(ch, sens))
    elif sens_type == "floor_temperature":
        cg.add(hub.add_channel_floor_temperature_sensor(ch, sens))
    elif sens_type == "floor_min_temperature":
        cg.add(hub.add_channel_floor_min_temperature_sensor(ch, sens))
    elif sens_type == "floor_max_temperature":
        cg.add(hub.add_channel_floor_max_temperature_sensor(ch, sens))
        
