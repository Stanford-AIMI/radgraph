import json
import os
import pytest

from radgraph import RadGraph

# NOTE removed test for modern-radgraph-xl because modern-radgraph-xl does not work right with transformers v5, and we do not use it in ARIES

# @pytest.mark.parametrize("model_type", ["modern-radgraph-xl"])
# def test_modern_radgraph_xl_outputs_match_expected(model_type):
#     """Verify current model output matches the stored golden file."""
#     base_dir = os.path.dirname(__file__)
#     expected_path = os.path.join(base_dir, "chexbert_test_set_modern_radgraph_xl.json")
#     input_path = os.path.join(base_dir, "chexbert_test_set.json")

#     # Load expected predictions and input reports
#     with open(expected_path, "r", encoding="utf-8") as f:
#         expected_predictions = json.load(f)

#     with open(input_path, "r", encoding="utf-8") as f:
#         reports_dict = json.load(f)

#     # Basic sanity check: lengths must match
#     assert len(expected_predictions) == len(reports_dict), (
#         "Mismatch between number of expected predictions and number of "
#         "reports in the test set"
#     )

#     radgraph = RadGraph(model_type=model_type)

#     # Iterate deterministically over the dataset to make debugging easier
#     for (report_id, report_text), expected_prediction in zip(
#         sorted(reports_dict.items(), key=lambda kv: int(kv[0])), expected_predictions
#     ):
#         current_prediction = radgraph([report_text])
#         assert current_prediction == expected_prediction, (
#             f"RadGraph output mismatch for report ID {report_id}"
#         )


if __name__ == "__main__":
    print("This module is meant to be executed with pytest, e.g.\n    pytest -xvs tests/test_radgraph_xl.py")
