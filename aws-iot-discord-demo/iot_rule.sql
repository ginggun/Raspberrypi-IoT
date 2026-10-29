
-- AWS IoT Core SQL Rule
-- Rule name: TemperatureAlertRule
-- SQL version: 2016-03-23
-- Input topic: raspi/temperature
-- Alert topic: raspi/alerts/temperature

SELECT device, sensor, value, 'WARNING' AS status
FROM 'raspi/temperature'
WHERE value > 30
