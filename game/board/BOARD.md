# Package `game.board`

## Table of Contents
1. [Purpose](#purpose)
2. [The `GameBoard` Class](#the-gameboard-class)
   1. [`GameBoard` Immutable Properties](#gameboard-immutable-properties)
   2. [`GameBoard` Mutable Properties](#gameboard-mutable-properties)
   3. [`GameBoard` UML Relationship Diagram`](#gameboard-uml-relationship-diagram)
3. [The `GameBoardSquare` Class](#the-gameboardsquare-class)
   1. [`GameBoardSquare` Immutable Properties](#gameboardsquare-immutable-properties)
   2. [`GameBoardSquare` Mutable Properties](#gameboardsquare-mutable-properties)
   3. [Concrete Subclasses of `GameBoardSquare`](#concrete-subclasses-of-gameboardsquare)
   4. [`GameBoardSquare` UML Relationship Diagram](#gameboardsquare-uml-relationship-diagram)
4. [Package Dependencies](#package-dependencies)


---
## Purpose
Classes and components related to the surface where the player interacts 
with the system and navigates obstacles to win. The package main classes are

- `GameBoard`
- `GameBoardSquare`

---
### The `GameBoard` Class
- A `GameBoard` is a 2-D array of `GameBoardSquare` items. Cells can be referenced by their
`row` and `column.
- A collection of type `GameFigure` is associated with each G`GameBoard`

---
#### `GameBoard` Immutable Properties
These are permanently on the board during its lifecycle.
- ***`num_rows`:*** Size of `List<GameBoardSquare>` representing y-coordinate. 
- ***`num_columns`:*** Size of `List<GameBoardSquare>` representing x-coordinate. 
- ***`List<Obstacle>`:***
- ***`EscapeSquare`:*** The player wins the level by landing on the `EsapeSquare`.
- ***`List<Vehicle>`:***

--- 
#### `GameBoard` Mutable Properties
These can be added to or removed from the board making them mutable.

- ***`PlayerFigure`***:

---
#### GameBoard UML Relationship Diagram
```plantuml
@startuml
' Abstract sealed class
abstract class GeoCodeState

' Subclasses of GeoCodeState
class Loading  <<immutable>> {
<<singleton>> ' Creates GeoCode object
}

class Success  <<immutable>> {
+ <i>geoCode</i>: GeoCode
}

class Error  <<immutable>> {
+ <i>message</i>: String
}

' Representing inheritance relationships
GeoCodeState <|--- Loading
GeoCodeState <|--up- Success
GeoCodeState <|--- Error

' Aggregation or Instantiation Relationship
GeoCodeState ..> Loading : creates
GeoCodeState ..> Success : creates
GeoCodeState ..> Error : creates

' Abstract class representing the sealed class
abstract class CurrentWeatherState  <<immutable>> {
 + loading(): Loading
  + createError(message: String): Error
 + createSuccess(currentWeather: CurrentWeather): Success
}

' Subclasses

class Loading  <<immutable>> {
 + Loading: <<singleton>> 
}

class Success  <<immutable>> {
 + <i>currentWeather</i>: CurrentWeather
}

class Error  <<immutable>> {
 + <i>message</i>: String
}

' Inheritance Relationships
CurrentWeatherState <|--- Loading
CurrentWeatherState <|--up- Success
CurrentWeatherState <|--- Error

' Aggregation or Instantiation Relationship
CurrentWeatherState ..> Loading : creates
CurrentWeatherState ..> Success : creates
CurrentWeatherState ..> Error : creates

@enduml
```

----
### The `GameboardSquare` Class
- A `GameBoardSquare` is an abstract class associated with a `GameBoard`.
- Can be occupied by a `GameFigure`

----
#### `GameBoardSquare` Immutable Properties

 - ***`id`:*** unique identifier
 - ***`dimensionInPixels:`*** Side length on the screen.
 - ***`row`:*** Row of `GameBoard` the square lives on.
 - ***`column`:*** Column of `GameBoard` the square lives on.
 - ***`color`:***

---
#### `GameBoardSquare` Mutable Properties
- ***Occupant:*** 

#### Concrete Subclasses of `GameBoardSquare`
- ***`Cell`:*** No different properties or behavior than superclass.
- ***`EscapeCell`:*** Implements `escape(Player player)`

#### `GameBoardSquare` Relationship Diagram

## Package Dependencies

### Python libraries and external packages
These need to be imported
1. pygame==2.6.1 
2. Pygments==2.19.1 
3. pytest==8.4.0
4. `dataclasses.dataclass`
5. `typing.Optional`

### Internal Dependencies
1. `game.common.game_constant`: `GameConstant`
2. `game.exception.exception`: `InvalidIdError`, `NegativeRowError`, `NegativeColumnError`
