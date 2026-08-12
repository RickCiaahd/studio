from unittest.mock import patch

from src.etl.main import run_pipeline


@patch("src.etl.main.save_to_db", return_value=1)
@patch("src.etl.main.create_table")
@patch("src.etl.main.transform_products", return_value=[{"title": "A"}])
@patch("src.etl.main.extract_products", return_value=[{"raw": "record"}])
def test_run_pipeline_coordinates_steps(mock_extract, mock_transform, mock_create, mock_save):
    assert run_pipeline() == 1
    mock_extract.assert_called_once_with()
    mock_transform.assert_called_once_with([{"raw": "record"}])
    mock_create.assert_called_once_with()
    mock_save.assert_called_once_with([{"title": "A"}])
