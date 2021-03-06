import os
import FormLibVariable as fmLib
import enumList as enumLib
import threading


# ------------------------- Vehiclerlar arası mesafelerin ne kadar olması gerektiği ayarlanıyor
def initAvoidLengthVehicles(avoidDistanceDeviance, forward, back, right, left):
    fmLib.avoidDistanceDeviance = avoidDistanceDeviance  # belirlenen mesafeler arasındaki standart sapma yüzdesi
    fmLib.avoidDistance.forwardDistanceAvoid = forward
    fmLib.avoidDistance.backDistanceAvoid = back
    fmLib.avoidDistance.rightDistanceAvoid = right
    fmLib.avoidDistance.leftDistanceAvoid = left

    fmLib.avoidDistanceFrontMin = forward - (forward * (avoidDistanceDeviance / 100));
    fmLib.avoidDistanceFrontMax = forward + (forward * (avoidDistanceDeviance / 100));

    fmLib.avoidDistanceBackMin = back - (back * (avoidDistanceDeviance / 100));
    fmLib.avoidDistanceBackMax = back + (back * (avoidDistanceDeviance / 100));

    fmLib.avoidDistanceRightMin = right - (right * (avoidDistanceDeviance / 100));
    fmLib.avoidDistanceRightMax = right + (right * (avoidDistanceDeviance / 100));

    fmLib.avoidDistanceLeftMin = left - (left * (avoidDistanceDeviance / 100));
    fmLib.avoidDistanceLeftMax = left + (left * (avoidDistanceDeviance / 100));


# ------------------------- Vehiclerlar arası mesafelerin ACIL durum ayarı
def initAvoidLengthAlarmVehicles(forward, back, right, left):
    fmLib.alarmDistance.alarmDistanceForward = forward
    fmLib.alarmDistance.alarmDistanceBack = back
    fmLib.alarmDistance.alarmDistanceRight = right
    fmLib.alarmDistance.alarmDistanceLeft = left


def frontVehicleCamAlarmProcess():
    # İlgili alanda olmamız durumu
    if fmLib.frontCAMCoordinate.coordinateX > fmLib.avoidDistanceFrontMin or fmLib.frontCAMCoordinate.coordinateX < fmLib.avoidDistanceFrontMax:
        fmLib.alarmSide.front = enumLib.AlarmStatus.NoPanic

    elif fmLib.frontCAMCoordinate.coordinateX > fmLib.avoidDistanceFrontMax:
        fmLib.alarmSide.front = enumLib.AlarmStatus.Careful

    elif fmLib.frontCAMCoordinate.coordinateX < fmLib.avoidDistanceFrontMin:
        fmLib.alarmSide.front = enumLib.AlarmStatus.Careful

def backVehicleCamAlarmProcess():
    # İlgili alanda olmamız durumu
    if fmLib.backCAMCoordinate.coordinateX > fmLib.avoidDistanceBackMin or fmLib.backCAMCoordinate.coordinateX < fmLib.avoidDistanceBackMax:
        fmLib.alarmSide.back = enumLib.AlarmStatus.NoPanic

    elif fmLib.backCAMCoordinate.coordinateX > fmLib.avoidDistanceBackMax:
        fmLib.alarmSide.back = enumLib.AlarmStatus.Careful

    elif fmLib.backCAMCoordinate.coordinateX < fmLib.avoidDistanceBackMin:
        fmLib.alarmSide.back = enumLib.AlarmStatus.Careful

def rightVehicleCamAlarmProcess():
    # İlgili alanda olmamız durumu
    if fmLib.rightCAMCoordinate.coordinateZ > fmLib.avoidDistanceRightMin or fmLib.rightCAMCoordinate.coordinateZ < fmLib.avoidDistanceRightMax:
        fmLib.alarmSide.right = enumLib.AlarmStatus.NoPanic

    elif fmLib.rightCAMCoordinate.coordinateZ > fmLib.avoidDistanceRightMax:
        fmLib.alarmSide.right = enumLib.AlarmStatus.Careful

    elif fmLib.rightCAMCoordinate.coordinateZ < fmLib.avoidDistanceRightMin:
        fmLib.alarmSide.right = enumLib.AlarmStatus.Careful

def leftVehicleCamAlarmProcess():
    # İlgili alanda olmamız durumu
    if fmLib.leftCAMCoordinate.coordinateZ > fmLib.avoidDistanceLeftMin or fmLib.leftCAMCoordinate.coordinateZ < fmLib.avoidDistanceLeftMax:
        fmLib.alarmSide.left = enumLib.AlarmStatus.NoPanic

    elif fmLib.leftCAMCoordinate.coordinateZ > fmLib.avoidDistanceLeftMax:
        fmLib.alarmSide.left = enumLib.AlarmStatus.Careful

    elif fmLib.leftCAMCoordinate.coordinateZ < fmLib.avoidDistanceLeftMin:
        fmLib.alarmSide.left = enumLib.AlarmStatus.Careful


def subAllProcessFunctionNothing():

    if fmLib.avoidDistance.forwardDistanceAvoid - fmLib.frontCoor.coordinateX > 0:
        #TODO: Vehicle hızlanma yapacak
        return 0
    elif fmLib.avoidDistance.forwardDistanceAvoid - fmLib.frontCoor.coordinateX < 0:
        #TODO: Vehicle yavaşlama yapacak
        return 0

    if fmLib.avoidDistance.rightDistanceAvoid - fmLib.rightCoor.coordinateZ > 0:
        #Todo: Vehicle sağa doğru yanaşma sergileyecek
        return 0
    elif fmLib.avoidDistance.rightDistanceAvoid - fmLib.rightCoor.coordinateZ < 0:
        #Todo: Vehicle sola doğru yanaşma sergileyecek
        return 0

    if fmLib.avoidDistance.leftDistanceAvoid - fmLib.leftCoor.coordinateZ > 0:
        #Todo: Vehicle sola doğru yanaşma sergileyecek
        return 0
    elif fmLib.avoidDistance.leftDistanceAvoid - fmLib.leftCoor.coordinateZ < 0:
        #Todo: Vehicle sağa doğru yanaşma sergileyecek
        return 0

def subAllProcessFunctionAlarm(alarm):
    if alarm == enumLib.avoidAlarmFormation.A:
        return 0
    else:
        return 0

def allProcessFunction(lock):
    alarm = enumLib.avoidAlarmFormation.Nothing

    lock.acquire()
    #TODO:: Burada verileri çekme işlemi yaptırcaz
    lock.release()
    if alarm == enumLib.avoidAlarmFormation.Nothing:
        # TODO::Acildurummevcutdeğilikenyapılacakdavranışlar
        subAllProcessFunctionNothing()

    else:
        # TODO::Alarm durumlarında ortaya çıkan yapılacaklar fonksiyonu
        subAllProcessFunctionAlarm(alarm)
    for i in range(0,500):
        print("AAA")

def tempFunction(lock):
    lock.acquire()
    #TODO: coordinatları burada alıp guncellemeyi göndericez sürekli
    for i in range(0, 500):
        print("BBBB")
    lock.release()
    return 0

def analysis(lock):
    #TODO : alınan verinin analizi burada yapılacak ona bağlı olarak acil işlem de allProcessFunction threadi durdurulup yeniden başlatılarak acil önlem işlemi yaptırılacak
    return 0

if __name__ == "__main__":
    lock = threading.Lock()
    t1 = threading.Thread(target=allProcessFunction,args=(lock,))
    t2 = threading.Thread(target=tempFunction,args=(lock,))
    t3 = threading.Thread(target=analysis,args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("\n\nProje completed....")