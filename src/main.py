import argparse

from config_loader import load_config
from runner import run_instance

def main() -> None:
    parser = argparse.ArgumentParser(description='Load YAML config and prepare scan run')
    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Path to YAML configuration file",
    )

    args = parser.parse_args()

    config = load_config(args.config)
    instances = config["instances"]
    for instance in instances:
        run_instance(instance)

if __name__ == "__main__":
    main()