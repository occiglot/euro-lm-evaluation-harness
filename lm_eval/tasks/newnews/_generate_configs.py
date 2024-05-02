"""
A simple script for generating the task configs. Run via:

python _generate_configs.py
"""

import os
from pathlib import Path


LANGUAGES = ["en", "fr", "it", "es", "de"]
DATES = [
    # 2021
    "2021_q1",
    "2021_q2",
    "2021_q3",
    "2021_q4",
    # 2022
    "2022_q1",
    "2022_q2",
    "2022_q3",
    "2022_q4",
    # 2023
    "2023_q1",
    "2023_q2",
    "2023_q3",
    "2023_q4",
    # 2024
    "2024_q1",
]
config_dir = Path(__file__).parent

print("Remove old config files")

for fp in config_dir.glob("newnews_*.yaml"):
    os.remove(fp)

print("Generating config files ...")


for language in LANGUAGES:
    for date in DATES:
        print(f"> {language=}, {date=}")

        config_yaml = f"""
task: newnews_{language}_{date}
dataset_name: {language}
test_split: "{date}"

include: _default_newnews_template_yaml
"""
        config_file_name = f"newnews_{language}_{date}.yaml"
        with open(config_dir / config_file_name, "w") as f:
            f.write(config_yaml)

print("done")
