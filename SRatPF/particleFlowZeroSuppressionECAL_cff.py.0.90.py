import FWCore.ParameterSet.Config as cms

pfZeroSuppressionThresholds_EB = [0.080]*170
pfZeroSuppressionThresholds_EEminus = [0.300]*39
pfZeroSuppressionThresholds_EEplus = pfZeroSuppressionThresholds_EEminus

_pfZeroSuppressionThresholds_EB_2017 = [0.250]*170
_pfZeroSuppressionThresholds_EEminus_2017 = [1.12521 , 1.1253 , 1.12542 , 1.12561 , 1.12587 , 1.12625 , 1.12679 , 1.12757 , 1.12869 , 1.13028 ,   # rings 170-179 (EE-) / 209-218 (EE+) 
                                             1.13258 , 1.13586 , 1.14056 , 1.14731 , 1.15698 , 1.17083 , 1.19069 , 1.21916 , 1.25995 , 1.31844 ,  # rings 180-189 (EE-) / 219-228 (EE+)
                                             1.40226 , 1.5224 , 1.69462 , 1.94144 , 2.29524 , 2.80234 , 3.52918 , 4.57098 , 6.06423 , 8.20453 ,   # rings 190-199 (EE-) / 229-238 (EE+)
                                             9 , 9 , 9 , 9 , 9 , 9 , 9 , 9 , 9 ]  # rings 200-208 (EE-) / 239-247 (EE+)
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

