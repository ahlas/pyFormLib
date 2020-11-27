from VehicleStructs import Coordinates,MovementValues,AvoidAlarmSide,AvoidLengthVehicles,AvoidAlarmDistance

#------------------------Variables For MultiThread
frontCoor = Coordinates()
backCoor = Coordinates()
rightCoor = Coordinates()
leftCoor = Coordinates()

#------------------------Camera Coordinates

frontCAMCoordinate = Coordinates()
backCAMCoordinate = Coordinates()
rightCAMCoordinate = Coordinates()
leftCAMCoordinate = Coordinates()


#----------------------- Distance Values
avoidDistance = AvoidLengthVehicles()
alarmDistance = AvoidAlarmDistance()
alarmSide   = AvoidAlarmSide()

avoidDistanceDeviance = 0.0
avoidDistanceFrontMax = 0.0
avoidDistanceFrontMin = 0.0
avoidDistanceBackMax  = 0.0
avoidDistanceBackMin  = 0.0
avoidDistanceRightMax = 0.0
avoidDistanceRightMin = 0.0
avoidDistanceLeftMax  = 0.0
avoidDistanceLeftMin  = 0.0