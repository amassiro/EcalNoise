import FWCore.ParameterSet.Config as cms

pfZeroSuppressionThresholds_EB = [0.080]*170
pfZeroSuppressionThresholds_EEminus = [0.300]*39
pfZeroSuppressionThresholds_EEplus = pfZeroSuppressionThresholds_EEminus

_pfZeroSuppressionThresholds_EB_2017 = [0.250]*170
_pfZeroSuppressionThresholds_EEminus_2017 = [0.875161 , 0.875231 , 0.875329 , 0.875476 , 0.875679 , 0.875973 , 0.876393 , 0.877002 , 0.87787 , 0.879109 ,  # rings 170-179 (EE-) / 209-218 (EE+) 
                                             0.880894 , 0.883449 , 0.887103 , 0.892353 , 0.899871 , 0.910644 , 0.926093 , 0.948234 , 0.979965 , 1.02545 ,  # rings 180-189 (EE-) / 219-228 (EE+)
                                             1.09065 , 1.18409 , 1.31804 , 1.51001 , 1.78519 , 2.1796 , 2.74492 , 3.55521 , 4.71662 , 6.3813 ,   # rings 190-199 (EE-) / 229-238 (EE+)
                                             7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 , 7 ]  # rings 200-208 (EE-) / 239-247 (EE+)
_pfZeroSuppressionThresholds_EEplus_2017 = _pfZeroSuppressionThresholds_EEminus_2017



particle_flow_zero_suppression_ECAL = cms.PSet(
    thresholds = cms.vdouble(pfZeroSuppressionThresholds_EB + pfZeroSuppressionThresholds_EEminus + pfZeroSuppressionThresholds_EEplus
        )
    )

_particle_flow_zero_suppression_ECAL_2017 = cms.PSet(
    thresholds = cms.vdouble(_pfZeroSuppressionThresholds_EB_2017 + _pfZeroSuppressionThresholds_EEminus_2017 + _pfZeroSuppressionThresholds_EEplus_2017
        )
    )

from Configuration.Eras.Modifier_run2_ECAL_2017_cff import run2_ECAL_2017
run2_ECAL_2017.toReplaceWith(particle_flow_zero_suppression_ECAL, _particle_flow_zero_suppression_ECAL_2017)

from Configuration.Eras.Modifier_phase2_ecal_cff import phase2_ecal
phase2_ecal.toReplaceWith(particle_flow_zero_suppression_ECAL, _particle_flow_zero_suppression_ECAL_2017)

