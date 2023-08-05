import configparser

filename = "file.ini"

# Writing Data
config = configparser.ConfigParser()
config.read(filename)

try:
    config.add_section("SETTINGS")
except configparser.DuplicateSectionError:
    pass

config.set("SETTINGS", "time", "utc")
config.set("SETTINGS", "time_format", "24h")
config.set("SETTINGS", "language", "english")
config.set("SETTINGS", "testing", "false")
config.set("SETTINGS", "production", "true")

with open(filename, "w") as config_file:
    config.write(config_file)

# Reading Data
config.read(filename)
keys = [
    "time",
    "time_format",
    "language",
    "testing",
    "production"
]
for key in keys:
    try:
        value = config.get("SETTINGS", key)
        print(f"{key}:", value)
    except configparser.NoOptionError:
        print(f"No option '{key}' in section 'SETTINGS'")