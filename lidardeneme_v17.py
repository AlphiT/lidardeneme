from rplidar import RPLidar, RPLidarException
import matplotlib.pyplot as plt
import numpy as np

lidar = RPLidar('com11')

lidar.__init__('com11', 256000, 3, None)

lidar.connect()

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

try:
    for i, scan in enumerate(lidar.iter_scans()):
        scan_data = []
        for d in scan:          
            #d[0] : Quality of the measurement
            if -90 < d[1] < 90:     #d[1] : Angle of the measurement
                print("Açı: ", round(d[1]), "Mesafe: ", d[2] / 10)  #d[2] : Distance of the measurement
                
                # Polar koordinatları güncelle
                polar_angle = np.deg2rad(d[1])  # Açıyı dereceden radyana dönüştür
                polar_distance = d[2] / 10  # Mesafeyi güncelle (mm cinsinden, cm'ye dönüştür)

                # Güncellenmiş polar koordinatları sakla
                scan_data.append((polar_angle, polar_distance))


        if False:
            lidar.stop()
            lidar.stop_motor()
            lidar.disconnect()
            break
except KeyboardInterrupt as err:
    print('key board interupt')
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()

except RPLidarException as err:
    print(err)
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
except AttributeError:
    print('hi attribute error')