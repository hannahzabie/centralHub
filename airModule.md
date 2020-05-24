# Matter Sensors:

## CO2, Temperature, & Humidity Sensor (SCD30:)

#### The SCD30 Sensor is a versatile sensor that can measure C02, termperature, and humidity...Embedded with Sensirion SCD30 for C02 observation with Sensirion humidity and temperature sensors, which are on the same sensor module.

<img src="https://raw.githubusercontent.com/SeeedDocument/Grove-CO2-Temperature-Humidity-Sensor-SCD30/master/img/pinout.jpg" width="700" height="500">

*Size: 58mm x 38mm x 19mm

*Interface: I2C

### Sensor Specifications:

Measurement | Range | Accuracy |
----------- | ----- | -------- |
C02 | 0 – 40’000 ppm | ± (30 ppm + 3%MV) |
Humidity | 0 %RH – 100 %RH | ± 3 %RH |
Temperature | - 40°C – 70°C | ± (0.4°C + 0.023 × (T [°C] – 25°C)) |

## HM3301 Dust Sensor:

#### The HM3301 is a laser dust detection sensor.

<img src="https://files.seeedstudio.com/wiki/Grove-Laser_PM2.5_Sensor-HM3301/img/pin_out.jpg">

*Interface: I2C

*Range: 1~500µg/ m3 (Effective Range)

*Particle Size: 3 channels-- 2.5µm, 5µm, 10µm

### Sensor Specifications:

Measurement | Value | 
----------- | ----- | 
Operating Voltage | 3.3V / 5V  |
Operating Humidity | 10%～90%RH (non-condensing) |
Operating Temperature | -10～60℃ |

#### HM-3301 Dust Sensor is based on the Mie scattering theory. Light passes through particles with an amount equal to or greater than the wavelength of the light, light scattering forms.
#### Scattered light -> photodiode -> photodiode is amplified and analyzed by a circuit -> concentrations of the dust particles are aquired

<img src="https://files.seeedstudio.com/wiki/Grove-Laser_PM2.5_Sensor-HM3301/img/principle.jpg" width="501" height="300">

## Alphasense OPC-N3:

#### The OPC-N3 Sensor uses laser beams to identify particles..Measures up to 40µm for pollen.

<img src="https://airqualitynews.com/wp-content/uploads/2018/04/OPC-N3-sensor-768x599.jpg" width="395" height="308">

*Digital Interface: SPI

*Dimensions: 75mm x 60mm x 63.5mm

### Sensor Specifications:
Measurement |       | 
----------- | ----- | 
Particle Range | 0.35 to 40µm |
Max Particle Count Rate | 10,000 Particles/Second | 

Measurement | Range | 
----------- | ----- | 
Humidity | 0 to 95%RH (non-condensing) |
Temperature | -10 to 50°C | 

## Humidity, Pressure, and Temperature Sensor BME280:

#### The BME280 combines a pressure sensor, humidity sensor, and temperature sensor in one.

<img src="https://cdn-shop.adafruit.com/1200x900/2652-03.jpg" width="500" height="400">

*Size: 2.5mm x 2.5mm x 0.93mm³

*Interface: I²C and SPI

### Sensor Specifications:

Measurement | Range | Accuracy |
----------- | ----- | -------- |
Pressure | 300 - 1100 hPa| ±0.12hPa |
Humidity | 0 %RH – 100 %RH | ± 3 %RH |
Temperature | -40 - 85°C | ±1.0 -40°C - 65°C |

## Grove – Multichannel Gas Sensor (MGS001:)

#### Gas detecting sensor with a built in MiCS-6814 that allows three gases to be measured concurrently, on account of its multi-channels. 

<img src="https://files.seeedstudio.com/wiki/Grove-Multichannel_Gas_Sensor/img/Multi_sensor1.png" width="530" height="315">

*Interface: I²C

### Sensor Specifications:

Detectable Gases | Range |                                  
----------- | ----- | 
Carbon monoxide CO | 1 – 1000ppm|
Nitrogen dioxide NO<sub>2</sub> | 0.05 – 10ppm |
Ethanol C<sub>2</sub>H<sub>5</sub>OH  | 10 – 500ppm | 
Hydrogen H<sub>2</sub> | 1 – 1000ppm |
Ammonia NH<sub>3</sub> | 1 – 500ppm |
Methane CH<sub>4</sub> | >1000ppm | 
Propane C<sub>3</sub>H<sub>8</sub> | >1000ppm |
Iso-butane C<sub>4</sub>H<sub>10</sub> | >1000ppm | 

Red Sensor | Range |                
----------- | ----- |                 
Sensing Resistance in Air | 100-1500kΩ|            
Typical CO Detection Range | 1-1000ppm |
Sensitivity Factor	 | 1.2-50 |

OX Sensor | Range |                
----------- | ----- |                 
Sensing Resistance in Air | .8-20kΩ |            
Typical NO<sub>2</sub> Detection Range | 0.05-10ppm |
Sensitivity Factor	 | 2 |

NH3 Sensor | Range |                
----------- | ----- |                 
Sensing Resistance in Air | 10-1500kΩ|            
Typical NH<sub>3</sub> Detection Range | 1-300ppm |
Sensitivity Factor	 | 1.5-15 |
