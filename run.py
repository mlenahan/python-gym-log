import argparse
from argparse import ArgumentError

parser = argparse.ArgumentParser(
    description='Gym logging app'
)

parser.add_argument(
    'resource',
    type=str,
    help='The resource to interact with.'
)

parser.add_argument(
    'action',
    type=str,
    help='Type of interaction.'
)

parser.add_argument(
    '--name',
    type=str
)

parser.add_argument(
    '--workoutid',
    type=str
)

parser.add_argument(
    '--movementid',
    type=str
)

parser.add_argument(
    '--reps',
    type=int
)

args = parser.parse_args()


def validate_movement_add():
    args = parser.parse_args()
    args_dict = vars(args)
    if args_dict['name'] is None:
        raise ValueError('Must include name when adding a movement.')


def validate_movement_show():
    args = parser.parse_args()
    args_dict = vars(args)
    if args_dict['name'] or args_dict['workoutid'] is None:
        raise ValueError('Must include name or workout id when showing a movement.')


def validate_workout_add():
    args = parser.parse_args()
    args_dict = vars(args)
    if args_dict['name'] is None:
        raise ValueError('Must include name when adding a workout.')


def validate_workout_delete():
    args = parser.parse_args()
    args_dict = vars(args)
    if args_dict['name'] and args_dict['workoutid'] is None:
        raise ValueError('Must include name or workout id when deleting a workout.')


def validate_set_add():
    args = parser.parse_args()
    args_dict = vars(args)
    if args_dict['workoutid'] and args_dict['movementid'] and args_dict['reps'] is None:
        raise ValueError('Must include workout id, movement id and reps when adding a set')


if args.resource == 'movement' and args.action == 'add':
    validate_movement_add()

if args.resource == 'movement' and args.action == 'show':
    validate_movement_show()

if args.resource == 'workout' and args.action == 'add':
    validate_workout_add()

if args.resource == 'set' and args.action == 'add':
    validate_set_add()

if args.resource == 'workout' and args.action == 'delete':
    validate_workout_delete()
# how to use - run.py movement add --name ... 

# resource, action, value
# movement show needs either id or name. write function to handle show

# to add workout - doesnt need name but
# workout - need id or name
# workout delete needs value or name - need a name or id to know what to delete

# cant add set without workout, exercise and number of reps
# 