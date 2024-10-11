# RadGraph

RadGraph is built for Python 3.8.

You can install it in a virtual environment using
```sh
brew install python@3.8
/opt/homebrew/opt/python@3.8/libexec/bin/python3 -m venv radgraph
source radgraph/bin/activate
```

## Build & Install Package Locally

```sh
$ pip install .
```

## Run Tests

First build & install the package locally; then run `pytest` to execute the tests.
```sh
$ pip install .
$ pytest
```

## Examples

Official package as per:

```bibtex
@inproceedings{delbrouck-etal-2024-radgraph,
    title = "{R}ad{G}raph-{XL}: A Large-Scale Expert-Annotated Dataset for Entity and Relation Extraction from Radiology Reports",
    author = "Delbrouck, Jean-Benoit  and
      Chambon, Pierre  and
      Chen, Zhihong  and
      Varma, Maya  and
      Johnston, Andrew  and
      Blankemeier, Louis  and
      Van Veen, Dave  and
      Bui, Tan  and
      Truong, Steven  and
      Langlotz, Curtis",
    editor = "Ku, Lun-Wei  and
      Martins, Andre  and
      Srikumar, Vivek",
    booktitle = "Findings of the Association for Computational Linguistics ACL 2024",
    month = aug,
    year = "2024",
    address = "Bangkok, Thailand and virtual meeting",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.findings-acl.765",
    pages = "12902--12915",
    }
```

Usage:
```python
from radgraph import RadGraph, F1RadGraph
radgraph = RadGraph()
annotations = radgraph(["no evidence of acute cardiopulmonary process moderate hiatal hernia"])
```

F1RadGraph as per:

```bibtex
@inproceedings{delbrouck-etal-2022-improving,
    title = "Improving the Factual Correctness of Radiology Report Generation with Semantic Rewards",
    author = "Delbrouck, Jean-Benoit  and
      Chambon, Pierre  and
      Bluethgen, Christian  and
      Tsai, Emily  and
      Almusa, Omar  and
      Langlotz, Curtis",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2022",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.findings-emnlp.319",
    pages = "4348--4360",
    abstract = "Neural image-to-text radiology report generation systems offer the potential to improve radiology reporting by reducing the repetitive process of report drafting and identifying possible medical errors. These systems have achieved promising performance as measured by widely used NLG metrics such as BLEU and CIDEr. However, the current systems face important limitations. First, they present an increased complexity in architecture that offers only marginal improvements on NLG metrics. Secondly, these systems that achieve high performance on these metrics are not always factually complete or consistent due to both inadequate training and evaluation. Recent studies have shown the systems can be substantially improved by using new methods encouraging 1) the generation of domain entities consistent with the reference and 2) describing these entities in inferentially consistent ways. So far, these methods rely on weakly-supervised approaches (rule-based) and named entity recognition systems that are not specific to the chest X-ray domain. To overcome this limitation, we propose a new method, the RadGraph reward, to further improve the factual completeness and correctness of generated radiology reports. More precisely, we leverage the RadGraph dataset containing annotated chest X-ray reports with entities and relations between entities. On two open radiology report datasets, our system substantially improves the scores up to 14.2{\%} and 25.3{\%} on metrics evaluating the factual correctness and completeness of reports.",
}
```
Usage:
```python
from radgraph import F1RadGraph
refs = ["no acute cardiopulmonary abnormality",
        "et tube terminates 2 cm above the carina retraction by several centimeters is recommended for more optimal placement bibasilar consolidations better assessed on concurrent chest ct"
]

hyps = ["no acute cardiopulmonary abnormality",
        "endotracheal tube terminates 2 5 cm above the carina bibasilar opacities likely represent atelectasis or aspiration",
]
f1radgraph = F1RadGraph(reward_level="all")
mean_reward, reward_list, hypothesis_annotation_lists, reference_annotation_lists = f1radgraph(hyps=hyps, refs=refs)

```


For info, radgraph v1 is:

```bibtex
@inproceedings{NEURIPS DATASETS AND BENCHMARKS2021_c8ffe9a5,
 author = {Jain, Saahil and Agrawal, Ashwin and Saporta, Adriel and Truong, Steven and Duong, Du Nguyen Duong Nguyen and Bui, Tan and Chambon, Pierre and Zhang, Yuhao and Lungren, Matthew and Ng, Andrew and Langlotz, Curtis and Rajpurkar, Pranav and Rajpurkar, Pranav},
 booktitle = {Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks},
 editor = {J. Vanschoren and S. Yeung},
 pages = {},
 publisher = {Curran},
 title = {RadGraph: Extracting Clinical Entities and Relations from Radiology Reports},
 url = {https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/file/c8ffe9a587b126f152ed3d89a146b445-Paper-round1.pdf},
 volume = {1},
 year = {2021}
}
```
