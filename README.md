# Applitools

README

    The Elevator class allows to control and operate an elevator in any building. 
    It lets the programmer set a speed limit, weight limit, heighest floor limit and lowest floor limit in order to suit every need.
    
CONTACT

    If there are any problems, ideas or suggestions please contact us via e-mail: ElevatorSupport@gmail.com
    
USAGE

    In order to initialize an instance of the elevator, execute the following line from your program:
    
    Elevator newElevator(DEFAULT_ELEVATOR_SPEED, DEFAULT_ELEVATOR_WEIGHT, HEIGHEST_FLOOR_IN_THE_BUILDING, LOWEST_FLOOR_IN_THE_BUILDING)
    
DEPENDENCIES

    The elevator class doesn't require any external libraries/packages.
    
FUNCTIONS
    
    init() - The initialization of the elevator sets the elevator speed, maximum weight allowed on the elevator, the heighest floor the elevator can reach, the lowest floor the elevator can reach, the current floor that the elevator is located - by default is located at the lobby floor, the direction that the elevator is going at - by default is in idle mode.
    
    move_up(num_of_floors) - Signals the elevator to move up a certain amount of floors. NOTE: Elevator wont go heigher than self._heighest_floor!

    move_down(num_of_floors) - Signals the elevator to move down a certain amount of floors. NOTE: Elevator wont go lower than self._lowest_floor!
    
    idle_mode() - Signals the elevator to stay put and wait for move_up or move_down calls.
    
    open_doors() - Signals the elevator to open the doors so that clients can enter/exit.
    
    close_doors() - Signals the elevator to close the doors and either enters idle mode, moves up or moves down.
    
    _check_max_weight() - Only used by close_doors function to check whether the current weight of the elevator exceeds the maximum allowed weight.
    
    emergency_stop() - Stops the elevator in case of an emergency. In case of emergency stop, will call the turn_on_alarm function until signaled to turn of alarm and then calls the turn_off_alarm.
    
    _turn_on_alarm() - Only used by emergency_stop and _check_max_weight functions to turn of the alarm in case of problem.
    
    _turn_off_alarm() - Only used by emergency_stop and _check_max_weight functions to turn off the alarm in case of problem.
    
COPYRIGHT

    Copyrights (c) 2017 "WHOMEVER". All rights reserved.
    
