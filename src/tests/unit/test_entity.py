from entities.todos import TodoSchema
from fixtures import JSON_RAW_DATA


def test_entity_serialization(mocker):
    """Test check if Marshmallow removed unknown fields."""
    data = TodoSchema(many=True).load(JSON_RAW_DATA)

    for d in data:
        assert len(set(d.keys()) - {'id', 'title'}) == 0, "Got unknown field into entity"

