from enum import Enum

class MovementTYPE(Enum):
	HOLD = 0
	FORWARD = 1
	LEFT = 2
	RIGHT = 3
	BACK = 4
	#Forward Behaviours
	FR_Strong_45 = 5
	FR_Weak_45 = 6
	FL_Strong_45 = 7
	FL_Weak_135 = 8
	#Back Behaviours
	BR_Strong_45 = 9
	BR_Weak_45 = 10
	BL_Strong_45 = 11
	BL_Weak_135 = 12


class VehicleStatus(Enum):
	LEADER			= 99
	BORDERLEFT		= 100
	BORDERRIGHT		= 101
	SLAVE			= 102

#-------Takip edeceği öncellik sıralaması
class PriorityToFollow(Enum):
	Alone = 1
	Forward = 2
	Back = 3
	Right = 4
	Left = 5

class AlarmStatus(Enum):
	NoPanic = 1
	Careful = 2
	Emergency = 3

#----------- Alarm durumlarına göre takınacağı tavır -----------
class avoidAlarmFormation(Enum):
	Nothing = 0
	A = 1
	B = 2
	C = 3
	D = 4
	E = 5
	F = 6
	G = 7
	H = 8
	K = 9
	L = 10
	M = 11
	N = 12
	P = 13
	R = 14
	S = 15
	T = 16