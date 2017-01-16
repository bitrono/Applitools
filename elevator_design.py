

class Elevator:
    """
    A class of an elevator.
    """
    
    def __init__(self, speed, max_allowed_weight, heighest_floor, lowest_floor, current_floor=0, direction=0):
        """
        Initializes an Elevator.
        """
        self._speed = speed     # Speed of the elevator
        self._max_allowed_weight = max_allowed_weight    # The maximum allowed weight of the elevator in kilograms
        self._heighest_floor = heighest_floor    # The heighest floor the elevator can reach
        self._lowest_floor = lowest_floor   # The lowest floor the elevator can reach
        self._current_floor = current_floor     # The current floor of the elevator
        self._direction = 0     # The current direction of the elevator - up (1), down (-1) or idle (0)
        
    def move_up(self, num_of_floors):
        """
        Moves the elevator up a certain number of floors.
     
        :type num_of_floors: int
        :param num_of_floors: The number of floors to move up
     
        :rtype: bool
        :return: True if successful
        """
    
    def move_down(self, num_of_floors):
        """
        Moves the elevator down a certain number of floors.
     
        :type num_of_floors: int
        :param num_of_floors: The number of floors to move down
     
        :rtype: bool
        :return: True if successful
        """
    
    def emergency_stop(self):
        """
        Stops the elevator in case of emergency.
        
        :rtype: bool
        :return: True if successful
        """
        
    def _turn_on_alarm(self):
        """
        Turns on the alarm of the elevator. 
        
        :rtype: bool
        :return: True if successful
        """
        
    def _turn_off_alarm(self):
        """
        Turns off the alarm of the elevator. 
        
        :rtype: bool
        :return: True if successful
        """
    
    def open_doors(self):
        """
        Opens the elevator doors.
        
        :rtype: bool
        :return: True if successful
        """
    
    def close_doors(self):
        """
        Closes the elevator doors.

        :rtype: bool
        :return: True if successful
        """
        
    def _check_max_weight(self):
        """
        Checks that the max weight hasn't been reached.

        :rtype: bool
        :return: True if max weight hasn't been reached
        """
    
    def idle_mode(self):
        """
        Signals the elevator to stay in idle mode.
        
        :rtype: bool
        :return: True if successful
        """
    
    
    
