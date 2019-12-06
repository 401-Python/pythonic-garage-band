## Lab 04: Classes and Fixtures

### Author: Alvian Joseph

### Links and Resources
* [PR]()
* [![Build Status]()
* [front end]()

### Tasks
Band Tests
A Band instance should have a name attribute which is a string.
A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.
A Band instance should have appropriate __str__ and __repr__ methods.
A Band should have a class method to_list which returns a list of previously created Band instances
A Band should have a static method create_from_data which takes a collection of formatted data and returns a created Band instance. The Band instance should have its members be set to musicians based on info from the input.
Musician Subclass Tests
Each kind of Musician instance should have appropriate __str__ and __repr__ methods.
Each kind of Musician instance should have a get_instrument method that returns string.
Each kind of Musician instance should have a play_solo method that returns string

### Modules
#### garage_band.py
  #### classes

  * ```Band```


  * ```Musician```
    
  
  * ```Guitarist```


  * ```Bassist```
    

  * ```Drummer```
     




### Testing
  pytest
  ptw
  

