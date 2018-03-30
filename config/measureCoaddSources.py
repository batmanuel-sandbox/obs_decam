from lsst.meas.algorithms import LoadPanstarrsObjectsTask
config.match.refObjLoader.retarget(LoadPanstarrsObjectsTask)
config.match.refObjLoader.ref_dataset_name = "ps1_pv3_3pi_20170110"
config.match.refObjLoader.filterMap['u'] = 'g'
config.match.refObjLoader.filterMap['Y'] = 'y'
