cvs_params = {
    "logy": True,
    "grid": True
}
info_params = {
    "info": "Normalized to #it{L}_{int} = 150 fb^{-1}",
	"cms_text": "CMS",
	"extra_text": "Work on progress"
} 
params = {
    # Z
    "ZMass": {
        "hist_params": {
            "rebin": 20,
            "x_title": "M(ll)",
            "y_title": "Events",
            "ratio_title": "x/Default",
            "ratio_range": [0.5, 1.5]
        },
    },
    "yZ": {
        "hist_params": {
            "x_title": "y^{Z}",
            "y_title": "Events",
            "ratio_title": "x/Default",
            "ratio_range": [0.5, 1.5],
        },
    },
    "ptZ": {
        "hist_params": {
            "rebin": 2,
            "x_title": "p_{T}(Z)",
            "y_title": "Events",
            "ratio_title": "x/Default",
            "x_range": [0., 200.],
            "ratio_range": [0.5, 1.5],
        },
    },
    "phiZ": {
        "hist_params": {
            "x_title": "#phi(Z)",
            "y_title": "Events",
            "ratio_title": "x/Default",
            "ratio_range": [0.5, 1.5],
        },
    },
    # Leptons
    "ptl1": {
        "hist_params": {
            "rebin": 2,
            "x_title": "p_{T}(l1)",
            "y_title": "Events",
            "ratio_title": "x/Default",
            "x_range": [0., 200.],
            "ratio_range": [0.5, 1.5],
        },
    },
    "ptl2": {
        "hist_params": {
            "rebin": 2,
            "x_title": "p_{T}(l2)",
            "y_title": "Events",
            "ratio_title": "x/Default",
            "x_range": [0., 200.],
            "ratio_range": [0.5, 1.5],
        },
    },
    "etal1": {
        "hist_params": {
            "x_title": "#eta(l1)",
            "y_title": "Events",
            "ratio_title": "x/Default",
            "ratio_range": [0.5, 1.5],
        },
    },
    "etal2": {
        "hist_params": {
            "x_title": "#eta(l2)",
            "y_title": "Events",
            "ratio_title": "x/Default",
            "ratio_range": [0.5, 1.5],
        },
    },
    "phil1": {
        "hist_params": {
            "x_title": "#phi(l1)",
            "y_title": "Events",
            "ratio_title": "x/Default",
            "ratio_range": [0.5, 1.5],
        },
    },
    "phil2": {
        "hist_params": {
            "x_title": "#phi(l2)",
            "y_title": "Events",
            "ratio_title": "x/Default",
            "ratio_range": [0.5, 1.5],
        },
    },
    "nLeptons": {
        "hist_params": {
            "x_title": "N(l)",
            "y_title": "Events",
            "ratio_title": "x/Default",
            "ratio_range": [0.5, 1.5],
        },
    },
    # Jets
    "ptj1": {
        "hist_params": {
            "x_title": "p_{T}(j1)",
            "y_title": "Events",
            "ratio_title": "x/Default",
            "x_range": [0., 200.],
            "ratio_range": [0., 2.0],
        },
    },
    "ptj2": {
        "hist_params": {
            "x_title": "p_{T}(j2)",
            "y_title": "Events",
            "ratio_title": "x/Default",
            "x_range": [0., 200.],
            "ratio_range": [0., 2.0],
        },
    },
    "etaj1": {
        "hist_params": {
            "x_title": "#eta(j1)",
            "y_title": "Events",
            "ratio_title": "x/Default",
            "ratio_range": [0., 2.0],
        },
    },
    "etaj2": {
        "hist_params": {
            "x_title": "#eta(j2)",
            "y_title": "Events",
            "ratio_title": "x/Default",
            "ratio_range": [0., 2.0],
        },
    },
    "phij1": {
        "hist_params": {
            "x_title": "#phi(j1)",
            "y_title": "Events",
            "ratio_title": "x/Default",
            "ratio_range": [0., 2.0],
        },
    },
    "phij2": {
        "hist_params": {
            "x_title": "#phi(j2)",
            "y_title": "Events",
            "ratio_title": "x/Default",
            "ratio_range": [0., 2.0],
        },
    },
    "nJets": {
        "hist_params": {
            "x_title": "N(j)",
            "y_title": "Events",
            "ratio_title": "x/Default",
            "ratio_range": [0.0, 2.0],
        },
    },
    "dRl1l2": {
        "hist_params": {
            "x_title": "#Delta R(l1l2)",
            "y_title": "Events",
            "ratio_title": "x/Defalut",
            "x_range": [0., 6.],
            "ratio_range": [0.5, 1.5]
        },
    },
    "dRj1l1": {
        "hist_params": {
            "x_title": "#Delta R(j1l1)",
            "y_title": "Events",
            "ratio_title": "x/Defalut",
            "x_range": [0., 6.],
            "ratio_range": [0.5, 1.5]
        },
    },
    "dRj1l2": {
        "hist_params": {
            "x_title": "#Delta R(j1l2)",
            "y_title": "Events",
            "ratio_title": "x/Defalut",
            "x_range": [0., 6.],
            "ratio_range": [0.5, 1.5]
        },
    },
    "dRj2l1": {
        "hist_params": {
            "x_title": "#Delta R(j2l1)",
            "y_title": "Events",
            "ratio_title": "x/Defalut",
            "x_range": [0., 6.],
            "ratio_range": [0.5, 1.5]
        },
    },
    "dRj2l2": {
        "hist_params": {
            "x_title": "#Delta R(j2l2)",
            "y_title": "Events",
            "ratio_title": "x/Defalut",
            "x_range": [0., 6.],
            "ratio_range": [0.5, 1.5]
        },
    },
    "dRj1j2": {
        "hist_params": {
            "x_title": "#Delta R(j1j2)",
            "y_title": "Events",
            "ratio_title": "x/Defalut",
            "x_range": [0., 6.],
            "ratio_range": [0.5, 1.5]
        },
    },
}
