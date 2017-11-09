# EcalNoise


Where:

    /afs/cern.ch/user/a/amassiro/work/ECAL/Pulses/CMSSW_9_2_9/src
    
    
Tests: 

    voms-proxy-init --voms cms

    
    
    Input: /RelValQCD_FlatPt_15_3000HS_13UP17/CMSSW_9_2_9-92X_upgrade2017_realistic_Candidate_forECALStudies_HS1M-v2/GEN-SIM
    /store/relval/CMSSW_9_2_9/RelValQCD_FlatPt_15_3000HS_13UP17/GEN-SIM/92X_upgrade2017_realistic_Candidate_forECALStudies_HS1M-v2/00000/0254DA66-8A9A-E711-A1A4-0242AC130002.root
    
    cmsDriver.py step2 --conditions 92X_upgrade2017_realistic_forECALStudies_ZeroN -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2017 --datatier GEN-SIM-DIGI-RAW-HLTDEBUG -n 10 --era Run2_2017 --eventcontent FEVTDEBUGHLT
    cmsRun step2_DIGI_L1_DIGI2RAW_HLT.py
    
    cmsDriver.py step3 --conditions 92X_upgrade2017_realistic_forECALStudies_ZeroN -n 10 --era Run2_2017 --eventcontent RECOSIM,MINIAODSIM,DQM --runUnscheduled  -s RAW2DIGI,L1Reco,RECO,EI,PAT,VALIDATION:@standardValidation+@miniAODValidation,DQM:@standardDQM+@miniAODDQM --datatier GEN-SIM-RECO,MINIAODSIM,DQMIO 
    cmsRun step3_RAW2DIGI_L1Reco_RECO_EI_PAT_VALIDATION_DQM.py
    
    
    
    /RelValZEE_13/CMSSW_9_2_1-92X_upgrade2017_realistic_v1-v1/GEN-SIM
    /store/relval/CMSSW_9_2_1/RelValZEE_13/GEN-SIM/92X_upgrade2017_realistic_v1-v1/10000/2EFD0D12-8E47-E711-95AE-0025905B857A.root
    
    cmsRun step2_DIGI_L1_DIGI2RAW_HLT.py
    
    cmsRun step3_RAW2DIGI_L1Reco_RECO_EI_PAT_VALIDATION_DQM.py
    
    
    
Dump TP information:

    cd ~/work/ECAL/CMSSW_9_3_0_pre4/src/ECALValidation/EcalTP/test/
    cmsenv

    cmsRun runRawtoRecoAndDump.py             inputFiles=file:/afs/cern.ch/user/a/amassiro/work/ECAL/Pulses/CMSSW_9_2_9/src/EcalNoise/step2_DIGI_L1_DIGI2RAW_HLT.root    outputFile=noNoise.root
 
    cmsRun runRawtoRecoAndDump.py             inputFiles=file:/afs/cern.ch/user/a/amassiro/work/ECAL/Pulses/CMSSW_9_2_9/src/EcalNoise/step2_DIGI_L1_DIGI2RAW_HLT.root    outputFile=noNoise.newConfigSasha.root
    cmsRun runRawtoRecoAndDump.py             inputFiles=file:/afs/cern.ch/user/a/amassiro/work/ECAL/Pulses/CMSSW_9_2_9/src/EcalNoise/step2_DIGI_L1_DIGI2RAW_HLT.root    outputFile=noNoise.newConfigSasha.hardcoded.root
    
    cmsRun runRawtoRecoAndDump.py             inputFiles=file:/afs/cern.ch/user/a/amassiro/work/ECAL/Pulses/CMSSW_9_2_9/src/EcalNoise/step2_DIGI_L1_DIGI2RAW_HLT.root    outputFile=withNoise.root
    
    cmsRun runRawtoRecoAndDump.py             inputFiles=file:/afs/cern.ch/user/a/amassiro/work/ECAL/Pulses/CMSSW_9_2_9/src/EcalNoise/step2_DIGI_L1_DIGI2RAW_HLT.root    outputFile=withoutNoise.root
    
 
    TTree* tree = (TTree*) _file0->Get("TreeProducer/tree")
    tree ->Draw("TPflag*(TPflag<2)+(TPflag>=2)*2>>h(3,0,3", "TPonlineETADC>-1", "colz");
    h->GetXaxis()->SetTitle("TP flag");
    h->Scale (1./h->Integral());
    h->SetLineWidth(2);
    h->Draw("hist");
    h->GetBinContent (1)
    h->GetBinContent (2)
    h->GetBinContent (3)
