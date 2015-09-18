# -*- coding: utf-8 -*-
def extract_band(hdf_image_id, working_directory, hdf_file, output_directory, band):
    '''
    Функция извлекает указанный канал из изображения, преобразует в проекцию и сохраняет в указанную директорию
    :param working_directory: Рабочая директория, в которой находится файл
    :param hdf_file: Имя изображения
    :param output_directory: Выходной путь
    :param band: Указанный канал для экспорта
    :return: Bool
    '''
    import os
    import ImagesBandsCtrl as ImagesBandsCtrl
    try:
        os.chdir(working_directory)
        os.system('''gdalwarp \
                        -t_srs "+proj=longlat +ellps=wgs84 +datum=wgs84" -multi \
                        -co COMPRESS=DEFLATE -co "TILED=YES" \
                        -overwrite \
                        -of GTiff 'HDF4_EOS:EOS_GRID:"{0}{1}":{4}' \
                        {2}{3}_"{4}".tif'''.format(working_directory, hdf_file, output_directory, hdf_file[:-4], band))

        filename =hdf_file[:-4] +'_'+band+'.tif'
        #hdf_file[:-4]
        size = os.stat(output_directory + filename).st_size
        print('ImagesBands')
        ImagesBandsCtrl.create(filename, hdf_image_id, band, size, output_directory)
        return True

    except Exception as e:
        print(e)
        return False
def convert_to_tif(hdf_file, working_directory, output_directory):
    """
    Функция конвертирует изображения через коммандную строку
    working_directory - директория в которой находятся hdf файлы
    output_directory - путь, куда сохраняются tif файлы
    """
    import os
    import datetime
    os.chdir(working_directory)

    year = hdf_file[9:13]
    day_of_year = hdf_file[13:16]
    # Конвертирование day_of_year в date
    date = datetime.date(int(year), 1, 1) + datetime.timedelta(int(day_of_year) - 1)


    output_filename = hdf_file[:23].replace(".", "_") + '_' + str(date)

    os.system('''gdalwarp -t_srs "+proj=longlat +ellps=wgs84 +datum=wgs84" -co COMPRESS=DEFLATE -co "TILED=YES" -of GTiff 'HDF4_EOS:EOS_GRID:"{0}{1}":MODIS_Grid_16DAY_500m_VI:500m 16 days NDVI' {2}{3}_16_Day_ndvi_500m.tif'''.format(working_directory, hdf_file, output_directory, output_filename))

    # os.system('''gdal_calc.py --co COMPRESS=DEFLATE --co  -A {0}{1}_16_Day_ndvi_500m_temp.tif --outfile={0}{1}_16_Day_ndvi_500m.tif --calc="A*0.0001"'''.format(output_directory, output_filename))
    #

    # from osgeo import gdal
    #
    # raster = gdal.Open('{0}{1}_16_Day_ndvi_500m_temp.tif'.format(output_directory, output_filename))
    # array = raster.ReadAsArray()       #Получение массива
    # array = array * 0.0001
    # geo_transform = (62.22895306301703, 0.003017612488776469, 0.0, 59.999999994611805, 0.0, -0.003017612488776469)
    # x_size = 12517
    # y_size = 3314
    # srs = 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433],AUTHORITY["EPSG","4326"]]'
    # driver = gdal.GetDriverByName("GTiff")
    #
    # dataset_out = driver.Create(output_directory+output_filename+"_16_Day_ndvi_500m.tif", x_size, y_size, 1, gdal.GDT_Float32)
    # dataset_out.SetGeoTransform(geo_transform)
    # dataset_out.SetProjection(srs)
    # dataset_out.GetRasterBand(1).WriteArray(array)
    #
    # os.remove("{0}_16_Day_ndvi_500m_temp.tif".format(output_directory + output_filename))


def save_tif(output_name, raster_data):

    from osgeo import gdal

    # sample = gdal.Open(dataset)
    geo_transform = (62.22895306301703, 0.003017612488776469, 0.0, 59.999999994611805, 0.0, -0.003017612488776469)
    x_size = 12517
    y_size = 3314
    srs = 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433],AUTHORITY["EPSG","4326"]]'
    driver = gdal.GetDriverByName("GTiff")

    dataset_out = driver.Create(output_name, x_size, y_size, 1, gdal.GDT_Float32, [ 'TILED=YES', 'COMPRESS=DEFLATE' ])
    dataset_out.SetGeoTransform(geo_transform)
    dataset_out.SetProjection(srs)
    dataset_out.GetRasterBand(1).WriteArray(raster_data)
