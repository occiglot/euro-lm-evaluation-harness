# LeoLM

### Paper

Abstract: https://laion.ai/blog/leo-lm/

We proudly introduce LeoLM (Linguistically Enhanced Open Language Model), the first comprehensive suite of German-language Foundation Language Models trained in collaboration with [HessianAI](https://hessian.ai/) on their new supercomputer 42! Built on Llama-2 and trained on a large-scale, high-quality German text corpus, we present LeoLM-7B and 13B, with LeoLM-70B on the horizon, accompanied by a collection of exceptionally proficient German and bilingual chat models.

Evaluating the capabilities of LLMs, especially chat models, is complex, and the best methods are still up for debate. Benchmarks based on multiple choice that are evaluated via the model's log-probabilities (as in the Open LLM Leaderboard) are one currently popular method. Another method automatically evaluates responses using GPT4, as in AlpacaEval or MT-Bench. This approach is more geared toward chat models, as it considers the quality of model responses in real-life tasks. To be as comparable as possible, we directly translate a set of English benchmarks to German. We release these datasets in our [HF Organization](https://huggingface.co/LeoLM) and with more detailed documentation on GitHub, and you can find the corresponding lm-evaluation-harness fork [here](https://github.com/bjoernpl/lm-evaluation-harness-de/tree/mmlu_de) and the FastEval fork [here](https://github.com/bjoernpl/FastEval).

Homepage: https://laion.ai/


#### Original datasets

* ARC : https://arxiv.org/abs/1803.05457

### Citation


### Groups and Tasks

#### Groups

* 'ai2_arc_m': Evaluates all default multilingual arc_challenge tasks

* 'ai2_arc_de': Evaluates all default german arc_challenge tasks

#### Tasks

* 'arc_challenge_de_leolm'

### Checklist

For adding novel benchmarks/datasets to the library:
* [ ] Is the task an existing benchmark in the literature?
  * [ ] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?


If other tasks on this dataset are already supported:
* [ ] Is the "Main" variant of this task clearly denoted?
* [ ] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [ ] Have you noted which, if any, published evaluation setups are matched by this variant?
