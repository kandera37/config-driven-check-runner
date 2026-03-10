import yaml

def load_config(config_path: str) -> dict:
    """Load YAML config file abd return it as a dictionary."""
    with open(config_path, "r", encoding="utf-8") as config_file:
        data = yaml.safe_load(config_file)

    if data is None:
        return {}
    return data
