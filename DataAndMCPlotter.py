from ROOT import TFile, TH1D
from ObsAndExp import ObsAndExp
from Parameters.obs_and_exp import param_set, cvs_params, info_params

# Get histograms
hist_obs = None
hists_exp = {}

skflat_output = "/data0/CRstudy/2017/"
observables = {
    "DY_DiMu": {
        "leptons": ["ptmu1", "ptmu2", "etamu1", "etamu2", "phimu1", "phimu2"],
        "jets": ["ptj1", "ptj2", "ptj3", "etaj1", "etaj2", "etaj3", "phij1", "phij2", "phij3", "nJets"],
        "METv": ["METv", "etaMETv", "phiMETv"],
        "bjets": [],
        "ZCand": ["ptZ", "etaZ", "phiZ", "Zmass"]
    },
    "TT_DiMu": {
        "leptons": ["ptmu1", "ptmu2", "etamu1", "etamu2", "phimu1", "phimu2"],
        "jets": ["ptj1", "ptj2", "ptj3", "etaj1", "etaj2", "etaj3", "phij1", "phij2", "phij3", "nJets"],
        "METv": ["METv", "etaMETv", "phiMETv"],
        "bjets": ["ptb1", "ptb2", "ptb3", "etab1", "etab2", "etab3", "phib1", "phib2", "phib3", "nBJets"],
        "ZCand": ["ptZ", "etaZ", "phiZ", "Zmass"]
    },
    "TT_EMu": {
        "leptons": ["ptmu1", "pte1", "etamu1", "etae1", "phimu1", "phie1"],
        "jets": ["ptj1", "ptj2", "ptj3", "etaj1", "etaj2", "etaj3", "phij1", "phij2", "phij3", "nJets"],
        "METv": ["METv", "etaMETv", "phiMETv"],
        "bjets": ["ptb1", "ptb2", "ptb3", "etab1", "etab2", "etab3", "phib1", "phib2", "phib3", "nBJets"],
        "ZCand": []
    }
}


if __name__ == "__main__":
    data = "MuonEG"
    mcsamples = ["fake", "VV", "SingleTop", "TTLL", "DY"]
    channel = "TT_EMu"
    output_path = "/root/workspace/www/CRstudy"

    leptons = observables[channel]["leptons"]
    jets = observables[channel]["jets"]
    bjets = observables[channel]["bjets"]
    met = observables[channel]["METv"]
    zcand = observables[channel]['ZCand']
    all_obs = leptons + jets + bjets + met + zcand
    params = param_set[channel]

    file = TFile()
    for obs in all_obs:
        hist_params = params[obs]["hist_params"]
        path_to_hist = channel + params[obs]["path"]
        print(path_to_hist)
        file = TFile(skflat_output+"DATA/CRstudy_"+data+".root")
        hist = file.Get(path_to_hist)
        hist.SetDirectory(0)
        hist_obs = hist

        for sample in mcsamples:
            if sample == "TTLL":
                file = TFile(skflat_output+"/CRstudy_TTLL_powheg.root")
            else:
                file = TFile(skflat_output+"CRstudy_"+sample+".root")
            hist = file.Get(path_to_hist)
            hist.SetDirectory(0)
            hists_exp[sample] = hist

        plotter = ObsAndExp(cvs_params, hist_params, info_params)
        plotter.get_hists(hist_obs, hists_exp)
        plotter.combine()
        save_name = output_path + "/DataAndMC_" + channel + "_" + obs + ".png"
        plotter.save(save_name)
