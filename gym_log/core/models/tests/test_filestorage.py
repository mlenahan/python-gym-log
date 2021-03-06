import unittest
import uuid
from mock import patch

from gym_log.storage.file_storage import FileStorage
from gym_log.core.models.movement import Movement
from gym_log.core.models.workout import Workout
from gym_log.core.models.set import Set


def mock_uuid4():
    mock_uuid = uuid.UUID('{12345678-1234-5678-1234-567812345678}')
    return mock_uuid


@patch('uuid.uuid4', mock_uuid4)
class TestFileStorage(unittest.TestCase):

    def test_initialization_file_storage(self):
        file_storage = FileStorage()
        self.assertTrue(isinstance(file_storage, FileStorage))

    def test_get_entity_path_for_movement(self):
        movement = Movement('Deadlift')
        file_storage = FileStorage()
        path = file_storage.get_entity_path(movement)
        self.assertTrue(path.endswith('gym_log/storage/data/movement.json'))

    def test_get_entity_path_for_workout(self):
        workout = Workout('Leg Day 1')
        file_storage = FileStorage()
        path = file_storage.get_entity_path(workout)
        self.assertTrue(path.endswith('gym_log/storage/data/workout.json'))

    def test_get_entity_path_for_set(self):
        set = Set('12345678', '12345678', 12)
        file_storage = FileStorage()
        path = file_storage.get_entity_path(set)
        self.assertTrue(path.endswith('gym_log/storage/data/set.json'))

    def test_save_movement(self):
        movement = Movement('Deadlift')
        file_storage = FileStorage()
        file_storage.save(movement)

    def test_save_multiple_classes(self):
        movement = Movement('Deadlift')
        workout = Workout('Push Day 2')
        file_storage = FileStorage()
        file_storage.save(movement)
        file_storage.save(workout)

    def test_save_multiple_movements(self):
        movement_1 = Movement('Deadlift', id='d123')
        movement_2 = Movement('Squat', id='s123')
        file_storage = FileStorage()
        file_storage.save(movement_1)
        file_storage.save(movement_2)
