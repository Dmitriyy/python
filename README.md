# -*- coding: utf-8 -*-
"""
Скрипт проверяет в таблице images все HDF файлы с параметром is_processed = 0
В случае True, сохраняет каналы из изображения в папку и записывает в БД
"""

from controllers import ImagesCtrl, mod09ga
images = ImagesCtrl.all('mod09gq')
for image in images:
    print(image)

if image['is_processed'] == "0":
mod09ga.extract_band(image['path'], image['filename'], '/media/3tb/images/geotiff/images_bands/mod09ga/', 'MODIS_Grid_1km_2D:SensorZenith_1')
mod09ga.extract_band(image['path'], image['filename'], '/media/3tb/images/geotiff/images_bands/mod09ga/', 'MODIS_Grid_1km_2D:SensorAzimuth_1')
mod09ga.extract_band(image['path'], image['filename'], '/media/3tb/images/geotiff/images_bands/mod09ga/', 'MODIS_Grid_500m_2D:sur_refl_b01_1')
mod09ga.extract_band(image['path'], image['filename'], '/media/3tb/images/geotiff/images_bands/mod09ga/', 'MODIS_Grid_500m_2D:sur_refl_b02_1')
mod09ga.extract_band(image['path'], image['filename'], '/media/3tb/images/geotiff/images_bands/mod09ga/', 'MODIS_Grid_500m_2D:sur_refl_b03_1')
mod09ga.extract_band(image['path'], image['filename'], '/media/3tb/images/geotiff/images_bands/mod09ga/', 'MODIS_Grid_500m_2D:sur_refl_b04_1')
mod09ga.extract_band(image['path'], image['filename'], '/media/3tb/images/geotiff/images_bands/mod09ga/', 'MODIS_Grid_500m_2D:sur_refl_b05_1')
mod09ga.extract_band(image['path'], image['filename'], '/media/3tb/images/geotiff/images_bands/mod09ga/', 'MODIS_Grid_500m_2D:sur_refl_b06_1')
mod09ga.extract_band(image['path'], image['filename'], '/media/3tb/images/geotiff/images_bands/mod09ga/', 'MODIS_Grid_500m_2D:sur_refl_b07_1')

ImagesCtrl.set_processed(image['id'], 1)
