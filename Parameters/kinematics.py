params = {
    # Leading prompt muons
    "1/pt": {
        "cvs_params": {
            "grid": True
        },
        "hist_params": {
            "rebin": 5,
            "x_title": "p_{T}(#mu1)",
            "x_range": [0., 150.],
            "y_title": "A.U.",
            "ratio_title": "x/Default",
            "ratio_range": [0., 5.0]
        },
        "info_params": {
            "info": "Normalized to 1",
            "cms_text": "CMS",
            "extra_text": "Work on progress"
        }
    },
    # Subleading prompt muons
    "2/pt": {
        "cvs_params": {
            "grid": True
        },
        "hist_params": {
            "rebin": 5,
            "x_title": "p_{T}(#mu2)",
            "x_range": [0., 160.],
            "y_title": "A.U.",
            "ratio_title": "x/Default",
            "ratio_range": [0., 2.0]
        },
        "info_params": {
            "info": "Normalized to 1",
            "cms_text": "CMS",
            "extra_text": "Work on progress"
        }
    }
}
