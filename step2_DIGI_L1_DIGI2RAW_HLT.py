# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions 92X_upgrade2017_realistic_forECALStudies_ZeroN -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2017 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG -n 10 --era Run2_2017 --eventcontent FEVTDEBUGHLT
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_2e34v21_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    #fileNames = cms.untracked.vstring('/store/relval/CMSSW_9_2_9/RelValQCD_FlatPt_15_3000HS_13UP17/GEN-SIM/92X_upgrade2017_realistic_Candidate_forECALStudies_HS1M-v2/00000/0254DA66-8A9A-E711-A1A4-0242AC130002.root'),
    fileNames = cms.untracked.vstring('/store/relval/CMSSW_9_2_1/RelValZEE_13/GEN-SIM/92X_upgrade2017_realistic_v1-v1/10000/2EFD0D12-8E47-E711-95AE-0025905B857A.root'),
    
    inputCommands = cms.untracked.vstring('keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW-HLTDEBUG'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(10485760),
    fileName = cms.untracked.string('step2_DIGI_L1_DIGI2RAW_HLT.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_upgrade2017_realistic_forECALStudies_ZeroN', '')


process.GlobalTag.toGet = cms.VPSet(


         cms.PSet(record = cms.string("EcalPedestalsRcd"),
            tag = cms.string("EcalPedestals_2017extrap_25fb_mc"),
            #tag = cms.string("EcalPedestals_2017_rms0.000001_mc"),
            #tag = cms.string("EcalPedestals_2017_rms0.2887_mc"),
            #tag = cms.string("EcalPedestals_2017_rms0.2887_EBEE_mc"),
            #tag = cms.string("EcalPedestals_2017_rms1.0_mc"),
            connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
            ),

)



# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi_valid)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)


# remove noise


#process.ecal_electronics_sim = cms.PSet(
    #ConstantTerm = cms.double(0.003),
    #applyConstantTerm = cms.bool(True),
    #doENoise = cms.bool(False)
#)

#process.theDigitizers.ecal = cms.PSet(
        #ConstantTerm = cms.double(0.003),
        #EBCorrNoiseMatrixG01 = cms.vdouble(1.0, 0.73354, 0.64442, 0.58851, 0.55425, 
            #0.53082, 0.51916, 0.51097, 0.50732, 0.50409),
        #EBCorrNoiseMatrixG06 = cms.vdouble(1.0, 0.70946, 0.58021, 0.49846, 0.45006, 
            #0.41366, 0.39699, 0.38478, 0.37847, 0.37055),
        #EBCorrNoiseMatrixG12 = cms.vdouble(1.0, 0.71073, 0.55721, 0.46089, 0.40449, 
            #0.35931, 0.33924, 0.32439, 0.31581, 0.30481),
        #EBdigiCollection = cms.string(''),
        #EBs25notContainment = cms.double(0.97),
        #EECorrNoiseMatrixG01 = cms.vdouble(1.0, 0.72698, 0.62048, 0.55691, 0.51848, 
            #0.49147, 0.47813, 0.47007, 0.46621, 0.46265),
        #EECorrNoiseMatrixG06 = cms.vdouble(1.0, 0.71217, 0.47464, 0.34056, 0.26282, 
            #0.20287, 0.17734, 0.16256, 0.15618, 0.14443),
        #EECorrNoiseMatrixG12 = cms.vdouble(1.0, 0.71373, 0.44825, 0.30152, 0.21609, 
            #0.14786, 0.11772, 0.10165, 0.09465, 0.08098),
        #EEdigiCollection = cms.string(''),
        #EEs25notContainment = cms.double(0.975),
        #ESdigiCollection = cms.string(''),
        #EcalPreMixStage1 = cms.bool(False),
        #EcalPreMixStage2 = cms.bool(False),
        #UseLCcorrection = cms.untracked.bool(True),
        #accumulatorType = cms.string('EcalDigiProducer'),
        #apdAddToBarrel = cms.bool(False),
        #apdDigiTag = cms.string('APD'),
        #apdDoPEStats = cms.bool(True),
        #apdNonlParms = cms.vdouble(1.48, -3.75, 1.81, 1.26, 2.0, 
            #45, 1.0),
        #apdSeparateDigi = cms.bool(True),
        #apdShapeTau = cms.double(40.5),
        #apdShapeTstart = cms.double(74.5),
        #apdSimToPEHigh = cms.double(88200000.0),
        #apdSimToPELow = cms.double(2450000.0),
        #apdTimeOffWidth = cms.double(0.8),
        #apdTimeOffset = cms.double(-13.5),
        #applyConstantTerm = cms.bool(True),
        #binOfMaximum = cms.int32(6),
        #cosmicsPhase = cms.bool(False),
        #cosmicsShift = cms.double(0.0),
        #doEB = cms.bool(True),
        #doEE = cms.bool(True),
        #doENoise = cms.bool(False),
        #doES = cms.bool(True),
        #doESNoise = cms.bool(True),
        #doFast = cms.bool(True),
        #doPhotostatistics = cms.bool(True),
        #hitsProducer = cms.string('g4SimHits'),
        #makeDigiSimLinks = cms.untracked.bool(False),
        #photoelectronsToAnalogBarrel = cms.double(0.000444444),
        #photoelectronsToAnalogEndcap = cms.double(0.000555555),
        #readoutFrameSize = cms.int32(10),
        #samplingFactor = cms.double(1.0),
        #simHitToPhotoelectronsBarrel = cms.double(2250.0),
        #simHitToPhotoelectronsEndcap = cms.double(1800.0),
        #syncPhase = cms.bool(True),
        #timePhase = cms.double(0.0)
    #)



##process.theDigitizersValid.ecal.doENoise = cms.bool(False)
##process.mix.ecal.doENoise = cms.bool(False)

#process.ecalDigitizer = cms.PSet(
    #ConstantTerm = cms.double(0.003),
    #EBCorrNoiseMatrixG01 = cms.vdouble(1.0, 0.73354, 0.64442, 0.58851, 0.55425, 
        #0.53082, 0.51916, 0.51097, 0.50732, 0.50409),
    #EBCorrNoiseMatrixG06 = cms.vdouble(1.0, 0.70946, 0.58021, 0.49846, 0.45006, 
        #0.41366, 0.39699, 0.38478, 0.37847, 0.37055),
    #EBCorrNoiseMatrixG12 = cms.vdouble(1.0, 0.71073, 0.55721, 0.46089, 0.40449, 
        #0.35931, 0.33924, 0.32439, 0.31581, 0.30481),
    #EBdigiCollection = cms.string(''),
    #EBs25notContainment = cms.double(0.97),
    #EECorrNoiseMatrixG01 = cms.vdouble(1.0, 0.72698, 0.62048, 0.55691, 0.51848, 
        #0.49147, 0.47813, 0.47007, 0.46621, 0.46265),
    #EECorrNoiseMatrixG06 = cms.vdouble(1.0, 0.71217, 0.47464, 0.34056, 0.26282, 
        #0.20287, 0.17734, 0.16256, 0.15618, 0.14443),
    #EECorrNoiseMatrixG12 = cms.vdouble(1.0, 0.71373, 0.44825, 0.30152, 0.21609, 
        #0.14786, 0.11772, 0.10165, 0.09465, 0.08098),
    #EEdigiCollection = cms.string(''),
    #EEs25notContainment = cms.double(0.975),
    #ESdigiCollection = cms.string(''),
    #EcalPreMixStage1 = cms.bool(False),
    #EcalPreMixStage2 = cms.bool(False),
    #UseLCcorrection = cms.untracked.bool(True),
    #accumulatorType = cms.string('EcalDigiProducer'),
    #apdAddToBarrel = cms.bool(False),
    #apdDigiTag = cms.string('APD'),
    #apdDoPEStats = cms.bool(True),
    #apdNonlParms = cms.vdouble(1.48, -3.75, 1.81, 1.26, 2.0, 
        #45, 1.0),
    #apdSeparateDigi = cms.bool(True),
    #apdShapeTau = cms.double(40.5),
    #apdShapeTstart = cms.double(74.5),
    #apdSimToPEHigh = cms.double(88200000.0),
    #apdSimToPELow = cms.double(2450000.0),
    #apdTimeOffWidth = cms.double(0.8),
    #apdTimeOffset = cms.double(-13.5),
    #applyConstantTerm = cms.bool(True),
    #binOfMaximum = cms.int32(6),
    #cosmicsPhase = cms.bool(False),
    #cosmicsShift = cms.double(0.0),
    #doEB = cms.bool(True),
    #doEE = cms.bool(True),
    #doENoise = cms.bool(False),
    #doES = cms.bool(True),
    #doESNoise = cms.bool(True),
    #doFast = cms.bool(True),
    #doPhotostatistics = cms.bool(True),
    #hitsProducer = cms.string('g4SimHits'),
    #makeDigiSimLinks = cms.untracked.bool(False),
    #photoelectronsToAnalogBarrel = cms.double(0.000444444),
    #photoelectronsToAnalogEndcap = cms.double(0.000555555),
    #readoutFrameSize = cms.int32(10),
    #samplingFactor = cms.double(1.0),
    #simHitToPhotoelectronsBarrel = cms.double(2250.0),
    #simHitToPhotoelectronsEndcap = cms.double(1800.0),
    #syncPhase = cms.bool(True),
    #timePhase = cms.double(0.0)
#)
    
    
    


# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.FEVTDEBUGHLToutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
