import os.path

from lsst.utils import getPackageDir
from lsst.meas.algorithms import LoadPanstarrsObjectsTask
from lsst.obs.decam.isr import DecamIsrTask
config.isr.retarget(DecamIsrTask)

decamConfigDir = os.path.join(getPackageDir('obs_decam'), 'config')
config.isr.load(os.path.join(decamConfigDir, 'isr.py'))

config.charImage.repair.cosmicray.nCrPixelMax = 100000

for refObjLoader in (config.calibrate.astromRefObjLoader,
                     config.calibrate.photoRefObjLoader,
                     config.charImage.refObjLoader,
                     ):
    refObjLoader.retarget(LoadPanstarrsObjectsTask)
    refObjLoader.ref_dataset_name = "ps1_pv3_3pi_20170110"
    # Note the u-band results may not be useful without a color term
    refObjLoader.filterMap['u'] = 'g'
    refObjLoader.filterMap['Y'] = 'y'


config.calibrate.photoCal.photoCatName = "ps1_pv3_3pi_20170110"
# this was the default prior to DM-11521.  New default is 2000.
config.calibrate.deblend.maxFootprintSize = 0
