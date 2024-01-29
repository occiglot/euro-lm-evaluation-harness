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
VARIATIONS = ['mc1', 'mc2']

SAFE_PATH = str(os.path.dirname(__file__)) + "/default/"

if __name__ == "__main__":
    for variation in VARIATIONS:
        for lang in tqdm(LANGS, desc=f"Generate truthfulqa_{variation}"):
            # generate truthfulqa_gen 
            yaml_dict = {
                "dataset_name": f"truthfulqa_{lang}",
                "task": f"truthfulqa_{variation}_m_{lang}",
                "group": [f"truthfulqa_multilingual",
                          f"truthfulqa_m_{lang}",
                          f"truthfulqa_m_{variation}"],
                "include": f"_default_multi_template_{variation}_yaml",
            }
            file_save_path = SAFE_PATH + f"truthfulqa_{variation}_m_{lang}.yaml"
            eval_logger.info(f"Saving yaml for multilanguage ({lang}) and {variation}-Task to {file_save_path}")
            with open(file_save_path, "w") as yaml_file:
                yaml.dump(
                    yaml_dict,
                    yaml_file,
                    allow_unicode=True,
                    default_style='"',
                )
