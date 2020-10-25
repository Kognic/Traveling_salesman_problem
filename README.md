* NAME: burma14
* TYPE: TSP
* COMMENT: 14-Staedte in Burma (Zaw Win)
* DIMENSION: 14
* EDGE_WEIGHT_TYPE: GEO
* EDGE_WEIGHT_FORMAT: FUNCTION 
* DISPLAY_DATA_TYPE: COORD_DISPLAY
* NODE_COORD_SECTION
  * 1  16.47       96.10
  * 2  16.47       94.44
  * 3  20.09       92.54
  * 4  22.39       93.37
  * 5  25.23       97.24
  * 6  22.00       96.05
  * 7  20.47       97.02
  * 8  17.20       96.29
  * 9  16.30       97.38
  * 10  14.05       98.12
  * 11  16.53       97.38
  * 12  21.52       95.59
  * 13  19.41       97.13
  * 14  20.09       94.55
* EOF.

# Results comparison
* brute force:
	* for 11 in km - ('1', '2', '3', '4', '5', '6', '7', '8', '11', '9', '10', '1') -> 3136 - 0:00:12.105144
	* for 12 in km - MemoryError
	* for 13 in km - MemoryError
	* for 14 in km - MemoryError

* branch and bound:
	* for 11 in km - 1:2:3:4:5:6:7:8:11:9:10:1, 3136 - 0:00:00.186148
	* for 12 in km - 1:2:3:4:5:6:12:7:8:11:9:10:1, 3150 - 0:00:00.416693
	* for 13 in km - 1:2:3:4:5:6:12:7:13:8:11:9:10:1, 3158 - 0:00:00.836091
	* for 14 in km - 1:2:14:3:4:5:6:12:7:13:8:11:9:10:1, 3323 - 0:00:01.770450

