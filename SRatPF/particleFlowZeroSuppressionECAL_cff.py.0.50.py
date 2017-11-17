import FWCore.ParameterSet.Config as cms

pfZeroSuppressionThresholds_EB = [0.080]*170
pfZeroSuppressionThresholds_EEminus = [0.300]*39
pfZeroSuppressionThresholds_EEplus = pfZeroSuppressionThresholds_EEminus

_pfZeroSuppressionThresholds_EB_2017 = [0.250]*170
_pfZeroSuppressionThresholds_EEminus_2017 = [0.625115 , 0.625165 , 0.625235 , 0.62534 , 0.625485 , 0.625695 , 0.625995 , 0.62643 , 0.62705 , 0.627935 ,   # rings 170-179 (EE-) / 209-218 (EE+) 
                                             0.62921 , 0.631035 , 0.633645 , 0.637395 , 0.642765 , 0.65046 , 0.661495 , 0.67731 , 0.699975 , 0.732465 ,   # rings 180-189 (EE-) / 219-228 (EE+)
                                             0.779035 , 0.84578 , 0.941455 , 1.07858 , 1.27514 , 1.55685 , 1.96065 , 2.53943 , 3.36901 , 4.55807 ,        # rings 190-199 (EE-) / 229-238 (EE+)
                                             5 , 5 , 5 , 5 , 5 , 5 , 5 , 5 , 5]  # rings 200-208 (EE-) / 239-247 (EE+)
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

