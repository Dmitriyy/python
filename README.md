# -*- coding: utf-8 -*-
def extract_band(working_directory, hdf_file, output_directory, band):
    '''
    Функция извлекает указанный канал из изображения, преобразует в проекцию и сохраняет в указанную директорию
    :param working_directory: Рабочая директория, в которой находится файл
    :param hdf_file: Имя изображения
    :param output_directory: Выходной путь
    :param band: Указанный канал для экспорта
    :return: Bool
    '''
    import os,re
    os.chdir(working_directory)

    # читаем метаданные HDF
    scene_gdalinfo = os.popen("gdalinfo " + hdf_file).read()
    #print scene_gdalinfo
    # Смотрим, как называется слой NDVI (SUBDATASET_1)
    prefix = ''.join(re.findall('SUBDATASET_1_NAME.*?\n', scene_gdalinfo))
    prefix = prefix.replace('\n', '')
    prefix = prefix.replace('SUBDATASET_1_NAME='+'HDF4_EOS:EOS_GRID:', '')
    prefix = prefix.replace('"'+hdf_file+'"'+':', '')
    prefix = prefix.replace(':'+band, '')
    #print band
    try:
        os.chdir(working_directory)
        os.system('''gdalwarp \
                        -t_srs "+proj=longlat +ellps=wgs84 +datum=wgs84"-multi \
                        -co COMPRESS=DEFLATE -co "TILED=YES" \
                        -overwrite \
                        -of GTiff 'HDF4_EOS:EOS_GRID:"{0}{1}":{5}:{4}' \
                        {2}{3}_"{4}".tif'''.format(working_directory, hdf_file, output_directory, hdf_file[:-4], band, prefix))

        return True
    except:
        return False

working_directory = "/media/1tb/images/hdf/mod09gq/2007/"
hdf_file = "MOD09GQ.A2007001.h22v03.005.2008132222251.hdf"
output_directory = "/home/pavel/testing/"

band = "num_observations"

extract_band( working_directory, hdf_file, output_directory, band)
