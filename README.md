# RadGraph

## Table of Contents
- [Requirements](#requirements)
- [RadGraph-XL](#radgraph-xl)
- [F1-RadGraph](#f1-radgraph)
- [Processed Annotations](#processed-annotations)
- [Data](#data)
    - [RadGraph-XL](#radgraph-xl-1)
    - [RadGraph-v1](#radgraph-v1)
- [RadGraph-v1](#radgraph-v1-1)
- [Citations](#citations)
    - [RadGraph-XL](#radgraph-xl-2)
    - [F1-RadGraph](#f1-radgraph-1)
    - [RadGraph-v1](#radgraph-v1-2)
---

## Requirements

```
python_requires=">=3.8",
install_requires=[
    "torch>=2.1.0",
    "transformers>=4.39.0",
    "appdirs",
    "jsonpickle",
    "filelock",
    "h5py",
    "nltk",
    "dotmap",
    "pytest",
],
```
Testing:
```python
pytest
```

## RadGraph-XL

Usage:
```python
from radgraph import RadGraph
radgraph = RadGraph(model_type="modern-radgraph-xl")
annotations = radgraph(["No evidence of pneumothorax following chest tube removal."])
```
Output:
```
{
  "0": {
    "text": "No evidence of pneumothorax following chest tube removal .",
    "entities": {
      "1": {
        "tokens": "pneumothorax",
        "label": "Observation::definitely absent",
        "start_ix": 3,
        "end_ix": 3,
        "relations": []
      },
      "2": {
        "tokens": "chest",
        "label": "Anatomy::definitely present",
        "start_ix": 5,
        "end_ix": 5,
        "relations": []
      },
      "3": {
        "tokens": "tube",
        "label": "Observation::definitely present",
        "start_ix": 6,
        "end_ix": 6,
        "relations": [
          [
            "located_at",
            "2"
          ]
        ]
      }
    },
    "data_source": null,
    "data_split": "inference"
  }
}
```

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


##  F1-RadGraph
Usage:
```python
from radgraph import F1RadGraph
refs = ["no acute cardiopulmonary abnormality",
        "endotracheal tube is present and bibasilar opacities likely represent mild atelectasis",
]

hyps = ["no acute cardiopulmonary abnormality",
        "et tube terminates 2 cm above the carina and bibasilar opacities"
]
f1radgraph = F1RadGraph(reward_level="all", model_type="radgraph-xl")
mean_reward, reward_list, hypothesis_annotation_lists, reference_annotation_lists = f1radgraph(hyps=hyps, refs=refs)

rg_e, rg_er, rg_bar_er = mean_reward

print(mean_reward)
```
Output:
```
(np.float64(0.75), np.float64(0.6666666666666666), np.float64(0.6538461538461539))
```
Over the years, RG_ER has been reported widely in RRG papers.

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
}
```

##  Processed Annotations
```python
import json
from radgraph import get_radgraph_processed_annotations, RadGraph

report = """
Mild pulmonary edema with probable small bilateral pleural effusions.  
More focal opacities at lung bases may reflect atelectasis but infection cannot be completely excluded.
"""
model_type = "modern-radgraph-xl"
radgraph = RadGraph(model_type=model_type)
annotations = radgraph(
    [report]
    )

processed_annotations = get_radgraph_processed_annotations(annotations)
for annotation in processed_annotations["processed_annotations"]:
    located_at = f" [Location: {', '.join(annotation['located_at'])}]" if annotation["located_at"] else ""
    suggestive_of = f" [Suggestive of: {', '.join(annotation['suggestive_of'])}]" if annotation["suggestive_of"] else ""
    tag = f" [Tag: {annotation['tags'][0]}]"
    print(f"Observation: {annotation['observation']}{located_at}{suggestive_of}{tag}")
```
Output:

```
Observation: mild edema [Location: pulmonary] [Tag: definitely present]
Observation: small effusions [Location: bilateral pleural] [Tag: uncertain]
Observation: focal opacities [Location: lung bases] [Suggestive of: opacities suggestive of atelectasis, opacities suggestive of infection] [Tag: definitely present]
Observation: atelectasis [Tag: uncertain]
Observation: infection [Tag: uncertain]
```

## Data
### RadGraph-XL
- Annotated MIMIC reports: https://physionet.org/content/radgraph-xl/1.0.0/ (300 samples) 
- Annotated Stanford reports: https://stanfordaimi.azurewebsites.net/datasets/57816fe0-661c-4a95-8724-3f95b29568d9 (2000 samples)

### RadGraph-v1
- Annotated MIMIC-CXR reports: https://physionet.org/content/radgraph/1.0.0/ (600 samples)

##  RadGraph-v1

```
radgraph = RadGraph(model="radgraph")
```

# Citations
## RadGraph-XL
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

## F1-RadGraph
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
}
```

## RadGraph-v1
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
