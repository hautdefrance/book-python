{}  # dict
{1}  # set
{1, 2}  # set
{1: 2}  # dict
{1: 1, 2: 2}  # dict

my_data = {}
isinstance(my_data, (set, dict))  # True

isinstance(my_data, dict)  # True
isinstance(my_data, set)  # False

my_data = {1}
isinstance(my_data, set)  # True
isinstance(my_data, dict)  # False

my_data = {1: 1}
isinstance(my_data, set)  # False
isinstance(my_data, dict)  # True
