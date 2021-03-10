=============================
The taskplanning Document reference
=============================

.. automodule:: taskplanning
    :members:

plan()
=============================

.. code-block:: python

   def plan():
       """
       This is the main function.
       This function will get the user input for number of parts in bins , kit tray and required parts in kit tray
        It also initializes all the flags and checks all the preconditions
       :return: Generated path or terminates the process if any invalid input given
       """



mov_to_bin(location_n)
=============================


.. code-block:: python

   def mov_to_bin(location_n):
       """
       This function will move the robot to the bins location
       :return: Change the location of the robot
       """



pick(gripper_n, part_bins_n, j_n, single_n)
=============================


.. code-block:: python
    def pick(gripper_n, part_bins_n, j_n, single_n)
    """
    A function to pick parts from the bins
    :param gripper_n: To change the status of gripper arms
    :param part: To decrease the number of parts in the bins
    :param j_n: It denotes which part is this either red, green or blue
    :param single: If True then only right arm will grab the part
    :return: Changes the flags and make necessary changes in parts present in bins
    """



mov_to_tray(location_n)
=============================

.. code-block:: python

   def mov_to_tray(location_n):
       """
       This function will move the robot to tray location
       :return: Change the location of the robot
       """


place(gripper_n, current_tray_n, j_n, single_n)
=============================

.. code-block:: python

   def place(gripper_n, current_tray_n, j_n, single_n):
       """
       This function will place the parts from grippers into the kit tray
       :param gripper_n: After placing parts the gripper flags will turn false
       :param current_tray: After placing parts the number of parts in tray will be increased
       :param j_n: It denotes which colored part is robot holding, either red, green or blue
       :param single: It denotes whether the robot is holding one part or two parts
       :return: Changes the flags and makes changes in the kit tray accordingly
       """



check_max(part_bins_n)
=============================

.. code-block:: python

   def check_max(part_bins_n):
       """
       This function will check if the number of parts in any of the bins is greater than 10 or not.
       :return: Changes the flag


=============================
The taskexecution Document reference
=============================

.. automodule:: taskplanning
    :members:

Execution file
=============================

.. code-block:: python

   # Importing the file with all the functions
   from rwa1 import taskplanning as tp

   # Calling the final function
   tp.plan()
