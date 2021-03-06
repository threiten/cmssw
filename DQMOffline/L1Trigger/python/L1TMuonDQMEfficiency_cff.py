import FWCore.ParameterSet.Config as cms

from DQMOffline.L1Trigger.L1TMuonDQMOffline_cfi import muonEfficiencyThresholds, muonEfficiencyThresholds_HI

plots = ["EffvsPt", "EffvsEta", "EffvsPhi",
        "EffvsPt_OPEN", "EffvsEta_OPEN", "EffvsPhi_OPEN",
        "EffvsPt_DOUBLE", "EffvsEta_DOUBLE", "EffvsPhi_DOUBLE",
        "EffvsPt_SINGLE", "EffvsEta_SINGLE", "EffvsPhi_SINGLE"]

allEfficiencyPlots = []
for plot in plots:
    for threshold in muonEfficiencyThresholds:
        plotName = '{0}_{1}'.format(plot, threshold)
        allEfficiencyPlots.append(plotName)

allEfficiencyPlots_HI = []
for plot in plots:
    for threshold in muonEfficiencyThresholds_HI:
        plotName = '{0}_{1}'.format(plot, threshold)
        allEfficiencyPlots_HI.append(plotName)

from DQMOffline.L1Trigger.L1TEfficiencyHarvesting_cfi import l1tEfficiencyHarvesting
l1tMuonDQMEfficiency = l1tEfficiencyHarvesting.clone(
    plotCfgs = cms.untracked.VPSet(
        cms.untracked.PSet(
            numeratorDir = cms.untracked.string("L1T/L1TMuon/numerators_and_denominators"),
            outputDir = cms.untracked.string("L1T/L1TMuon"),
            numeratorSuffix = cms.untracked.string("_Num"),
            denominatorSuffix = cms.untracked.string("_Den"),
            plots = cms.untracked.vstring(allEfficiencyPlots)
        )
    )
)

# modifications for the pp reference run
from Configuration.Eras.Modifier_ppRef_2017_cff import ppRef_2017
ppRef_2017.toModify(l1tMuonDQMEfficiency,
    plotCfgs = cms.untracked.VPSet(
        cms.untracked.PSet(
            numeratorDir = cms.untracked.string("L1T/L1TMuon/numerators_and_denominators"),
            outputDir = cms.untracked.string("L1T/L1TMuon"),
            numeratorSuffix = cms.untracked.string("_Num"),
            denominatorSuffix = cms.untracked.string("_Den"),
            plots = cms.untracked.vstring(allEfficiencyPlots_HI)
        )
    )
)

