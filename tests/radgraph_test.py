from radgraph import RadGraph, F1RadGraph


def test_radgraph():
    radgraph = RadGraph(model_type="radgraph")
    annotations = radgraph(["no evidence of acute cardiopulmonary process moderate hiatal hernia"])
    assert annotations == {'0': {'text': 'no evidence of acute cardiopulmonary process moderate hiatal hernia',
                                 'entities': {'1': {'tokens': 'acute', 'label': 'OBS-DA', 'start_ix': 3, 'end_ix': 3,
                                                    'relations': []},
                                              '2': {'tokens': 'cardiopulmonary', 'label': 'ANAT-DP', 'start_ix': 4,
                                                    'end_ix': 4,
                                                    'relations': []},
                                              '3': {'tokens': 'process', 'label': 'OBS-DA', 'start_ix': 5, 'end_ix': 5,
                                                    'relations': [['located_at', '2']]},
                                              '4': {'tokens': 'moderate', 'label': 'OBS-DP', 'start_ix': 6, 'end_ix': 6,
                                                    'relations': []},
                                              '5': {'tokens': 'hiatal', 'label': 'ANAT-DP', 'start_ix': 7, 'end_ix': 7,
                                                    'relations': []},
                                              '6': {'tokens': 'hernia', 'label': 'OBS-DP', 'start_ix': 8, 'end_ix': 8,
                                                    'relations': []}},
                                 'data_source': None, 'data_split': 'inference'}}


def test_f1radgraph():
    refs = ["no acute cardiopulmonary abnormality",
            "et tube terminates 2 cm above the carina retraction by several centimeters is recommended for more optimal placement bibasilar consolidations better assessed on concurrent chest ct",
            "there is no significant change since the previous exam the feeding tube and nasogastric tube have been removed",
            "unchanged mild pulmonary edema no radiographic evidence pneumonia",
            "no evidence of acute pulmonary process moderately large size hiatal hernia",
            "no acute intrathoracic process"]

    hyps = ["no acute cardiopulmonary abnormality",
            "endotracheal tube terminates 2 5 cm above the carina bibasilar opacities likely represent atelectasis or aspiration",
            "there is no significant change since the previous exam",
            "unchanged mild pulmonary edema and moderate cardiomegaly",
            "no evidence of acute cardiopulmonary process moderate hiatal hernia",
            "no acute cardiopulmonary process"]

    f1radgraph = F1RadGraph(reward_level="all", model_type="radgraph")
    mean_reward, reward_list, hypothesis_annotation_lists, reference_annotation_lists = f1radgraph(hyps=hyps, refs=refs)
    assert mean_reward == (0.6238095238095238, 0.5111111111111111, 0.5011204481792717)
    assert reward_list == ([1.0, 0.4, 0.5714285714285715, 0.8, 0.5714285714285715, 0.4],
                           [1.0, 0.26666666666666666, 0.5714285714285715, 0.4, 0.42857142857142855, 0.4],
                           [1.0, 0.23529411764705885, 0.5714285714285715, 0.4, 0.4, 0.4])


test_radgraph()
