import enumList


class Coordinates:
    coordinateX = 0.0
    coordinateY = 0.0
    coordinateZ = 0.0


class MovementValues:
    MovementType = enumList.MovementTYPE.HOLD
    speedYaw = 0.0
    speedPitch = 0.0
    speedRoll = 0.0


class AvoidLengthVehicles:
    forwardDistanceAvoid = 0.0
    backDistanceAvoid = 0.0
    rightDistanceAvoid = 0.0
    leftDistanceAvoid = 0.0


class AvoidAlarmDistance:
    alarmDistanceForward = 0.0
    alarmDistanceBack = 0.0
    alarmDistanceRight = 0.0
    alarmDistanceLeft = 0.0


class AvoidAlarmSide:
    front = enumList.AlarmStatus.NoPanic
    back = enumList.AlarmStatus.NoPanic
    right = enumList.AlarmStatus.NoPanic
    left = enumList.AlarmStatus.NoPanic
