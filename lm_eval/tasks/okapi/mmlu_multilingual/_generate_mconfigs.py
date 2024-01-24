"""
generate multilingual yaml files
"""

import os
import yaml
from tqdm import tqdm

from lm_eval.logger import eval_logger

LANGS = "ar,bn,ca,da,de,es,eu,fr,gu,hi,hr,hu,hy,id,it,kn,ml,mr,ne,nl,pt,ro,ru,sk,sr,sv,ta,te,uk,vi,zh".split(
    ","
)


SAFE_PATH = str(os.path.dirname(__file__)) + "/default/"

if __name__ == "__main__":
    for lang in tqdm(LANGS):
        yaml_dict = {
            "dataset_name": f"mmlu_{lang}",
            "task": f"mmlu_m_{lang}",
            "include": "_default_multi_template_yaml",
        }
        file_save_path = SAFE_PATH + f"mmlu_m_{lang}.yaml"
        eval_logger.info(f"Saving yaml for multilanguage ({lang}) to {file_save_path}")

        with open(file_save_path, "w") as yaml_file:
            yaml.dump(
                yaml_dict,
                yaml_file,
                allow_unicode=True,
                default_style='"',
            )
