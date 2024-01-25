"""
generate multilingual yaml files
"""

import os
import yaml
from tqdm import tqdm

LANGS = "ar,bn,ca,da,de,es,eu,fr,gu,hi,hr,hu,hy,id,it,kn,ml,mr,ne,nl,pt,ro,ru,sk,sr,sv,ta,te,uk,vi,zh".split(
    ","
)


BASE_PATH = os.path.dirname(__file__)

if __name__ == "__main__":
    for lang in tqdm(LANGS):
        yaml_dict = {
            "dataset_name": f"arc_{lang}",
            "task": f"arc_challenge_m_{lang}",
            "include": "_arc_challenge_m_yaml",
        }
        file_save_path = os.path.join(BASE_PATH, f"arc_challenge_m_{lang}.yaml")
        print(f"Saving yaml for multilanguage ({lang}) to {file_save_path}")

        with open(file_save_path, "w") as yaml_file:
            yaml.dump(
                yaml_dict,
                yaml_file,
                allow_unicode=True,
                default_style='"',
            )
